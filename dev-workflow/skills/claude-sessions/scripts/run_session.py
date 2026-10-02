#!/usr/bin/env python3
"""Launch one scoped Claude session from a non-Claude agent; dry-run unless --execute."""
import argparse
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import uuid


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--caller-agent", required=True)
    parser.add_argument("--cwd", required=True, type=Path)
    parser.add_argument("--role", required=True, choices=("develop", "review", "test"))
    parser.add_argument("--model", required=True)
    parser.add_argument("--effort", required=True,
                        choices=("low", "medium", "high", "xhigh", "max"))
    parser.add_argument("--prompt", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--allow-command", action="append", default=[])
    parser.add_argument("--execute", action="store_true")
    args = parser.parse_args()
    if not re.fullmatch(r"[a-z][a-z0-9-]*", args.caller_agent) or "claude" in args.caller_agent:
        parser.error("--caller-agent must identify a non-Claude agent.")
    # Routing/recursion guard, not proof of caller identity or a permission grant.
    if os.environ.get("CLAUDECODE") or os.environ.get("CLAUDE_CODE_ENTRYPOINT"):
        parser.error("This helper is for non-Claude agents; Claude sessions must not launch it.")
    if not re.fullmatch(r"claude-[a-z]+-\d+(?:-\d+)*(?:\[1m\])?", args.model):
        parser.error("Provide a verified exact Anthropic model ID, not an alias.")
    if not args.cwd.is_absolute() or not args.cwd.is_dir():
        parser.error("--cwd must be an existing absolute owned checkout directory.")
    if not args.prompt.is_absolute() or not args.prompt.is_file():
        parser.error("--prompt must be an existing absolute private text file.")
    if not args.output_dir.is_absolute():
        parser.error("--output-dir must be absolute and outside tracked files.")
    if args.role == "review" and args.allow_command:
        parser.error("Review sessions cannot receive shell permissions.")
    for command in args.allow_command:
        if not command.strip() or any(c in command for c in "*?[],\n\r;|&`$<>()\\"):
            parser.error("--allow-command accepts a reviewed literal command, no patterns or shell syntax.")
    executable = shutil.which("claude")
    if not executable:
        parser.error("Claude Code is not installed on PATH.")
    session_id = str(uuid.uuid4())
    tools = "Read,Grep,Glob"
    if args.role == "develop":
        tools += ",Edit,Write,Bash"
    elif args.role == "test":
        tools += ",Bash"
    settings = {"fallbackModel": [], "switchModelsOnFlag": False, "ultracode": False}
    argv = [executable, "-p", "--model", args.model, "--effort", args.effort,
            "--session-id", session_id, "--output-format", "json",
            "--tools", tools, "--disable-slash-commands", "--strict-mcp-config",
            "--mcp-config", '{"mcpServers":{}}', "--settings", json.dumps(settings),
            "--permission-mode", "acceptEdits" if args.role == "develop" else "manual",
            "--permission-prompts", "none",
            "--append-system-prompt",
            "Read the supplied project instructions first. Stay in the assigned role and file scope. "
            "Do not invoke the claude-sessions skill or start another Claude Code process. "
            "Do not launch subagents or extra sessions. Do not publish, commit, push, merge, "
            "delete user data, or access credentials. Report permission denials and validation gaps."]
    if args.allow_command:
        argv += ["--allowedTools", ",".join(f"Bash({c})" for c in args.allow_command)]
    plan = {"session_id": session_id, "caller_agent": args.caller_agent, "role": args.role, "requested_model": args.model,
            "requested_effort": args.effort, "cwd": str(args.cwd), "argv": argv,
            "executed": args.execute}
    if not args.execute:
        print(json.dumps(plan, ensure_ascii=False, indent=2))
        return 0
    # A new private directory avoids replacing logs or following existing log symlinks.
    os.umask(0o077)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    run_dir = args.output_dir / session_id
    run_dir.mkdir(mode=0o700)
    (run_dir / "request.json").write_text(json.dumps(plan, ensure_ascii=False, indent=2))
    with args.prompt.open() as prompt, (run_dir / "result.json").open("x") as result, \
            (run_dir / "stderr.log").open("x") as stderr:
        completed = subprocess.run(argv, cwd=args.cwd, stdin=prompt, stdout=result,
                                   stderr=stderr, check=False)
    print(json.dumps({"session_id": session_id, "exit_code": completed.returncode,
                      "result_dir": str(run_dir)}, ensure_ascii=False))
    return completed.returncode


if __name__ == "__main__":
    raise SystemExit(main())
