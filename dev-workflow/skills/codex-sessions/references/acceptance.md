# 사용자 공용 위임 스킬 인수 조건

조건은 Markdown으로 유지한다. 검증이 필요하면 최소 임시 실행 스크립트를 작성하며, 통과 후 환경·결과·미검증 범위를 기록하고 스크립트는 폐기한다.

| ID | Given / When | Then |
| --- | --- | --- |
| U1 | 현재 프로젝트 외의 임시 작업 디렉터리에서 두 helper를 dry-run | 지정 model·effort·role·cwd를 유지하고 실제 CLI를 호출하거나 로그 디렉터리를 만들지 않는다. |
| U2 | Claude caller/환경에서 claude helper, Codex caller/환경에서 codex helper 실행 | 실제 CLI 호출 전 거절한다. 다른 에이전트는 인자 구성이 가능하다. caller·환경 표식은 권한 증명이 아니다. |
| U3 | Codex develop/review/test 역할의 실행 계획 | develop/test는 workspace-write, review는 read-only. 위험한 우회 옵션·추가 writable directory가 없고 multi-agent 비활성이다. |
| U4 | 실제 UUID로 Codex 재개 계획 생성 | resume UUID·model·effort·역할을 보존하고 --last나 새 스레드 생성으로 대체하지 않는다. |
| U5 | 제어된 가짜 CLI가 JSON 이벤트·최종 메시지를 반환 | 실제 반환 thread ID와 종료·완료 상태를 기록하고 반환되지 않은 model/effort는 null이다. JSON 오류·turn 실패·ID/모델/effort 불일치는 성공으로 표시하지 않는다. 이 검증은 실제 모델 실행이 아니다. |
| U6 | 사용자 공용 설치 완료 | 원천은 ~/.agents/skills이며 관련 에이전트 검색 위치는 원천을 가리킨다. Claude 검색 위치에는 claude-sessions가 없고 Codex 검색 위치에는 codex-sessions가 없다. 스킬 본문도 자기 호출을 금지한다. 공용 경로를 직접 읽는 경우의 자동 발견은 해당 에이전트 동작에 따른다. |
| U7 | 프로젝트 스킬 제거 후 지침과 사용자 스킬 읽기 | 프로젝트 상대 링크·특정 프로젝트 이름·고정 실행 명령이 남지 않고 기존 프로젝트 전용 게이트는 보존된다. |

## 검증 기록

검증 소스는 사용자 공용 승격 준비본이다. Python 3의 두 helper, 설치된 Codex CLI 0.154.0의 도움말·옵션, 제어된 가짜 CLI와 JSON fixture를 사용했다. U1–U5 통과: dry-run 무실행·무로그, 자기 호출 거절, 역할별 sandbox, UUID 재개, 완료·실패·잘못된 JSON·모델/effort/ID 불일치 판정과 실제 관측 없는 model/effort의 null 처리를 확인했다. 임시 명령은 `python3 verify_helpers.py`였으며 검증 후 해당 실행 스크립트를 폐기한다.

U6–U7 통과: ~/.agents/skills의 사용자 공용 원천 4개와 Codex·Claude·Gemini·OpenCode의 심볼릭 링크를 확인했다. Claude용 경로에는 claude-sessions를, Codex용 경로에는 codex-sessions를 등록하지 않았다. 프로젝트의 이전 원천 7개는 삭제하고 AGENTS 참조를 사용자 경로로 갱신했으며 프로젝트 전용 게이트·검수 스킬은 보존했다. 설치된 helper의 Python 3.14.8 구문·dry-run·현재 Codex 환경 자기 호출 거절, 스킬 YAML·상대 참조·git diff 공백 검사를 확인했다. 실제 모델·다른 에이전트 UI의 자동 발견은 별도 실제 실행 전까지 미검증이다. caller·환경 가드는 재귀 방지 장치이며 악의적인 신원 위조를 막는 보안 경계가 아니다.

## 설치본 재검증 — 2026-10-02

설치된 사용자 공용 원천에서 구문·dry-run·자기 호출 거절·모델/effort/cwd 유지·사용자 검색 경로·프로젝트 비종속성을 직접 검사했다. Python 3.14.8, Codex CLI 0.154.0, Claude Code 2.1.287 환경이며 결과는 27개 체크 통과다. CLI 버전 확인은 실제 실행했지만 모델 위임 호출은 0회다.

- Claude helper는 현재 Codex에서 임시 cwd로 review dry-run을 실행했다. 요청 `claude-sonnet-5-5`·`low`와 cwd를 유지하며 `executed=false`, 결과 디렉터리 생성 없음이었다. 모델을 요청값대로 실제 호출했다고 주장하지 않는다.
- Claude 자기 caller 두 형식과 Claude runtime guard를 확인했다. Codex helper는 실제 현재 Codex runtime marker를 그대로 상속했으며 CLI 실행 전 자기 호출을 거절했다. 가드를 우회하거나 다른 에이전트인 척 실행하지 않았다.
- 공용 원천 네 개, 각 에이전트용 14개 심볼릭 링크, Claude/Codex의 자기 helper 등록 제외와 프로젝트 이름이 없는 본문을 확인했다. 이 검증은 다른 에이전트 UI에서의 자동 발견을 뜻하지 않는다.
- 명령은 임시 Python 검증 스크립트 실행과 두 CLI의 `--version`이다. 통과 후 해당 검증 스크립트는 폐기했다. 재검증 시 U1/U2/U6/U7에서 필요한 부분만 다시 작성한다. U3–U5의 제어된 CLI 이벤트 전체 사례는 이번에 재실행하지 않았다. 실제 모델 위임과 다른 에이전트 UI 발견은 계속 미검증이다.
