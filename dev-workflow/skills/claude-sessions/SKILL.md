---
name: claude-sessions
description: For non-Claude agents to delegate development, review, and testing to Claude Code when the user explicitly requests Claude (클로드) or Sonnet/Opus (소넷/오퍼스) with a model, effort, role, or session composition. Preserve requested versions and session counts. Claude itself and delegated Claude sessions must not use this skill. Examples, questions, and skill edits do not launch sessions.
---

# Claude Sessions

Claude 이외의 조정 에이전트가 사용자가 지정한 Claude 구성을 실제 Claude Code 프로세스로 실행한다. 조정 담당은 작업 분할·통합·검증을 맡는다. Claude 이름만 붙인 다른 모델의 하위 에이전트로 대체하지 않는다. 특정 프로젝트·언어·검증 명령에 종속되지 않는다.

**사용 대상:** Codex·Gemini·OpenCode 등 Claude 이외의 에이전트. Claude 자신과 위임받은 Claude 세션은 이 스킬을 사용하거나 새 Claude 세션을 시작하지 않는다. 자신의 실행 에이전트가 불명확하면 실제 호출을 시작하지 않는다. helper의 Claude 환경 감지를 우회하기 위해 환경 변수를 제거하지 않는다.

## 1. 요청을 실행표로 변환

현재 목표와 사용자 지침에서 `역할 / 모델 원문 / 정확한 model ID / effort / 세션 수 / 담당 범위`를 추출한다. 명시된 값은 우선하고, 없는 값만 기존 세션 지침에서 상속한다. 작업·모델을 결정할 정보가 없으면 필요한 정보만 질문한다. 예시 인용은 실행 요청이 아니다.

- 역할: 개발/develop → 구현, 리뷰/review → 읽기 전용 검토, 테스트/test → 현재 목표의 인수 검증.
- 범위 effort는 세션에 순서대로 분산한다. `low~high` 3세션은 `low, medium, high`, 2세션은 `low, high`다. 다른 수는 CLI가 지원하는 범위의 수준에 균등 분산하고, 1세션은 상한을 사용한다. 이 해석을 실행표에 명시한다. 사용자가 세션 내부에서 effort를 조절하라고 지정했다면 그 지시를 따른다.
- 모델의 버전은 고정한다. `소넷 5.5` → `claude-sonnet-5-5`, `opus 5.5` → `claude-opus-5-5`는 공식 문서에서 확인한 매핑이다. 다른 버전·provider의 ID는 실행 시 공식 문서와 연결 환경에서 확인한다. 버전이 지정됐으면 최신 alias로 바꾸지 않는다.
- 요청한 최초 세션 수를 보존한다. 수정·후속 질문은 해당 세션을 재개하며 추가 세션·재귀 위임·테스트 세션을 임의 생성하지 않는다. 플랫폼 동시 실행 상한이 있으면 요청된 세션을 차례로 실행한다.

예시 요청의 실행표:

| 세션 | 역할 | model | effort |
| --- | --- | --- | --- |
| dev-1 | 개발 | claude-sonnet-5-5 | low |
| dev-2 | 개발 | claude-sonnet-5-5 | medium |
| dev-3 | 개발 | claude-sonnet-5-5 | high |
| review-1 | 리뷰 | claude-opus-5-5 | high |
| review-2 | 리뷰 | claude-opus-5-5 | high |

## 2. 실행 준비와 작업 분할

`command -v claude`, `claude --version`, `claude --help`로 설치와 옵션을 확인한다. 인증 파일을 읽지 않는다. 실제 호출에서 인증·사용량·모델 지원 오류가 나면 해당 원인을 보고하고 다른 모델로 대체하지 않는다. 설치/도움말 확인은 계정의 모델 사용 가능성을 증명하지 않는다.

개발자는 파일 소유 범위가 겹치지 않는 독립 작업을 맡긴다. 병렬 쓰기는 독립 작업용 checkout/worktree를 우선하며 현재 사용자의 미커밋 변경을 누락하거나 덮어쓰지 않는다. 공유 파일이나 순차 의존 작업은 직렬화한다. worktree 생성이 불가능하면 같은 체크아웃에서 개발 세션을 직렬 실행한다. 다른 작업의 checkout·앱·프로필·프로세스를 종료하거나 정리하지 않는다.

현재 AGENTS.md와 필요한 하위 지침을 각 세션에 전달한다. Claude가 AGENTS.md를 자동으로 읽는다고 가정하지 않는다. 작업 지침에는 다음을 포함한다:

```text
목표와 인수 기준:
요청된 역할 / model / effort / session ID:
기준 checkout·revision 및 현재 변경 상태:
담당 파일·허용된 수정 범위 / 다른 세션의 소유 범위:
적용할 AGENTS.md와 사용자 지침 원문 또는 경로(먼저 읽을 것):
검증 명령·현재 목표의 테스트 정책:
입력 맥락·이미 확인한 사실·미확인 사항:
보고: 변경 파일, 변경 이유, 검증 명령과 결과, 미검증 범위, blocker.
추가 에이전트·세션을 만들지 말 것. 범위 확장·공유 파일 충돌은 보고할 것.
```

