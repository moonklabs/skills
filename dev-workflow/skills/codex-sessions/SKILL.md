---
name: codex-sessions
description: For non-Codex agents such as Claude to delegate development, review, and testing to actual Codex CLI sessions when the user explicitly requests Codex with a model, reasoning effort, role, or session composition. Preserve requested models and counts. Codex itself and delegated Codex sessions must not use this skill. Examples, questions, and skill edits do not launch sessions.
---

# Codex Sessions

Claude·Gemini·OpenCode 등 Codex 이외의 조정 에이전트가 사용자 요청을 실제 Codex CLI에 배정한다. 다른 모델의 하위 에이전트에 Codex 이름만 붙이지 않는다. 특정 프로젝트나 검증 언어에 종속되지 않는다.

**사용 대상:** Codex 이외의 에이전트. Codex 자신과 위임받은 Codex 세션은 이 스킬을 사용하거나 새 Codex 세션을 시작하지 않는다. 실행 에이전트가 불명확하면 실제 호출을 시작하지 않는다. helper의 자기 호출 가드를 우회하기 위해 Codex 환경 변수를 제거하지 않는다. 환경 표식과 caller 이름은 재귀 방지용이며 권한·신원 증명이 아니다.

## 1. 실행표와 현재 CLI 확인

- 사용자 요청에서 역할·정확한 model ID·reasoning effort·최초 세션 수·담당 범위를 추출한다. 명시되지 않은 값은 기존 사용자 지침에서 상속하며 모델 alias를 임의로 최신 모델로 바꾸지 않는다.
- `low~high` 개발 3세션은 `low, medium, high`, 2세션은 `low, high`, 1세션은 상한이다. 세션 내 조정을 명시했다면 그 요청을 따른다. 실제 모델이 지원하는 수준인지 먼저 확인하고 미지원 값을 다른 effort로 바꾸지 않는다.
- `command -v codex`, `codex --version`, `codex exec --help`, `codex exec resume --help`로 설치와 옵션을 확인한다. 현재 설치의 모델 목록·provider 설정·프로젝트 지침에서 model/effort를 확인하되 인증 파일과 토큰을 읽지 않는다. 도움말 확인만으로 계정 사용 가능성을 주장하지 않는다.
- 실제 호출에서 인증·모델 지원·사용량·sandbox 오류가 나면 그 원인을 보고한다. fallback 모델이나 추가 세션으로 대체하지 않는다.

## 2. 범위와 지침 전달

- 개발 작업은 파일 소유 범위를 분리한다. 독립 checkout/worktree를 우선하고 공유 파일의 쓰기는 직렬화한다. 미커밋 변경·다른 사용자의 checkout·앱·프로필을 보존한다.
- 각 프롬프트에 현재 프로젝트 지침, 목표와 Markdown 인수 ID, 역할·model·effort, 기준 소스 상태, 허용 파일·행동, 검증 명령, 확인한 사실·미확인 사항, 결과 보고 형식을 적는다.
- Codex가 프로젝트 지침을 자동으로 읽는다고 가정하지 않는다. 존재하는 AGENTS.md 등 실제 경로를 전달하고 먼저 읽게 한다.
- 추가 에이전트·다른 Codex 세션·`codex-sessions` 재호출, Git·외부 게시, 무관한 데이터·자격증명 접근을 담당 지침으로 금지한다. 제한을 우회하지 않는다.
- 인수 조건은 Markdown에 정의·보존한다. 필요할 때만 현재 목표의 임시 실행 스크립트를 작성하고 실제 통과 후 소스 상태·명령·환경·결과·미검증을 적고 스크립트를 폐기한다. 실행 스크립트 부재는 이번 실행 생략이며 저장소의 다른 필수 게이트는 유지한다.

## 3. helper 실행

[scripts/run_session.py](scripts/run_session.py)는 표준 Python만 사용하고 기본은 dry-run이다. 아래 경로를 현재 읽은 스킬의 절대 경로로 바꾼다. 프롬프트·로그는 접근 권한을 제한한 임시 위치에 저장하며 Git에 넣지 않는다.

```bash
python3 /absolute/path/to/codex-sessions/scripts/run_session.py \
  --caller-agent claude --cwd /absolute/owned/checkout --role review \
  --model EXACT_MODEL_ID --effort high \
  --prompt /absolute/private/task.txt --output-dir /absolute/private/results
# 사용자가 실제 위임을 요청한 경우에만 --execute를 추가한다.
# 수정은 --resume ACTUAL_THREAD_UUID로 동일 세션을 재개한다.
```

- 개발·테스트는 `workspace-write`, 리뷰는 `read-only` sandbox로 실행한다. approval policy는 `never`이며 sandbox 밖 작업은 승인 없이 실패한다. 이는 sandbox 우회가 아니다. 리뷰는 읽기 전용 검토, 테스트는 지정된 검증만 수행하도록 지시한다.
- Codex CLI에는 Claude helper와 동일한 도구별 shell allowlist가 없다. 명령·행동 제한은 프롬프트로 명시하고 OS sandbox·현재 실행 환경의 실제 권한을 따른다. 그런 제한이 강제된 allowlist라고 주장하지 않는다.
- helper는 정확한 모델·effort와 역할을 기록하고 multi-agent 기능을 끈다. 위험한 sandbox·approval 우회 플래그, 추가 writable directory, 임의 추가 인자·최근 세션 선택은 제공하지 않는다.
- 재개는 반환된 실제 `thread_id`의 UUID만 사용하고 같은 model·effort·role·cwd를 유지한다. `--last`와 새 세션을 추가 생성하는 방식으로 수정하지 않는다.
- 모델 요청·prompt를 셸 문자열에 삽입하지 않고 argv와 stdin으로 전달한다. 프롬프트에는 비밀·토큰·무관한 사용자 자료를 포함하지 않는다.

## 4. 통합·리뷰·검증

개발 완료를 확인하고 diff를 검토해 합친다. 요청된 리뷰는 동일 통합본을 읽되 관점을 나눈다. 리뷰 지적은 원래 개발 세션으로 전달하고 필요할 때 같은 리뷰 세션을 재개한다. 요청된 최초 세션 수를 유지하고 재귀 위임하지 않는다.

최종 통합 검증은 조정 담당 책임이다. 실제 테스트 결과·앱 실행·모델 실행·사람 확인을 구별한다. commit·push·PR·merge·배포는 별도 사용자 요청 범위에 따른다.

## 5. 증거와 종료

- helper의 `invocation_id`는 로컬 호출 식별자이고 실제 Codex 세션 ID가 아니다. `thread.started` JSON 이벤트의 실제 `thread_id`를 확인한다. 이벤트·최종 메시지·stderr와 실제 실패를 읽는다.
- 종료 코드 0만으로 작업 완료를 인정하지 않는다. `turn.completed`와 검증 근거를 확인한다. JSON 이벤트에 실제 model/effort가 없으면 `미확인`으로 보고한다. CLI 지정값을 관측값으로 바꾸지 않는다.
- 결과에는 역할·요청 model/effort·관측값·실제 thread ID·변경·검증·미검증·blocker를 요약한다. 실행 중인 요청 세션은 끝까지 추적하고 무관한 프로세스를 종료하지 않는다.

스킬을 수정할 때는 [references/acceptance.md](references/acceptance.md)의 조건으로 helper·설치 상태를 검증한다. 모델 실행 검증과 제어된 CLI 검증을 구별한다.
