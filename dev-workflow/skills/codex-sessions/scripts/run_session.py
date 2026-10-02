#!/usr/bin/env python3
"""Launch a scoped Codex session from a non-Codex agent; dry-run unless --execute."""
import argparse
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import uuid


def codex_runtime(env):
    # Recursion diagnostics, not caller authentication or a permission grant.
    return any(env.get(key) for key in ("CODEX_THREAD_ID", "CODEX_SESSION_ID", "CODEX_SANDBOX"))


def read_events(path):
    observed = {"thread_id": None, "turn_completed": False,
                "observed_model": None, "observed_effort": None,
                "usage": None, "errors": [], "invalid_json_lines": 0}
    with path.open() as stream:
        for line in stream:
            if not line.strip():
                continue
            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                observed["invalid_json_lines"] += 1
                continue
            if not isinstance(event, dict):
                observed["invalid_json_lines"] += 1
                continue
            kind = event.get("type")
            if kind == "thread.started":
                observed["thread_id"] = event.get("thread_id")
            if kind in ("thread.started", "turn.started"):
                if isinstance(event.get("model"), str):
                    observed["observed_model"] = event["model"]
                if isinstance(event.get("reasoning_effort"), str):
                    observed["observed_effort"] = event["reasoning_effort"]
            if kind == "turn.completed":
                observed["turn_completed"] = True
                observed["usage"] = event.get("usage")
            if kind in ("turn.failed", "error"):
                observed["errors"].append(event.get("error", event.get("message", "Codex error")))
    return observed


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--caller-agent", required=True)
    parser.add_argument("--cwd", required=True, type=Path)
    parser.add_argument("--role", required=True, choices=("develop", "review", "test"))
    parser.add_argument("--model", required=True)
    parser.add_argument("--effort", required=True)
    parser.add_argument("--prompt", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--resume")
    parser.add_argument("--execute", action="store_true")
    args = parser.parse_args()
    if not re.fullmatch(r"[a-z][a-z0-9-]*", args.caller_agent) or "codex" in args.caller_agent:
        parser.error("--caller-agent must identify a non-Codex agent.")
    if codex_runtime(os.environ):
        parser.error("Codex sessions must not launch this helper; do not remove runtime markers.")
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._:/\[\]-]*", args.model):
        parser.error("Provide a verified exact model ID without whitespace or shell syntax.")
    if not re.fullmatch(r"[a-z]+", args.effort):
        parser.error("Provide the requested reasoning effort supported by that model.")
    if not args.cwd.is_absolute() or not args.cwd.is_dir():
        parser.error("--cwd must be an existing absolute owned checkout directory.")
    if not args.prompt.is_absolute() or not args.prompt.is_file():
        parser.error("--prompt must be an existing absolute private text file.")
    if not args.output_dir.is_absolute():
        parser.error("--output-dir must be an absolute private untracked directory.")
    if args.resume:
        try:
            if str(uuid.UUID(args.resume)) != args.resume.lower():
                raise ValueError()
        except ValueError:
            parser.error("--resume must be the actual returned Codex thread UUID.")
    executable = shutil.which("codex")
    if not executable:
        parser.error("Codex CLI is not installed on PATH.")
    invocation_id = str(uuid.uuid4())
    run_dir = args.output_dir / invocation_id
    sandbox = "read-only" if args.role == "review" else "workspace-write"
    argv = [executable, "--ask-for-approval", "never", "--sandbox", sandbox,
            "--cd", str(args.cwd), "--config", "model_reasoning_effort=" + json.dumps(args.effort),
            "--disable", "multi_agent", "exec"]
    if args.resume:
        argv += ["resume"]
    argv += ["--model", args.model, "--json", "--output-last-message", str(run_dir / "last-message.txt")]
    if args.resume:
        argv += [args.resume]
    argv += ["-"]
    plan = {"invocation_id": invocation_id, "caller_agent": args.caller_agent,
            "role": args.role, "requested_model": args.model, "requested_effort": args.effort,
            "cwd": str(args.cwd), "resume_thread_id": args.resume, "sandbox": sandbox,
            "argv": argv, "executed": args.execute}
    if not args.execute:
        print(json.dumps(plan, ensure_ascii=False, indent=2))
        return 0
    os.umask(0o077)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    run_dir.mkdir(mode=0o700)
    (run_dir / "request.json").write_text(json.dumps(plan, ensure_ascii=False, indent=2))
    with args.prompt.open() as source, (run_dir / "events.jsonl").open("x") as events, \
            (run_dir / "stderr.log").open("x") as stderr:
        prompt = source.read()
        constraints = ("Read the supplied project instructions first. Stay in the assigned role and scope. "
                       "Do not invoke codex-sessions, start another Codex process or launch extra agents. "
                       "Do not publish, commit, push, merge, delete user data or access credentials. "
                       "Report permission denials, actual validation and remaining gaps.\n\n")
        completed = subprocess.run(argv, cwd=args.cwd, input=constraints + prompt,
                                   text=True, stdout=events, stderr=stderr, check=False)
    observed = read_events(run_dir / "events.jsonl")
    if args.resume and observed["thread_id"] and observed["thread_id"] != args.resume:
        observed["errors"].append("Resumed thread ID differs from the requested thread.")
    if observed["observed_model"] and observed["observed_model"] != args.model:
        observed["errors"].append("Observed model differs from the requested model.")
    if observed["observed_effort"] and observed["observed_effort"] != args.effort:
        observed["errors"].append("Observed effort differs from the requested effort.")
    status = completed.returncode
    if not status and (not observed["thread_id"] or not observed["turn_completed"] or observed["errors"] or observed["invalid_json_lines"]):
        status = 1
    summary = {"invocation_id": invocation_id, "cli_exit_code": completed.returncode,
               "exit_code": status, "result_dir": str(run_dir), **observed}
    (run_dir / "result.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2))
    print(json.dumps({"invocation_id": invocation_id, "thread_id": observed["thread_id"],
                      "exit_code": status, "result_dir": str(run_dir)}, ensure_ascii=False))
    return status


if __name__ == "__main__":
    raise SystemExit(main())