현재 프로젝트의 지침·검증 명령·데이터 접근 범위를 전달한다. 인수 조건은 Markdown에 정의하고 자동 실행이 필요할 때만 임시 스크립트를 작성한다. 통합 담당은 실제 통과를 확인한 뒤 문서에 소스 상태·명령·환경·결과·미검증 범위를 남기고 스크립트를 폐기한다. 재검증은 문서에서 다시 구현한다. 실행 스크립트가 없으면 `이번 실행 생략`으로 기록하며 과거 통과를 현재 소스의 검증으로 승격하지 않는다. 현재 저장소의 다른 필수 게이트는 유지한다. 비밀·토큰·무관한 사용자 자료를 프롬프트에 포함하지 않는다. 변경 금지 저장소·사용자 데이터·외부 게시 범위는 작업 지침으로 명시한다.

## 3. 실제 Claude 호출

반복 실행의 인자와 출력 경로를 보존하려면 [scripts/run_session.py](scripts/run_session.py)를 사용한다. 아래 예시의 script 경로는 현재 읽은 스킬 디렉터리의 절대 경로로 바꾼다. 표준 Python만 필요하며 기본은 dry-run이다. 프롬프트는 접근 권한 0600의 임시 파일에 작성한다. 모델에 보낼 관련 소스만 포함하고 로그·프롬프트는 Git에 넣지 않는다.

```bash
python3 /absolute/path/to/claude-sessions/scripts/run_session.py \
  --caller-agent codex --cwd /absolute/owned/checkout --role develop \
  --model claude-sonnet-5-5 --effort low \
  --prompt /absolute/private/task.txt --output-dir /absolute/private/results
# 실행 요청을 받은 작업에서만 동일 인자에 --execute를 추가한다.
```

helper는 매 호출 UUID, 정확한 model/effort, 역할별 tools, JSON 출력과 stderr 파일을 관리한다. 개발은 로컬 파일 편집 모드, 리뷰는 Read/Grep/Glob만 사용한다. 테스트는 읽기와 Bash만 제공한다. 개발/테스트의 필요한 명령은 사전 검토한 `--allow-command 'npm run typecheck'`처럼 정확한 명령으로 한정한다. 광범위한 Bash 허용, `bypassPermissions`, `--dangerously-skip-permissions`를 사용하지 않는다. 도구 권한 거부를 승인으로 바꾸지 않는다.

helper는 Anthropic 형식의 정확한 model ID를 받는다. 다른 provider는 확인된 deployment ID로 같은 역할·권한·로그 계약을 따르는 직접 CLI 호출을 구성한다. 셸 문자열에 사용자 프롬프트를 삽입하지 않는다. 이후 수정에는 기록한 session ID로 `claude --resume ID -p ...`를 사용하고 동일 모델·effort·도구 제한을 유지한다. 추가 세션을 만들기 위해 helper를 다시 실행하지 않는다.

요청 범위의 로컬 작업에 기존 도구 권한을 사용할 수 있으면 진행한다. 실제 CLI 호출이 sandbox 때문에 인증/쓰기 접근에 실패하면 허용된 도구의 정상 승인 경로를 사용한다. skill은 sandbox 권한을 부여하지 않는다.

## 4. 통합·리뷰·테스트

개발 완료를 확인하고 diff를 검토해 합친다. 요청된 리뷰 세션들은 같은 통합본을 읽되 정확성·계약과 구조·유지보수처럼 관점을 나눈다. 리뷰 결과는 심각도·파일/행·근거·해결안을 포함해야 한다. 리뷰어는 파일을 수정하지 않는다.

요청된 테스트 세션은 통합본의 현재 목표 인수 기준을 검증한다. 테스트 수정이 필요하면 개발 세션에 돌려보낸다. 자동 테스트, 실제 앱, 실제 모델, 사람 확인을 구별한다. 리뷰/테스트를 별도로 요청하지 않았으면 조정 담당이 필요한 통합 검증을 수행하며 Claude 세션 수를 늘리지 않는다.

핵심 지적은 원래 개발 세션에 전달해 수정하고 필요하면 같은 리뷰 세션을 재개한다. 근거 없이 반복하지 않는다. 최종 통합 검증은 조정 담당 책임이다. commit·push·PR·merge·배포는 별도 사용자 요청 범위에 따른다.

## 5. 실행 증거와 종료

결과 JSON의 오류·실제 모델 정보(예: modelUsage)와 stderr를 확인한다. `--model`/`--effort` 지정만으로 실제 모델/effort가 검증됐다고 주장하지 않는다. 실제 값이 없으면 `미확인`이다. 모델 전환이 관측되면 요청 구성 불일치로 보고하고 해당 결과를 요청 모델의 성공으로 인정하지 않는다. 자동 fallback과 추가 workflow는 helper의 세션 설정으로 끄며, 상위 정책이 이를 강제하면 중단 원인을 보고한다.

마지막 보고는 `역할 / 요청 model·effort / 관측 model·effort / session ID / 변경·검증 / blocker`를 요약한다. 프로세스 종료코드 0만으로 테스트나 작업 완료를 인정하지 않는다. 아직 실행 중인 요청 세션이 있으면 계속 추적하고, 무관한 프로세스를 일괄 종료하지 않는다.

공식 옵션과 버전 정보는 실행 시 [Claude CLI](https://code.claude.com/docs/en/cli-reference)와 [모델·effort 설정](https://code.claude.com/docs/en/model-config)을 확인한다. 사용자 예시를 실제 실행했다고 보고하지 않는다.
