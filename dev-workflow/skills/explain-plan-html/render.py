#!/usr/bin/env python3
"""render.py — 플랜(작업 계획) 마크다운 + DSL 문서를 자기 완결형 HTML 해설서로 렌더링한다.

explain-diff-html 의 렌더러에서 파생했으며, 플랜 파일에 특화된 지시자
5종(timeline / deps / files / checklist / decision)을 추가로 지원한다.
플랜 파일의 공통 골격 — Context, 핵심 결정, Phase별 실행 계획(공수·게이트),
태스크 의존 관계(blocked-by), 파일 배치, 검증 — 을 각각 전용 시각 요소로 옮긴다.

사용법
------
    python render.py plan-doc.md [-o out.html] [--repo PATH] [--plan PATH] [--open]

-o 생략 시 /tmp/YYYY-MM-DD-plan-<slug>.html 로 저장하고 경로를 stdout 에 출력한다.

원문 패널 (plan: / src: 링크)
-----------------------------
frontmatter `plan:` (또는 --plan) 에 플랜 원문 md 경로를 주면, 원문 전체가 렌더된
HTML 로 드로어(우측 슬라이드 패널)에 내장된다 — 우하단 "플랜 원문" 버튼으로 연다.
본문에서 `[표시 텍스트](src:원문-제목-일부)` 링크를 쓰면 클릭 시 드로어가 열리며
해당 원문 제목으로 스크롤 + 하이라이트된다. 검색어는 공백 대신 하이픈을 쓰고
(매칭 시 공백·하이픈·장식 무시), 원문 제목과 매칭되지 않으면 렌더가 실패한다.

입력 형식
---------
YAML 유사 frontmatter + 마크다운 본문 + 펜스 지시자(fenced directive).

    ---
    title: 문서 제목
    subtitle: 한 문단짜리 리드
    kicker: 상단 라벨
    slug: url-slug
    repo: /path/to/repo          # gitdiff/snippet 지시자가 쓸 저장소
    meta:
      - 2026-07-21
      - "브랜치 `feature/x`"
    ---

    ## 배경 {#bg}

    본문은 **마크다운**이다. `인라인 코드`, [링크](url), 목록, 파이프 표를 지원한다.

    ### 소제목

`##` 은 섹션(자동으로 "Part N" 번호와 목차 항목이 붙는다), `###` 은 하위 목차 항목이 된다.
`{#id}` 로 앵커를 명시할 수 있고, 생략하면 s1 / s1-2 처럼 자동 부여된다.

지원 지시자 (펜스 블록)
-----------------------
모든 지시자는 마지막에 `:: 캡션` 줄을 둘 수 있다(선택).
스타일 토큰: hi(강조) ok(성공) no(실패) wa(주의).

  flow — 가로 흐름 다이어그램. 한 줄 = 박스 하나, 사이에 화살표가 자동 삽입된다.
    ```flow 피드의 기본 구조
    앱 (v0.2.0) | 4시간마다 체크 | hi
    GET beta.yml | 피드에서 매니페스트
    :: 앱은 매니페스트 하나만 읽으면 된다.
    ```

  stack — 세로 단계 나열. 한 줄 = 한 행이고 ` > ` 로 나눈 조각이 알약(pill)이 된다.
    ```stack 지시대로 세 곳을 바꿨을 때
    UPDATE_FEED_URL = 실 URL > PLACEHOLDER = 실 URL
    판정이 항상 true [no]
    ```

  uiwin — 앱 창 목업. `win:` 으로 창을 여러 개 두면 자동으로 나란히 배치된다.
    ```uiwin 변경 전후
    win: ① 다운로드 완료
    banner: 새 버전 준비됐어요. | btn: 지금 재시작
    stub
    win: ② 수집 중 클릭
    banner.mute: 수집이 끝나면 재시작할 수 있어요. | btn.gone: 지금 재시작
    ```

  gitdiff — git 에서 diff 를 직접 뽑는다. 손으로 옮겨 적지 않으므로 원본과 어긋날 수 없다.
    ```gitdiff desktop/src/main.ts
    rev: 25c7a47..HEAD
    grep: updaterHandle        # 이 문자열을 포함한 hunk 만
    context: 3
    ```

  snippet — 파일 일부를 그대로 인용한다.
    ```snippet desktop/src/updater.ts:55-60
    rev: HEAD                  # 생략 시 워킹트리
    ```

  code — git 에 없는 코드/설정을 직접 쓸 때.
    ```code ts 예시
    const x = 1;
    ```

  callout — 핵심 개념·엣지 케이스 강조. 종류: info(기본) warn bad good.
    ```callout warn 놓치기 쉬운 곳
    입력 기본값만 바꾸면 부족하다. **두 곳**을 함께 바꿔야 한다.
    ```

  quiz — 대화형 객관식. `*` 가 정답, `>` 가 해설, `---` 가 문제 구분자.
    ```quiz
    Q: 센티널을 실 호스트로 바꾸면?
    - 정상 발효된다
    * 판정이 항상 true 가 되어 영구 비활성된다
    > url.includes(HOST) 이므로 실 URL 이 자기 자신을 포함하게 된다.
    ---
    Q: 다음 문제
    ...
    ```
    보기 순서는 렌더링 시점에 섞이므로 자연스러운 순서로 쓰면 된다.

  html — 위 지시자로 표현할 수 없을 때의 탈출구. 원시 HTML 을 그대로 통과시킨다.

플랜 전용 지시자
---------------
  timeline — Phase 로드맵. `배지 | 제목 | 공수·게이트 조건 | 상태` (상태: done/now/gate, 생략 가능).
    ```timeline 실행 로드맵
    P0 | 백엔드 착지 | 0.5일 | done
    P1 | Skill+Command 도그푸딩 | 1일 | now
    P2 | 배포 패키징 | 1~2일
    P3 | Hook 강제 | 게이트: H-도장 확증 후 | gate
    ```

  deps — 태스크/이슈 의존 그래프. `id: 라벨 <- 선행id들`. 위상 정렬로 층을 자동 배치한다.
    ```deps 이슈 의존 관계
    i1: main 핫픽스 3커밋 반영 [hi]
    i2: GROWTH/AD 원천 차단 <- i1
    i3: coupangAdETL 확장 <- i1
    i5: 레거시 축소 검토 <- i2 i3
    ```

  files — 파일 배치 맵. 접두어: `+` 신규, `~` 수정, `-` 삭제, `?` 미정.
    ```files Phase 1 파일 배치
    + .claude/skills/sprintable-loop/SKILL.md | 루프 규범 (~150줄)
    ~ packages/cli/src/commands/connect.ts | 플러그인 설치 추가
    ```

  checklist — 인터랙티브 검증 체크리스트. 체크 상태가 localStorage 에 저장되어
    브라우저를 다시 열어도 유지된다. 진행률 바 자동 표시.
    ```checklist 검증 체크리스트
    - [ ] advisor 테스트 10파일 통과
    - [x] provenance zero-collision 확인
    ```

  decision — 결정 카드. pick(선택) / why(근거) / drop(기각안) / hold(보류) 필드.
    ```decision Command인가 Skill인가?
    pick: 셋 다 쓰되 역할 분담 — Skill=자동 규범, Command=수동 진입, Hook=후행
    why: 개발자는 MCP 툴을 직접 호출하지 않는다. 에이전트가 호출하고 스킬이 시점을 가르친다.
    drop: Hook 선행 도입 — 가설 확증 전에 강제부터 넣지 않는다
    ```

설계 원칙: 이 스크립트는 순수 템플릿 렌더러다. "무엇을 설명할지, 어떤 다이어그램을 그릴지"
같은 저술 판단은 전부 작성자(LLM)의 몫으로 남고, 스크립트는 반복 작업만 제거한다.
"""
from __future__ import annotations

import argparse
import datetime
import html as html_mod
import random
import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

# --------------------------------------------------------------------------
# 프레젠테이션 상수 — 문서마다 바뀌지 않는 부분 전량
# --------------------------------------------------------------------------

CSS = r"""
:root{
  --ink:#1b1a17; --ink-soft:#4a4740; --ink-faint:#7d7970;
  --paper:#fbfaf7; --paper-2:#f3f1eb; --rule:#e2ded4;
  --accent:#8a5a2b; --accent-soft:#f0e5d6;
  --good:#2e6b45; --good-soft:#e3f0e7;
  --bad:#9a3131; --bad-soft:#f7e4e2;
  --warn:#8a6a12; --warn-soft:#f7efd8;
  --code-bg:#f5f3ee;
  --mono: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace;
  --serif: "Iowan Old Style", "Palatino Linotype", Palatino, Georgia, "Nanum Myeongjo", serif;
  --sans: -apple-system, BlinkMacSystemFont, "Segoe UI", "Apple SD Gothic Neo", "Noto Sans KR", sans-serif;
}
@media (prefers-color-scheme: dark){
  :root{
    --ink:#e8e5de; --ink-soft:#b5b1a7; --ink-faint:#8b877e;
    --paper:#161513; --paper-2:#1f1d1a; --rule:#332f2a;
    --accent:#d9a066; --accent-soft:#2e2519;
    --good:#7fc79b; --good-soft:#1a2a20;
    --bad:#e58c85; --bad-soft:#2c1c1a;
    --warn:#d9bd6a; --warn-soft:#2a2417;
    --code-bg:#1c1a17;
  }
}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0; background:var(--paper); color:var(--ink);
  font-family:var(--serif); font-size:18px; line-height:1.72}
.wrap{max-width:1180px; margin:0 auto; padding:0 20px; display:block}
@media (min-width:1060px){
  .wrap{display:grid; grid-template-columns:232px minmax(0,1fr); gap:52px; align-items:start}
}
header.mast{border-bottom:1px solid var(--rule); background:var(--paper-2)}
.mast-in{max-width:1180px;margin:0 auto;padding:44px 20px 34px}
.kicker{font-family:var(--sans); font-size:12px; letter-spacing:.16em; text-transform:uppercase;
  color:var(--accent); font-weight:650; margin:0 0 12px}
h1{font-size:clamp(28px,4.6vw,42px); line-height:1.22; margin:0 0 14px; font-weight:600; letter-spacing:-.015em}
.standfirst{margin:0; color:var(--ink-soft); font-size:clamp(17px,2.1vw,20px); max-width:64ch}
.meta{font-family:var(--sans); font-size:13px; color:var(--ink-faint); margin-top:20px;
  display:flex; flex-wrap:wrap; gap:8px 18px}
.meta code{font-family:var(--mono); font-size:12px}
nav.toc{font-family:var(--sans); font-size:13.5px; line-height:1.6; padding:28px 0}
@media (min-width:1060px){ nav.toc{position:sticky; top:0; max-height:100vh; overflow:auto; padding:40px 0} }
nav.toc h2{font-family:var(--sans); font-size:11px; letter-spacing:.14em; text-transform:uppercase;
  color:var(--ink-faint); margin:0 0 12px; font-weight:650}
nav.toc ol{list-style:none; margin:0; padding:0}
nav.toc > ol > li{margin:0 0 4px}
nav.toc ol ol{padding-left:12px; margin:3px 0 8px; border-left:1px solid var(--rule)}
nav.toc a{display:block; padding:3px 8px; color:var(--ink-soft); text-decoration:none; border-radius:5px}
nav.toc a:hover{background:var(--paper-2); color:var(--ink)}
nav.toc a.on{color:var(--accent); background:var(--accent-soft); font-weight:600}
nav.toc ol ol a{font-size:12.8px; color:var(--ink-faint)}
article{padding:28px 0 90px; min-width:0}
article > section{scroll-margin-top:20px}
h2.sec{font-size:clamp(23px,3vw,30px); margin:56px 0 6px; font-weight:600; letter-spacing:-.01em;
  padding-top:22px; border-top:1px solid var(--rule)}
section:first-of-type h2.sec{margin-top:8px; border-top:0; padding-top:0}
h2.sec .num{color:var(--accent); font-family:var(--sans); font-size:.62em; font-weight:650;
  display:block; letter-spacing:.1em; text-transform:uppercase; margin-bottom:6px}
h3{font-size:20px; margin:38px 0 8px; font-weight:600; letter-spacing:-.005em; scroll-margin-top:20px}
h4{font-family:var(--sans); font-size:14.5px; margin:26px 0 6px; font-weight:650; color:var(--ink-soft)}
p{margin:0 0 17px; max-width:70ch}
ul,ol.md{max-width:70ch; padding-left:1.3em; margin:0 0 17px}
li{margin:0 0 7px}
strong{font-weight:650}
em{font-style:italic; color:var(--ink-soft)}
a{color:var(--accent)}
code{font-family:var(--mono); font-size:.855em; background:var(--code-bg); padding:.12em .38em;
  border-radius:4px; border:1px solid var(--rule); word-break:break-word}
.lede{font-size:1.06em; color:var(--ink-soft)}
hr.soft{border:0; border-top:1px solid var(--rule); margin:34px 0}
pre{background:var(--code-bg); border:1px solid var(--rule); border-radius:9px;
  padding:15px 17px; overflow-x:auto; margin:0 0 20px;
  font-family:var(--mono); font-size:13px; line-height:1.62; white-space:pre; tab-size:2}
pre code{background:none; border:0; padding:0; font-size:inherit; white-space:pre}
pre.wrap-code, pre.wrap-code code{white-space:pre-wrap; word-break:break-word}
.codecap{font-family:var(--sans); font-size:12px; color:var(--ink-faint); margin:-12px 0 20px; padding-left:3px}
.tok-c{color:var(--ink-faint); font-style:italic}
.tok-s{color:var(--good)}
.tok-k{color:var(--accent); font-weight:600}
.tok-n{color:var(--bad)}
.tok-y{color:var(--accent)}
.dl{display:block}
.d-add{background:var(--good-soft); color:var(--good)}
.d-del{background:var(--bad-soft); color:var(--bad)}
.d-hunk{color:var(--ink-faint); font-weight:600}
.d-meta{color:var(--ink-faint)}
.call{border-left:3px solid var(--accent); background:var(--accent-soft); padding:14px 18px;
  border-radius:0 8px 8px 0; margin:0 0 22px; max-width:70ch}
.call.warnc{border-color:var(--warn); background:var(--warn-soft)}
.call.badc{border-color:var(--bad); background:var(--bad-soft)}
.call.goodc{border-color:var(--good); background:var(--good-soft)}
.call .tag{font-family:var(--sans); font-size:11px; letter-spacing:.13em; text-transform:uppercase;
  font-weight:700; color:var(--accent); display:block; margin-bottom:6px}
.call.warnc .tag{color:var(--warn)} .call.badc .tag{color:var(--bad)} .call.goodc .tag{color:var(--good)}
.call p:last-child{margin-bottom:0}
.call p{font-size:.95em}
.fig{margin:0 0 26px; padding:20px 18px; background:var(--paper-2); border:1px solid var(--rule);
  border-radius:11px; overflow-x:auto}
.fig .cap{font-family:var(--sans); font-size:12.5px; color:var(--ink-faint); margin-top:14px;
  padding-top:11px; border-top:1px solid var(--rule); line-height:1.55}
.flow{display:flex; align-items:stretch; gap:9px; flex-wrap:wrap}
.dbox{flex:1 1 130px; min-width:118px; background:var(--paper); border:1px solid var(--rule);
  border-radius:8px; padding:11px 12px; font-family:var(--sans); font-size:12.5px; line-height:1.45}
.dbox .t{font-weight:650; font-size:13px; display:block; margin-bottom:3px}
.dbox .d{color:var(--ink-faint); font-size:11.5px; display:block}
.dbox.ok{border-color:var(--good); background:var(--good-soft)}
.dbox.no{border-color:var(--bad); background:var(--bad-soft)}
.dbox.hi{border-color:var(--accent); background:var(--accent-soft)}
.dbox.wa{border-color:var(--warn); background:var(--warn-soft)}
.arrow{align-self:center; color:var(--ink-faint); font-family:var(--sans); font-size:17px; flex:0 0 auto}
.dstack{display:flex; flex-direction:column; gap:8px}
.row{display:flex; gap:9px; align-items:center; flex-wrap:wrap}
.pill{font-family:var(--sans); font-size:11.5px; padding:3px 9px; border-radius:20px;
  border:1px solid var(--rule); background:var(--paper); color:var(--ink-soft)}
.pill.ok{border-color:var(--good); color:var(--good); background:var(--good-soft)}
.pill.no{border-color:var(--bad); color:var(--bad); background:var(--bad-soft)}
.pill.wa{border-color:var(--warn); color:var(--warn); background:var(--warn-soft)}
.pill.hi{border-color:var(--accent); color:var(--accent); background:var(--accent-soft)}
.lbl{font-family:var(--sans); font-size:11px; letter-spacing:.1em; text-transform:uppercase;
  color:var(--ink-faint); font-weight:650; margin:2px 0 7px}
.wins{display:grid; grid-template-columns:1fr; gap:14px}
@media (min-width:660px){ .wins.n2{grid-template-columns:1fr 1fr} }
.uiwin{border:1px solid var(--rule); border-radius:9px; overflow:hidden; background:var(--paper);
  max-width:430px; font-family:var(--sans)}
.uibar{background:var(--paper-2); padding:7px 11px; display:flex; gap:5px; align-items:center;
  border-bottom:1px solid var(--rule)}
.uidot{width:9px;height:9px;border-radius:50%;background:var(--rule)}
.uibar .ttl{font-size:11.5px; color:var(--ink-faint); margin-left:7px}
.uibody{padding:13px}
.uibanner{display:flex; align-items:center; gap:10px; flex-wrap:wrap; padding:9px 11px;
  border:1px solid var(--accent); background:var(--accent-soft); border-radius:7px; font-size:12.5px}
.uibanner.mute{border-color:var(--rule); background:var(--paper-2); color:var(--ink-faint)}
.uibtn{font-size:11.5px; padding:4px 11px; border-radius:6px; border:1px solid var(--accent);
  background:var(--accent); color:var(--paper); font-weight:600; white-space:nowrap}
.uibtn.ghost{background:transparent; color:var(--accent)}
.uibtn.gone{opacity:.28; text-decoration:line-through}
.uistub{height:7px; background:var(--rule); border-radius:4px; margin:9px 0; opacity:.5; width:78%}
.uistub.s{width:55%}
.tbl{width:100%; border-collapse:collapse; font-family:var(--sans); font-size:13.5px; margin:0 0 22px}
.tbl th,.tbl td{text-align:left; padding:9px 11px; border-bottom:1px solid var(--rule); vertical-align:top}
.tbl th{font-size:11.5px; letter-spacing:.08em; text-transform:uppercase; color:var(--ink-faint); font-weight:650}
.tbl td.r,.tbl th.r{text-align:right}
.tbl code{font-size:12px}
.quiz{border:1px solid var(--rule); border-radius:11px; padding:20px 19px; margin:0 0 20px; background:var(--paper-2)}
.quiz .qn{font-family:var(--sans); font-size:11px; letter-spacing:.13em; text-transform:uppercase;
  color:var(--accent); font-weight:700; margin-bottom:7px}
.quiz .qt{font-weight:600; margin:0 0 15px; font-size:17px; line-height:1.55}
.opts{display:flex; flex-direction:column; gap:8px}
.opt{display:flex; gap:10px; align-items:flex-start; text-align:left; width:100%;
  font-family:var(--sans); font-size:14px; line-height:1.5; padding:11px 13px; cursor:pointer;
  background:var(--paper); border:1px solid var(--rule); border-radius:8px; color:var(--ink);
  transition:border-color .12s, background .12s}
.opt:hover:not(.locked){border-color:var(--accent)}
.opt .mk{flex:0 0 auto; width:21px; height:21px; border-radius:50%; border:1.5px solid var(--rule);
  display:flex; align-items:center; justify-content:center; font-size:11.5px; font-weight:700; color:var(--ink-faint)}
.opt.correct{border-color:var(--good); background:var(--good-soft)}
.opt.correct .mk{border-color:var(--good); color:var(--good)}
.opt.wrong{border-color:var(--bad); background:var(--bad-soft)}
.opt.wrong .mk{border-color:var(--bad); color:var(--bad)}
.opt.locked{cursor:default}
.fb{margin-top:13px; padding:12px 14px; border-radius:8px; font-family:var(--sans);
  font-size:13.5px; line-height:1.6; display:none}
.fb.show{display:block}
.fb.y{background:var(--good-soft); border-left:3px solid var(--good)}
.fb.n{background:var(--bad-soft); border-left:3px solid var(--bad)}
.fb b{font-weight:700}
.score{font-family:var(--sans); font-size:14.5px; padding:15px 18px; border-radius:10px;
  background:var(--accent-soft); border:1px solid var(--accent); text-align:center; font-weight:600}
footer.end{border-top:1px solid var(--rule); margin-top:60px; padding:26px 0 0;
  font-family:var(--sans); font-size:13px; color:var(--ink-faint)}
/* ---- 플랜 전용 컴포넌트 ---- */
.tline{display:flex; flex-direction:column}
.tl{display:flex; gap:14px; position:relative; padding:0 0 20px}
.tl:before{content:""; position:absolute; left:16px; top:34px; bottom:2px; width:2px; background:var(--rule)}
.tl:last-child{padding-bottom:2px}
.tl:last-child:before{display:none}
.tl-dot{flex:0 0 34px; width:34px; height:34px; border-radius:50%; background:var(--paper);
  border:2px solid var(--rule); display:flex; align-items:center; justify-content:center;
  font-family:var(--sans); font-size:11px; font-weight:700; color:var(--ink-faint); z-index:1}
.tl.done .tl-dot{border-color:var(--good); color:var(--good); background:var(--good-soft)}
.tl.now .tl-dot{border-color:var(--accent); color:var(--accent); background:var(--accent-soft)}
.tl.gate .tl-dot{border-color:var(--warn); color:var(--warn); background:var(--warn-soft)}
.tl-body{flex:1; min-width:0; font-family:var(--sans); padding-top:3px}
.tl-head{display:flex; align-items:center; gap:10px; flex-wrap:wrap}
.tl-t{font-weight:650; font-size:14.5px}
.tl.now .tl-t{color:var(--accent)}
.tl-d{color:var(--ink-faint); font-size:12.5px; margin-top:3px; line-height:1.55}
.deps{display:flex; flex-direction:column; gap:6px}
.dep-layer{display:flex; gap:9px; flex-wrap:wrap}
.dep-join{color:var(--ink-faint); font-family:var(--sans); font-size:15px; padding-left:14px}
.dbox .dep-from{color:var(--ink-faint); font-size:11px; display:block; margin-top:4px;
  font-family:var(--mono)}
.fmap{width:100%; border-collapse:collapse; font-family:var(--sans); font-size:13px; margin:0}
.fmap td{padding:7px 10px 7px 0; border-bottom:1px solid var(--rule); vertical-align:top}
.fmap tr:last-child td{border-bottom:0}
.fmap .fpath{font-family:var(--mono); font-size:12.5px; word-break:break-all}
.fmap .fnote{color:var(--ink-faint)}
.fbadge{display:inline-block; font-size:10.5px; font-weight:700; letter-spacing:.08em;
  padding:2px 8px; border-radius:20px; border:1px solid var(--rule); white-space:nowrap}
.fbadge.add{color:var(--good); border-color:var(--good); background:var(--good-soft)}
.fbadge.mod{color:var(--accent); border-color:var(--accent); background:var(--accent-soft)}
.fbadge.del{color:var(--bad); border-color:var(--bad); background:var(--bad-soft)}
.fbadge.tbd{color:var(--warn); border-color:var(--warn); background:var(--warn-soft)}
.ck{border:1px solid var(--rule); border-radius:11px; background:var(--paper-2);
  padding:18px 19px; margin:0 0 22px; font-family:var(--sans)}
.ck .lbl{margin-bottom:10px}
.ckbar{height:7px; border-radius:5px; background:var(--rule); overflow:hidden; margin:0 0 6px}
.ckbar i{display:block; height:100%; width:0; background:var(--good); border-radius:5px;
  transition:width .25s}
.ckpct{font-size:12px; color:var(--ink-faint); margin:0 0 13px}
.ckitem{display:flex; gap:10px; align-items:flex-start; padding:8px 10px; border-radius:8px;
  font-size:14px; line-height:1.55; cursor:pointer}
.ckitem:hover{background:var(--paper)}
.ckitem input{margin-top:4px; accent-color:var(--good); width:15px; height:15px; flex:0 0 auto; cursor:pointer}
.ckitem.on span{color:var(--ink-faint); text-decoration:line-through}
.dec{border:1px solid var(--accent); border-radius:11px; background:var(--paper);
  padding:18px 20px; margin:0 0 22px; font-family:var(--sans); max-width:70ch}
.dec .tag{font-size:11px; letter-spacing:.13em; text-transform:uppercase; font-weight:700;
  color:var(--accent); display:block; margin-bottom:6px}
.dec .dt{font-size:16.5px; font-weight:650; margin:0 0 10px; font-family:var(--serif)}
.dec .pick{font-size:14px; padding:10px 13px; border-radius:8px; background:var(--accent-soft);
  border-left:3px solid var(--accent); margin:0 0 10px; line-height:1.6}
.dec .why{font-size:13.5px; color:var(--ink-soft); margin:0 0 10px; line-height:1.6}
.dec ul.alt{list-style:none; padding:0; margin:0; font-size:13px}
.dec ul.alt li{margin:0 0 5px; padding-left:20px; position:relative; line-height:1.55}
.dec ul.alt li.drop{color:var(--ink-faint)}
.dec ul.alt li.drop:before{content:"✕"; position:absolute; left:0; color:var(--bad)}
.dec ul.alt li.drop .altbody{text-decoration:line-through}
.dec ul.alt li.hold{color:var(--ink-soft)}
.dec ul.alt li.hold:before{content:"…"; position:absolute; left:0; color:var(--warn); font-weight:700}
/* ---- 원문 패널(드로어) ---- */
a.srclink{color:var(--accent); text-decoration:none; border-bottom:1px dashed var(--accent);
  cursor:pointer}
a.srclink:after{content:" ↗"; font-size:.8em}
.srcback{position:fixed; inset:0; background:rgba(0,0,0,.35); opacity:0; pointer-events:none;
  transition:opacity .2s; z-index:40}
.srcback.show{opacity:1; pointer-events:auto}
.srcpanel{position:fixed; top:0; right:0; bottom:0; width:min(680px,94vw); z-index:41;
  background:var(--paper); border-left:1px solid var(--rule); display:flex; flex-direction:column;
  transform:translateX(102%); transition:transform .22s ease; box-shadow:-12px 0 40px rgba(0,0,0,.18)}
.srcpanel.show{transform:translateX(0)}
.srchead{display:flex; align-items:center; gap:12px; padding:14px 18px;
  border-bottom:1px solid var(--rule); background:var(--paper-2); font-family:var(--sans)}
.srchead .tag{font-size:11px; letter-spacing:.13em; text-transform:uppercase; font-weight:700;
  color:var(--accent)}
.srcname{font-family:var(--mono); font-size:12.5px; color:var(--ink-soft); flex:1; min-width:0;
  overflow:hidden; text-overflow:ellipsis; white-space:nowrap}
.srcclose{font-family:var(--sans); font-size:12.5px; border:1px solid var(--rule); background:var(--paper);
  color:var(--ink-soft); border-radius:7px; padding:5px 12px; cursor:pointer}
.srcclose:hover{border-color:var(--accent); color:var(--accent)}
.srcbody{flex:1; overflow-y:auto; padding:22px 26px 60px; font-size:15.5px; line-height:1.7}
.srcbody h2{font-size:22px; margin:8px 0 12px; font-weight:650}
.srcbody h3{font-size:18px; margin:30px 0 8px}
.srcbody h4,.srcbody h5{font-family:var(--sans); font-size:14px; margin:22px 0 6px; font-weight:650;
  color:var(--ink-soft)}
.srcbody .srch{scroll-margin-top:14px}
.srcbody pre{font-size:12px}
.srcbody p,.srcbody ul,.srcbody ol.md{max-width:none}
@keyframes srcflash{0%{background:var(--accent-soft)} 100%{background:transparent}}
.srcbody .srch.flash{animation:srcflash 1.6s ease-out}
.srchbtn{font-family:var(--sans); font-size:12.5px; font-weight:650; padding:6px 14px;
  border-radius:20px; cursor:pointer; border:1px solid var(--accent); background:var(--accent-soft);
  color:var(--accent); white-space:nowrap}
.srchbtn:hover{background:var(--accent); color:var(--paper)}
.srcfab{position:fixed; right:18px; bottom:18px; z-index:39; font-family:var(--sans);
  font-size:13px; font-weight:650; padding:10px 16px; border-radius:24px; cursor:pointer;
  border:1px solid var(--accent); background:var(--accent); color:var(--paper);
  box-shadow:0 4px 16px rgba(0,0,0,.22)}
.srcfab:hover{filter:brightness(1.08)}
@media print{.srcfab,.srcback,.srcpanel{display:none}}
"""

JS = r"""
(function(){
  "use strict";
  function esc(s){return s.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;");}
  var TS_KW="const|let|var|function|return|if|else|for|of|in|new|class|interface|type|export|import|from|async|await|try|catch|finally|throw|typeof|void|null|undefined|true|false|this|extends|implements|readonly|private|public|static|def|self|import|elif|not|and|or|None|True|False";
  function hlTs(src){
    var re=new RegExp("(\\/\\/[^\\n]*|#[^\\n]*|\\/\\*[\\s\\S]*?\\*\\/)"+
      "|('(?:[^'\\\\]|\\\\.)*'|\"(?:[^\"\\\\]|\\\\.)*\"|`(?:[^`\\\\]|\\\\.)*`)"+
      "|\\b("+TS_KW+")\\b|\\b(\\d[\\d_]*(?:\\.\\d+)?)\\b","g");
    var out="",last=0,m;
    while((m=re.exec(src))!==null){
      out+=esc(src.slice(last,m.index));
      if(m[1])out+='<span class="tok-c">'+esc(m[1])+"</span>";
      else if(m[2])out+='<span class="tok-s">'+esc(m[2])+"</span>";
      else if(m[3])out+='<span class="tok-k">'+esc(m[3])+"</span>";
      else if(m[4])out+='<span class="tok-n">'+esc(m[4])+"</span>";
      last=re.lastIndex; if(m[0]==="")re.lastIndex++;
    }
    return out+esc(src.slice(last));
  }
  function hlYaml(src){
    return src.split("\n").map(function(line){
      var cm=line.match(/^(\s*)(#.*)$/);
      if(cm)return esc(cm[1])+'<span class="tok-c">'+esc(cm[2])+"</span>";
      var out=line,trailing="";
      var tc=out.match(/\s#(?!\{).*$/);
      if(tc){trailing='<span class="tok-c">'+esc(tc[0])+"</span>";out=out.slice(0,tc.index);}
      var km=out.match(/^(\s*-?\s*)([A-Za-z0-9_.\-]+)(:)(.*)$/);
      if(km){
        var v=km[4];
        var vh=/^\s*['"]/.test(v)?'<span class="tok-s">'+esc(v)+"</span>":esc(v);
        return esc(km[1])+'<span class="tok-y">'+esc(km[2])+"</span>"+esc(km[3])+vh+trailing;
      }
      return esc(out)+trailing;
    }).join("\n");
  }
  function hlDiff(src){
    return src.split("\n").map(function(l){
      var c="";
      if(/^(diff |index |--- |\+\+\+ )/.test(l))c="d-meta";
      else if(/^@@/.test(l))c="d-hunk";
      else if(/^\+/.test(l))c="d-add";
      else if(/^-/.test(l))c="d-del";
      return '<span class="dl '+c+'">'+esc(l===""?" ":l)+"</span>";
    }).join("");
  }
  document.querySelectorAll("pre code[data-lang]").forEach(function(el){
    var lang=el.getAttribute("data-lang"),raw=el.textContent;
    if(lang==="diff")el.innerHTML=hlDiff(raw);
    else if(lang==="yaml"||lang==="yml")el.innerHTML=hlYaml(raw);
    else if(lang==="text")el.innerHTML=esc(raw);
    else el.innerHTML=hlTs(raw);
  });

  var QUESTIONS=window.__QUIZ__||[];
  var answered=0,correct=0;
  var root=document.getElementById("quizroot"),scoreEl=document.getElementById("score");
  if(root)QUESTIONS.forEach(function(item,qi){
    var box=document.createElement("div");box.className="quiz";
    var num=document.createElement("div");num.className="qn";
    num.textContent="질문 "+(qi+1)+" / "+QUESTIONS.length;box.appendChild(num);
    var qt=document.createElement("p");qt.className="qt";qt.innerHTML=item.q;box.appendChild(qt);
    var opts=document.createElement("div");opts.className="opts";
    var fb=document.createElement("div");fb.className="fb";
    var done=false;
    item.opts.forEach(function(text,oi){
      var b=document.createElement("button");b.type="button";b.className="opt";
      var mk=document.createElement("span");mk.className="mk";
      mk.textContent=String.fromCharCode(65+oi);
      var sp=document.createElement("span");sp.innerHTML=text;
      b.appendChild(mk);b.appendChild(sp);
      b.addEventListener("click",function(){
        if(done)return; done=true;
        var ok=(oi===item.a); answered++; if(ok)correct++;
        Array.prototype.forEach.call(opts.children,function(ch,ci){
          ch.classList.add("locked");
          if(ci===item.a){ch.classList.add("correct");ch.querySelector(".mk").textContent="✓";}
          else if(ci===oi){ch.classList.add("wrong");ch.querySelector(".mk").textContent="✕";}
        });
        fb.className="fb show "+(ok?"y":"n");
        fb.innerHTML="<b>"+(ok?"정답입니다.":"아쉽네요 — 정답은 "+String.fromCharCode(65+item.a)+"입니다.")+"</b> "+item.why;
        if(scoreEl)scoreEl.textContent=QUESTIONS.length+"문제 중 "+answered+"문제 완료 · "+correct+"개 정답"+
          (answered===QUESTIONS.length?(correct===QUESTIONS.length?" — 완벽합니다!":" — 틀린 문제의 해설을 다시 읽어보세요."):"");
      });
      opts.appendChild(b);
    });
    box.appendChild(opts);box.appendChild(fb);root.appendChild(box);
  });

  var panel=document.getElementById("srcpanel"),back=document.getElementById("srcback"),
      fab=document.getElementById("srcfab");
  function srcOpen(target){
    if(!panel)return;
    panel.classList.add("show"); back.classList.add("show");
    if(target){
      var el=document.getElementById(target);
      if(el){
        el.classList.remove("flash");
        setTimeout(function(){ el.scrollIntoView({block:"start"}); el.classList.add("flash"); },230);
      }
    }
  }
  function srcClose(){
    if(!panel)return;
    panel.classList.remove("show"); back.classList.remove("show");
  }
  if(fab)fab.addEventListener("click",function(){srcOpen();});
  var hbtn=document.getElementById("srchbtn");
  if(hbtn)hbtn.addEventListener("click",function(){srcOpen();});
  if(back)back.addEventListener("click",srcClose);
  var closeBtn=document.getElementById("srcclose");
  if(closeBtn)closeBtn.addEventListener("click",srcClose);
  document.addEventListener("keydown",function(e){if(e.key==="Escape")srcClose();});
  document.querySelectorAll("a.srclink").forEach(function(a){
    a.addEventListener("click",function(e){
      e.preventDefault();
      srcOpen(a.getAttribute("data-src"));
    });
  });

  var DOC=window.__DOC__||"plan";
  document.querySelectorAll(".ck").forEach(function(ck){
    var key="skplan:"+DOC+":"+ck.getAttribute("data-ck");
    var saved={};
    try{saved=JSON.parse(localStorage.getItem(key)||"{}")}catch(e){}
    var boxes=Array.prototype.slice.call(ck.querySelectorAll("input[type=checkbox]"));
    var bar=ck.querySelector(".ckbar i"),pct=ck.querySelector(".ckpct");
    function upd(){
      var done=0;
      boxes.forEach(function(b){
        b.closest(".ckitem").classList.toggle("on",b.checked);
        if(b.checked)done++;
      });
      var p=boxes.length?Math.round(done*100/boxes.length):0;
      if(bar)bar.style.width=p+"%";
      if(pct)pct.textContent=boxes.length+"개 중 "+done+"개 완료 ("+p+"%)"+
        (done===boxes.length&&boxes.length?" — 검증 완료!":"");
    }
    boxes.forEach(function(b,i){
      if(Object.prototype.hasOwnProperty.call(saved,i))b.checked=!!saved[i];
      b.addEventListener("change",function(){
        saved[i]=b.checked;
        try{localStorage.setItem(key,JSON.stringify(saved))}catch(e){}
        upd();
      });
    });
    upd();
  });

  var links=Array.prototype.slice.call(document.querySelectorAll("#toc a"));
  var targets=links.map(function(a){
    var el=document.querySelector(a.getAttribute("href"));
    return el?{a:a,el:el}:null;
  }).filter(Boolean);
  function spy(){
    var y=window.scrollY+110,cur=null;
    targets.forEach(function(t){if(t.el.offsetTop<=y)cur=t.a;});
    links.forEach(function(a){a.classList.toggle("on",a===cur);});
  }
  var ticking=false;
  window.addEventListener("scroll",function(){
    if(ticking)return; ticking=true;
    window.requestAnimationFrame(function(){spy();ticking=false;});
  },{passive:true});
  spy();
})();
"""

STYLE_TOKENS = {"hi", "ok", "no", "wa"}
CALLOUT_KIND = {"info": "", "warn": "warnc", "bad": "badc", "good": "goodc"}


# --------------------------------------------------------------------------
# frontmatter
# --------------------------------------------------------------------------

def parse_frontmatter(text: str) -> tuple[dict, str]:
    """`---` 로 감싼 최소 YAML(문자열 값 + 단순 리스트)을 파싱한다."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end < 0:
        return {}, text
    head = text[3:end].strip("\n")
    body = text[end + 4:].lstrip("\n")
    meta: dict = {}
    key = None
    for line in head.split("\n"):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if re.match(r"^\s+-\s+", line):
            if key:
                meta.setdefault(key, [])
                if isinstance(meta[key], list):
                    meta[key].append(_unquote(line.split("-", 1)[1].strip()))
            continue
        m = re.match(r"^([A-Za-z_][\w-]*)\s*:\s*(.*)$", line)
        if m:
            key, val = m.group(1), m.group(2).strip()
            meta[key] = _unquote(val) if val else []
    return meta, body


def _unquote(s: str) -> str:
    if len(s) >= 2 and s[0] == s[-1] and s[0] in "\"'":
        return s[1:-1]
    return s


# --------------------------------------------------------------------------
# 마크다운 서브셋
# --------------------------------------------------------------------------

def md_inline(s: str) -> str:
    """인라인 마크다운 → HTML. 코드 스팬을 먼저 보호한 뒤 이스케이프한다."""
    spans: list[str] = []

    def hold(m):
        spans.append(m.group(1))
        return f"\x00{len(spans) - 1}\x00"

    s = re.sub(r"`([^`]+)`", hold, s)
    s = html_mod.escape(s, quote=False)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\*\w])\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", s)
    s = re.sub(r"~~(.+?)~~", r"<del>\1</del>", s)
    s = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", r'<a href="\2">\1</a>', s)
    s = re.sub(r"\x00(\d+)\x00",
               lambda m: "<code>" + html_mod.escape(spans[int(m.group(1))], quote=False) + "</code>", s)
    return s


def _table(lines: list[str]) -> str:
    def cells(row: str) -> list[str]:
        row = row.strip()
        if row.startswith("|"):
            row = row[1:]
        if row.endswith("|"):
            row = row[:-1]
        return [c.strip() for c in row.split("|")]

    header = cells(lines[0])
    aligns = ["r" if c.strip().endswith(":") and c.strip().startswith("-") is False or c.strip().startswith("---") and c.strip().endswith(":") else ""
              for c in cells(lines[1])]
    out = ['<table class="tbl"><thead><tr>']
    for i, h in enumerate(header):
        cls = ' class="r"' if i < len(aligns) and aligns[i] == "r" else ""
        out.append(f"<th{cls}>{md_inline(h)}</th>")
    out.append("</tr></thead><tbody>")
    for row in lines[2:]:
        if not row.strip():
            continue
        out.append("<tr>")
        for i, c in enumerate(cells(row)):
            cls = ' class="r"' if i < len(aligns) and aligns[i] == "r" else ""
            out.append(f"<td{cls}>{md_inline(c)}</td>")
        out.append("</tr>")
    out.append("</tbody></table>")
    return "".join(out)


def render_md(text: str, hs: list | None = None, sec_idx: int = 0) -> str:
    """마크다운 서브셋 → HTML. hs 가 주어지면 ### 제목을 (id, 텍스트)로 수집한다."""
    lines = text.split("\n")
    out: list[str] = []
    i = 0
    sub = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue

        m = re.match(r"^(#{3,4})\s+(.*?)\s*(?:\{#([\w-]+)\})?\s*$", line)
        if m:
            level = len(m.group(1))
            title = m.group(2)
            if level == 3:
                sub += 1
                hid = m.group(3) or f"s{sec_idx}-{sub}"
                if hs is not None:
                    hs.append((hid, title))
                out.append(f'<h3 id="{hid}">{md_inline(title)}</h3>')
            else:
                out.append(f"<h4>{md_inline(title)}</h4>")
            i += 1
            continue

        if re.match(r"^---+\s*$", line):
            out.append('<hr class="soft">')
            i += 1
            continue

        if "|" in line and i + 1 < len(lines) and re.match(r"^\s*\|?[\s:|-]{3,}\|", lines[i + 1]):
            blk = []
            while i < len(lines) and lines[i].strip():
                blk.append(lines[i])
                i += 1
            out.append(_table(blk))
            continue

        if re.match(r"^\s*[-*]\s+", line):
            items = []
            while i < len(lines) and re.match(r"^\s*[-*]\s+", lines[i]):
                items.append(re.sub(r"^\s*[-*]\s+", "", lines[i]))
                i += 1
            out.append("<ul>" + "".join(f"<li>{md_inline(x)}</li>" for x in items) + "</ul>")
            continue

        if re.match(r"^\s*\d+\.\s+", line):
            items = []
            while i < len(lines) and re.match(r"^\s*\d+\.\s+", lines[i]):
                items.append(re.sub(r"^\s*\d+\.\s+", "", lines[i]))
                i += 1
            out.append('<ol class="md">' + "".join(f"<li>{md_inline(x)}</li>" for x in items) + "</ol>")
            continue

        if line.lstrip().startswith("<"):
            blk = []
            while i < len(lines) and lines[i].strip():
                blk.append(lines[i])
                i += 1
            out.append("\n".join(blk))
            continue

        para = []
        cls = ""
        while i < len(lines) and lines[i].strip() and not re.match(r"^(#{3,4}\s|---+\s*$|\s*[-*]\s|\s*\d+\.\s)", lines[i]) \
                and not lines[i].lstrip().startswith("<"):
            t = lines[i]
            if t.startswith("!lede "):
                cls = ' class="lede"'
                t = t[6:]
            para.append(t)
            i += 1
        if para:
            out.append(f"<p{cls}>{md_inline(' '.join(para))}</p>")
    return "\n".join(out)


# --------------------------------------------------------------------------
# 지시자(diagram / code / callout)
# --------------------------------------------------------------------------

def _split_caption(body: str) -> tuple[list[str], str]:
    lines, cap = [], ""
    for ln in body.split("\n"):
        if ln.strip().startswith(":: "):
            cap = ln.strip()[3:]
        elif ln.strip() == "::":
            cap = ""
        else:
            lines.append(ln)
    return [l for l in lines if l.strip()], cap


def _fig(label: str, inner: str, cap: str) -> str:
    head = f'<div class="lbl">{md_inline(label)}</div>' if label else ""
    tail = f'<div class="cap">{md_inline(cap)}</div>' if cap else ""
    return f'<div class="fig">{head}{inner}{tail}</div>'


def d_flow(title: str, body: str) -> str:
    rows, cap = _split_caption(body)
    boxes = []
    for r in rows:
        parts = [p.strip() for p in r.split("|")]
        style = ""
        if len(parts) >= 3 and parts[-1] in STYLE_TOKENS:
            style = " " + parts.pop()
        t = parts[0] if parts else ""
        d = parts[1] if len(parts) > 1 else ""
        dd = f'<span class="d">{md_inline(d)}</span>' if d else ""
        boxes.append(f'<div class="dbox{style}"><span class="t">{md_inline(t)}</span>{dd}</div>')
    inner = '<div class="arrow">→</div>'.join(boxes)
    return _fig(title, f'<div class="flow">{inner}</div>', cap)


def d_stack(title: str, body: str) -> str:
    rows, cap = _split_caption(body)
    out = []
    for r in rows:
        style = ""
        m = re.search(r"\[(\w+)\]\s*$", r)
        if m and m.group(1) in STYLE_TOKENS:
            style = " " + m.group(1)
            r = r[:m.start()].strip()
        pills = [p.strip() for p in r.split(">") if p.strip()]
        cells = []
        for k, p in enumerate(pills):
            if k:
                cells.append('<span class="arrow">→</span>')
            cells.append(f'<span class="pill{style}">{md_inline(p)}</span>')
        out.append('<div class="row">' + "".join(cells) + "</div>")
    return _fig(title, '<div class="dstack">' + "".join(out) + "</div>", cap)


def d_uiwin(title: str, body: str) -> str:
    rows, cap = _split_caption(body)
    wins: list[tuple[str, list[str]]] = []
    cur_label, cur_body = "", []
    for r in rows:
        s = r.strip()
        if s.startswith("win:"):
            if cur_body or cur_label:
                wins.append((cur_label, cur_body))
            cur_label, cur_body = s[4:].strip(), []
        else:
            cur_body.append(s)
    if cur_body or cur_label:
        wins.append((cur_label, cur_body))

    cards = []
    for label, items in wins:
        inner = []
        for it in items:
            if it == "stub":
                inner.append('<div class="uistub"></div><div class="uistub s"></div>')
                continue
            m = re.match(r"^banner(\.mute)?:\s*(.*)$", it)
            if m:
                mute = " mute" if m.group(1) else ""
                rest = m.group(2)
                btn = ""
                if "|" in rest:
                    rest, bt = rest.split("|", 1)
                    bm = re.match(r"^\s*btn(\.\w+)?:\s*(.*)$", bt.strip())
                    if bm:
                        bcls = (" " + bm.group(1)[1:]) if bm.group(1) else ""
                        btn = f'<span class="uibtn{bcls}">{md_inline(bm.group(2).strip())}</span>'
                inner.append(f'<div class="uibanner{mute}"><span>{md_inline(rest.strip())}</span>{btn}</div>')
                continue
            inner.append(f"<p>{md_inline(it)}</p>")
        lab = f'<div class="lbl">{md_inline(label)}</div>' if label else ""
        cards.append(
            f'<div>{lab}<div class="uiwin"><div class="uibar">'
            f'<span class="uidot"></span><span class="uidot"></span><span class="uidot"></span>'
            f'<span class="ttl">{md_inline(title or "앱")}</span></div>'
            f'<div class="uibody">{"".join(inner)}</div></div></div>'
        )
    n = " n2" if len(cards) == 2 else ""
    return _fig(title, f'<div class="wins{n}">' + "".join(cards) + "</div>", cap)


def _pre(code: str, lang: str, cap: str = "") -> str:
    esc = html_mod.escape(code.rstrip("\n"), quote=False)
    tail = f'<div class="codecap">{md_inline(cap)}</div>' if cap else ""
    return f'<pre><code data-lang="{lang}">{esc}</code></pre>{tail}'


def _git(repo: Path, args: list[str]) -> str:
    r = subprocess.run(["git", "-C", str(repo), "--no-pager"] + args,
                       capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} 실패: {r.stderr.strip()}")
    return r.stdout


def _opts(body: str) -> tuple[dict, str]:
    opts, rest = {}, []
    for ln in body.split("\n"):
        m = re.match(r"^(rev|grep|context|max|strip|lang|cap)\s*:\s*(.*)$", ln.strip())
        if m:
            opts[m.group(1)] = m.group(2).strip()
        else:
            rest.append(ln)
    return opts, "\n".join(rest)


def d_gitdiff(title: str, body: str, repo: Path | None) -> str:
    if repo is None:
        raise RuntimeError("gitdiff 지시자에는 frontmatter 의 repo: 또는 --repo 가 필요합니다")
    o, _ = _opts(body)
    rev = o.get("rev", "HEAD~1..HEAD")
    ctx = o.get("context", "3")
    args = ["diff", f"-U{ctx}"] + rev.split() + ["--", title]
    text = _git(repo, args)
    if not text.strip():
        raise RuntimeError(f"gitdiff: '{rev} -- {title}' 에 변경이 없습니다")
    if o.get("strip", "true") != "false":
        text = "\n".join(l for l in text.split("\n")
                         if not re.match(r"^(diff --git|index |new file|deleted file|old mode|new mode|similarity|rename )", l))
    if "grep" in o:
        needle = o["grep"]
        head = [l for l in text.split("\n") if re.match(r"^(--- |\+\+\+ )", l)]
        hunks = re.split(r"(?m)^(?=@@)", text)
        kept = [h for h in hunks if h.startswith("@@") and needle in h]
        if not kept:
            raise RuntimeError(f"gitdiff: grep '{needle}' 에 해당하는 hunk 가 없습니다")
        text = "\n".join(head + [h.rstrip("\n") for h in kept])
    if "max" in o:
        ls = text.split("\n")
        n = int(o["max"])
        if len(ls) > n:
            text = "\n".join(ls[:n] + [f"… ({len(ls) - n}줄 생략)"])
    return _pre(text, "diff", o.get("cap", ""))


def d_snippet(title: str, body: str, repo: Path | None) -> str:
    o, _ = _opts(body)
    m = re.match(r"^(.*?)(?::(\d+)-(\d+))?$", title.strip())
    path, a, b = m.group(1), m.group(2), m.group(3)
    if "rev" in o:
        if repo is None:
            raise RuntimeError("snippet 의 rev: 에는 repo 가 필요합니다")
        text = _git(repo, ["show", f"{o['rev']}:{path}"])
    else:
        base = repo if repo else Path(".")
        text = (base / path).read_text(encoding="utf-8")
    if a and b:
        ls = text.split("\n")
        text = "\n".join(ls[int(a) - 1:int(b)])
    lang = o.get("lang") or _lang_of(path)
    return _pre(text, lang, o.get("cap", ""))


def _lang_of(path: str) -> str:
    ext = Path(path).suffix.lower()
    return {".ts": "ts", ".tsx": "ts", ".js": "ts", ".mjs": "ts", ".py": "ts",
            ".yml": "yaml", ".yaml": "yaml"}.get(ext, "text")


def d_code(title: str, body: str) -> str:
    parts = title.split(None, 1)
    lang = parts[0] if parts else "text"
    cap = parts[1] if len(parts) > 1 else ""
    return _pre(body, lang, cap)


def d_callout(title: str, body: str) -> str:
    parts = title.split(None, 1)
    kind = parts[0] if parts and parts[0] in CALLOUT_KIND else "info"
    label = (parts[1] if len(parts) > 1 else "") if parts and parts[0] in CALLOUT_KIND \
        else (title or "")
    cls = CALLOUT_KIND[kind]
    tag = f'<span class="tag">{md_inline(label)}</span>' if label else ""
    return f'<div class="call {cls}">{tag}{render_md(body)}</div>'


# --------------------------------------------------------------------------
# 원문 패널 — 플랜 원문 md 를 통째로 렌더해 드로어에 내장한다
# --------------------------------------------------------------------------

def _norm_head(s: str) -> str:
    """src: 링크 매칭용 정규화 — 공백·하이픈·마크다운 장식을 제거하고 casefold."""
    return re.sub(r"[\s\-—·*`_#]+", "", s).casefold()


def render_plain_md(text: str) -> tuple[str, list[tuple[str, str]]]:
    """원문 마크다운 전체 → HTML. 코드 펜스를 지원하고 모든 제목에 src-hN id 를 부여한다.

    반환: (html, [(id, 제목 텍스트), ...])
    """
    pres: list[str] = []

    def hold_fence(m):
        lang = (m.group(1) or "").strip().split()[0] if (m.group(1) or "").strip() else "text"
        lang = {"typescript": "ts", "javascript": "ts", "python": "ts", "bash": "text",
                "sh": "text", "shell": "text", "json": "ts"}.get(lang, lang)
        if lang not in ("ts", "yaml", "yml", "diff", "text"):
            lang = "text"
        pres.append(_pre(m.group(2), lang))
        return f"\x01{len(pres) - 1}\x01"

    text = re.sub(r"(?ms)^```([^\n]*)\n(.*?)^```\s*$", hold_fence, text)

    heads: list[tuple[str, str]] = []
    lines = text.split("\n")
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        pm = re.match(r"^\x01(\d+)\x01\s*$", line.strip())
        if pm:
            out.append(pres[int(pm.group(1))])
            i += 1
            continue
        hm = re.match(r"^(#{1,4})\s+(.*?)\s*$", line)
        if hm:
            level = len(hm.group(1))
            title = hm.group(2)
            hid = f"src-h{len(heads)}"
            heads.append((hid, title))
            tag = min(level + 1, 5)  # 원문 h1 → 패널 h2 …
            out.append(f'<h{tag} id="{hid}" class="srch">{md_inline(title)}</h{tag}>')
            i += 1
            continue
        if re.match(r"^---+\s*$", line):
            out.append('<hr class="soft">')
            i += 1
            continue
        if "|" in line and i + 1 < len(lines) and re.match(r"^\s*\|?[\s:|-]{3,}\|", lines[i + 1]):
            blk = []
            while i < len(lines) and lines[i].strip():
                blk.append(lines[i])
                i += 1
            out.append(_table(blk))
            continue
        if re.match(r"^\s*[-*]\s+", line):
            items = []
            while i < len(lines) and re.match(r"^\s*[-*]\s+", lines[i]):
                items.append(re.sub(r"^\s*[-*]\s+", "", lines[i]))
                i += 1
            out.append("<ul>" + "".join(f"<li>{md_inline(x)}</li>" for x in items) + "</ul>")
            continue
        if re.match(r"^\s*\d+\.\s+", line):
            items = []
            while i < len(lines) and re.match(r"^\s*\d+\.\s+", lines[i]):
                items.append(re.sub(r"^\s*\d+\.\s+", "", lines[i]))
                i += 1
            out.append('<ol class="md">' + "".join(f"<li>{md_inline(x)}</li>" for x in items) + "</ol>")
            continue
        para = []
        while i < len(lines) and lines[i].strip() \
                and not re.match(r"^(#{1,4}\s|---+\s*$|\s*[-*]\s|\s*\d+\.\s|\x01\d+\x01\s*$)", lines[i].strip() if lines[i].strip().startswith("\x01") else lines[i]):
            para.append(lines[i])
            i += 1
        if para:
            out.append(f"<p>{md_inline(' '.join(para))}</p>")
    return "\n".join(out), heads


def resolve_src_links(body_html: str, heads: list[tuple[str, str]], has_plan: bool) -> str:
    """본문의 href="src:검색어" 링크를 원문 제목 앵커로 치환한다. 미해결이면 오류."""

    def sub(m):
        needle = m.group(1)
        if not has_plan:
            raise RuntimeError("src: 링크를 쓰려면 frontmatter 의 plan: (원문 경로)이 필요합니다")
        n = _norm_head(needle)
        for hid, title in heads:
            if n and n in _norm_head(title):
                return f'class="srclink" data-src="{hid}" href="#{hid}"'
        raise RuntimeError(f"src: '{needle}' 에 맞는 원문 제목이 없습니다 — 원문 제목 일부를 쓰세요"
                           f" (공백 대신 하이픈 가능)")

    return re.sub(r'href="src:([^"]+)"', sub, body_html)


# --------------------------------------------------------------------------
# 플랜 전용 지시자
# --------------------------------------------------------------------------

TL_STATUS = {"done", "now", "gate"}


def d_timeline(title: str, body: str) -> str:
    """Phase 로드맵: `배지 | 제목 | 공수·게이트 | 상태(done/now/gate)` + `| 설명` 선택."""
    rows, cap = _split_caption(body)
    items = []
    for r in rows:
        parts = [p.strip() for p in r.split("|")]
        status = ""
        if len(parts) >= 2 and parts[-1] in TL_STATUS:
            status = " " + parts.pop()
        badge = parts[0] if parts else ""
        t = parts[1] if len(parts) > 1 else ""
        chip = parts[2] if len(parts) > 2 else ""
        desc = parts[3] if len(parts) > 3 else ""
        chip_html = f'<span class="pill{status or ""}">{md_inline(chip)}</span>' if chip else ""
        desc_html = f'<div class="tl-d">{md_inline(desc)}</div>' if desc else ""
        items.append(
            f'<div class="tl{status}"><div class="tl-dot">{md_inline(badge)}</div>'
            f'<div class="tl-body"><div class="tl-head"><span class="tl-t">{md_inline(t)}</span>'
            f'{chip_html}</div>{desc_html}</div></div>'
        )
    return _fig(title, '<div class="tline">' + "".join(items) + "</div>", cap)


def d_deps(title: str, body: str) -> str:
    """의존 그래프: `id: 라벨 [스타일] <- 선행id들`. 위상 정렬로 층을 배치한다."""
    rows, cap = _split_caption(body)
    nodes: dict[str, dict] = {}
    order: list[str] = []
    for r in rows:
        m = re.match(r"^([\w가-힣.-]+)\s*:\s*(.*)$", r.strip())
        if not m:
            raise RuntimeError(f"deps: 형식 오류 — `id: 라벨 <- 선행id` 여야 합니다: {r!r}")
        nid, rest = m.group(1), m.group(2)
        style = ""
        sm = re.search(r"\[(\w+)\]\s*$", rest)
        if sm and sm.group(1) in STYLE_TOKENS:
            style = " " + sm.group(1)
            rest = rest[:sm.start()]
        deps: list[str] = []
        if "<-" in rest:
            rest, dep_s = rest.split("<-", 1)
            deps = [d for d in re.split(r"[,\s]+", dep_s.strip()) if d]
        nodes[nid] = {"label": rest.strip(), "deps": deps, "style": style}
        order.append(nid)

    for nid, n in nodes.items():
        for d in n["deps"]:
            if d not in nodes:
                raise RuntimeError(f"deps: '{nid}' 의 선행 '{d}' 가 정의되지 않았습니다")

    layer: dict[str, int] = {}

    def depth(nid: str, seen: frozenset = frozenset()) -> int:
        if nid in seen:
            raise RuntimeError(f"deps: 순환 의존 발견 — {nid}")
        if nid not in layer:
            n = nodes[nid]
            layer[nid] = 0 if not n["deps"] else \
                1 + max(depth(d, seen | {nid}) for d in n["deps"])
        return layer[nid]

    for nid in order:
        depth(nid)

    max_layer = max(layer.values()) if layer else 0
    out = []
    for lv in range(max_layer + 1):
        if lv:
            out.append('<div class="dep-join">↓ 선행 완료 후</div>')
        boxes = []
        for nid in order:
            if layer[nid] != lv:
                continue
            n = nodes[nid]
            frm = f'<span class="dep-from">← {", ".join(n["deps"])}</span>' if n["deps"] else ""
            boxes.append(
                f'<div class="dbox{n["style"]}"><span class="t">{md_inline(nid)}</span>'
                f'<span class="d">{md_inline(n["label"])}</span>{frm}</div>'
            )
        out.append('<div class="dep-layer">' + "".join(boxes) + "</div>")
    return _fig(title, '<div class="deps">' + "".join(out) + "</div>", cap)


FILE_BADGE = {"+": ("add", "신규"), "~": ("mod", "수정"), "-": ("del", "삭제"), "?": ("tbd", "미정")}


def d_files(title: str, body: str) -> str:
    """파일 배치 맵: `+ path | 설명` (접두어: + 신규 / ~ 수정 / - 삭제 / ? 미정)."""
    rows, cap = _split_caption(body)
    trs = []
    for r in rows:
        s = r.strip()
        if s[:1] not in FILE_BADGE:
            raise RuntimeError(f"files: 각 줄은 + ~ - ? 중 하나로 시작해야 합니다: {r!r}")
        cls, label = FILE_BADGE[s[0]]
        rest = s[1:].strip()
        path, note = (p.strip() for p in rest.split("|", 1)) if "|" in rest else (rest, "")
        trs.append(
            f'<tr><td><span class="fbadge {cls}">{label}</span></td>'
            f'<td class="fpath">{html_mod.escape(path)}</td>'
            f'<td class="fnote">{md_inline(note)}</td></tr>'
        )
    return _fig(title, '<table class="fmap"><tbody>' + "".join(trs) + "</tbody></table>", cap)


_CK_COUNTER = [0]


def d_checklist(title: str, body: str) -> str:
    """인터랙티브 체크리스트. `- [ ] 항목` / `- [x] 항목` / `- 항목`. 상태는 localStorage 저장."""
    rows, cap = _split_caption(body)
    items = []
    for r in rows:
        m = re.match(r"^\s*[-*]\s*(?:\[([ xX])\]\s*)?(.+)$", r)
        if not m:
            raise RuntimeError(f"checklist: 항목은 `- [ ] 내용` 형식이어야 합니다: {r!r}")
        checked = " checked" if (m.group(1) or "").lower() == "x" else ""
        items.append(
            f'<label class="ckitem"><input type="checkbox"{checked}>'
            f"<span>{md_inline(m.group(2).strip())}</span></label>"
        )
    _CK_COUNTER[0] += 1
    lbl = f'<div class="lbl">{md_inline(title)}</div>' if title else ""
    tail = f'<div class="cap">{md_inline(cap)}</div>' if cap else ""
    return (
        f'<div class="ck" data-ck="{_CK_COUNTER[0]}">{lbl}'
        f'<div class="ckbar"><i></i></div><div class="ckpct"></div>'
        f'{"".join(items)}{tail}</div>'
    )


def d_decision(title: str, body: str) -> str:
    """결정 카드: pick(선택, 필수) / why(근거) / drop(기각) / hold(보류) 필드."""
    rows, cap = _split_caption(body)
    pick, whys, alts = "", [], []
    for r in rows:
        m = re.match(r"^(pick|why|drop|hold)\s*:\s*(.*)$", r.strip())
        if not m:
            raise RuntimeError(f"decision: 각 줄은 pick/why/drop/hold 로 시작해야 합니다: {r!r}")
        k, v = m.group(1), m.group(2).strip()
        if k == "pick":
            pick = v
        elif k == "why":
            whys.append(v)
        else:
            alts.append((k, v))
    if not pick:
        raise RuntimeError("decision: pick 필드는 필수입니다")
    why_html = "".join(f'<p class="why">{md_inline(w)}</p>' for w in whys)
    alt_html = ""
    if alts:
        lis = "".join(
            f'<li class="{k}"><span class="altbody">{md_inline(v)}</span></li>' for k, v in alts)
        alt_html = f'<ul class="alt">{lis}</ul>'
    cap_html = f'<div class="cap">{md_inline(cap)}</div>' if cap else ""
    return (
        f'<div class="dec"><span class="tag">결정</span>'
        f'<p class="dt">{md_inline(title)}</p>'
        f'<div class="pick">{md_inline(pick)}</div>{why_html}{alt_html}{cap_html}</div>'
    )


def parse_quiz(body: str) -> list[dict]:
    qs = []
    for blk in re.split(r"(?m)^---+\s*$", body):
        blk = blk.strip()
        if not blk:
            continue
        q, why, opts = "", "", []
        for ln in blk.split("\n"):
            s = ln.strip()
            if s.startswith("Q:"):
                q = s[2:].strip()
            elif s.startswith("* "):
                opts.append((s[2:].strip(), True))
            elif s.startswith("- "):
                opts.append((s[2:].strip(), False))
            elif s.startswith("> "):
                why += (" " if why else "") + s[2:].strip()
        if not q or not opts:
            continue
        random.shuffle(opts)
        a = next((i for i, (_, c) in enumerate(opts) if c), 0)
        qs.append({"q": md_inline(q), "opts": [md_inline(t) for t, _ in opts],
                   "a": a, "why": md_inline(why)})
    return qs


# --------------------------------------------------------------------------
# 문서 조립
# --------------------------------------------------------------------------

@dataclass
class Section:
    sid: str
    title: str
    html: str = ""
    subs: list = field(default_factory=list)


FENCE = re.compile(r"(?ms)^```([a-zA-Z][\w]*)([^\n]*)\n(.*?)^```\s*$")


def render_body(body: str, repo: Path | None, quiz_out: list) -> list[Section]:
    chunks = re.split(r"(?m)^##\s+", body)
    intro = chunks[0].strip()
    sections: list[Section] = []
    if intro:
        sections.append(Section("s0", "", render_blocks(intro, repo, quiz_out, 0)))
    for n, ch in enumerate(chunks[1:], start=1):
        head, _, rest = ch.partition("\n")
        m = re.match(r"^(.*?)\s*(?:\{#([\w-]+)\})?\s*$", head.strip())
        title, sid = m.group(1), m.group(2) or f"s{n}"
        sec = Section(sid, title)
        sec.html = render_blocks(rest, repo, quiz_out, n, sec.subs)
        sections.append(sec)
    return sections


def render_blocks(text: str, repo: Path | None, quiz_out: list,
                  sec_idx: int, subs: list | None = None) -> str:
    out, pos = [], 0
    for m in FENCE.finditer(text):
        pre = text[pos:m.start()]
        if pre.strip():
            out.append(render_md(pre, subs, sec_idx))
        kind, arg, inner = m.group(1), m.group(2).strip(), m.group(3)
        out.append(dispatch(kind, arg, inner, repo, quiz_out))
        pos = m.end()
    tail = text[pos:]
    if tail.strip():
        out.append(render_md(tail, subs, sec_idx))
    return "\n".join(x for x in out if x)


def dispatch(kind: str, arg: str, inner: str, repo: Path | None, quiz_out: list) -> str:
    if kind == "flow":
        return d_flow(arg, inner)
    if kind == "stack":
        return d_stack(arg, inner)
    if kind == "uiwin":
        return d_uiwin(arg, inner)
    if kind == "gitdiff":
        return d_gitdiff(arg, inner, repo)
    if kind == "snippet":
        return d_snippet(arg, inner, repo)
    if kind == "code":
        return d_code(arg, inner)
    if kind == "callout":
        return d_callout(arg, inner)
    if kind == "timeline":
        return d_timeline(arg, inner)
    if kind == "deps":
        return d_deps(arg, inner)
    if kind == "files":
        return d_files(arg, inner)
    if kind == "checklist":
        return d_checklist(arg, inner)
    if kind == "decision":
        return d_decision(arg, inner)
    if kind == "html":
        return inner
    if kind == "quiz":
        quiz_out.extend(parse_quiz(inner))
        return "__QUIZ_SLOT__"
    raise RuntimeError(f"알 수 없는 지시자: ```{kind}")


def build(meta: dict, sections: list[Section], quiz: list[dict],
          src: tuple[str, str, list] | None = None) -> str:
    toc = []
    for i, s in enumerate(sections):
        if not s.title:
            continue
        toc.append(f'<li><a href="#{s.sid}">{md_inline(s.title)}</a>')
        if s.subs:
            toc.append("<ol>" + "".join(
                f'<li><a href="#{hid}">{md_inline(t)}</a></li>' for hid, t in s.subs) + "</ol>")
        toc.append("</li>")

    parts = []
    part_no = 0
    for s in sections:
        if not s.title:
            parts.append(f'<section id="{s.sid}">{s.html}</section>')
            continue
        part_no += 1
        parts.append(
            f'<section id="{s.sid}"><h2 class="sec">'
            f'<span class="num">Part {part_no}</span>{md_inline(s.title)}</h2>\n{s.html}</section>'
        )
    body_html = "\n".join(parts)

    quiz_block = '<div id="quizroot"></div><div class="score" id="score">아직 푼 문제가 없습니다.</div>'
    body_html = body_html.replace("__QUIZ_SLOT__", quiz_block if quiz else "")

    body_html = resolve_src_links(body_html, src[2] if src else [], src is not None)
    src_html = ""
    src_btn = ""
    if src:
        src_btn = '<button class="srchbtn" id="srchbtn" type="button">플랜 원문 보기 ↗</button>'
    if src:
        name, panel, _ = src
        src_html = (
            '<div class="srcback" id="srcback"></div>'
            '<aside class="srcpanel" id="srcpanel">'
            f'<div class="srchead"><span class="tag">플랜 원문</span>'
            f'<span class="srcname">{html_mod.escape(name)}</span>'
            '<button class="srcclose" id="srcclose" type="button">닫기 ✕</button></div>'
            f'<div class="srcbody">{panel}</div></aside>'
            '<button class="srcfab" id="srcfab" type="button">플랜 원문</button>'
        )

    chips = "".join(f"<span>{md_inline(x)}</span>" for x in meta.get("meta", []) or [])
    kicker = f'<p class="kicker">{md_inline(meta["kicker"])}</p>' if meta.get("kicker") else ""
    stand = f'<p class="standfirst">{md_inline(meta["subtitle"])}</p>' if meta.get("subtitle") else ""
    doc_key = meta.get("slug") or slugify(meta.get("title", ""))
    quiz_js = "window.__QUIZ__=" + _json(quiz) + ";window.__DOC__=" + _json(doc_key) + ";"

    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html_mod.escape(meta.get("title", "해설"))}</title>
<style>{CSS}</style>
</head>
<body>
<header class="mast"><div class="mast-in">
{kicker}<h1>{md_inline(meta.get("title", ""))}</h1>
{stand}
<div class="meta">{chips}{src_btn}</div>
</div></header>
<div class="wrap">
<nav class="toc" id="toc"><h2>목차</h2><ol>{"".join(toc)}</ol></nav>
<article>
{body_html}
</article>
</div>
{src_html}
<script>{quiz_js}</script>
<script>{JS}</script>
</body>
</html>
"""


def _json(obj) -> str:
    import json
    return json.dumps(obj, ensure_ascii=False).replace("</", "<\\/")


def slugify(text: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return s or "explanation"


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("doc", type=Path, help="마크다운 소스 문서")
    ap.add_argument("-o", "--output", type=Path, default=None)
    ap.add_argument("--repo", type=Path, default=None, help="gitdiff/snippet 기준 저장소")
    ap.add_argument("--plan", type=Path, default=None,
                    help="플랜 원문 md — 드로어에 내장되고 src: 링크의 대상이 된다")
    ap.add_argument("--open", action="store_true", help="렌더 후 기본 브라우저로 열기")
    ap.add_argument("--seed", type=int, default=None, help="퀴즈 보기 셔플 시드(재현용)")
    args = ap.parse_args()

    if args.seed is not None:
        random.seed(args.seed)

    text = args.doc.read_text(encoding="utf-8")
    meta, body = parse_frontmatter(text)
    repo = args.repo or (Path(meta["repo"]).expanduser() if meta.get("repo") else None)

    plan_path = args.plan or (Path(meta["plan"]).expanduser() if meta.get("plan") else None)
    if plan_path and not plan_path.is_absolute():
        plan_path = (args.doc.parent / plan_path).resolve()

    quiz: list[dict] = []
    try:
        src = None
        if plan_path:
            if not plan_path.exists():
                raise RuntimeError(f"plan: 원문 파일이 없습니다 — {plan_path}")
            panel, heads = render_plain_md(plan_path.read_text(encoding="utf-8"))
            src = (plan_path.name, panel, heads)
        sections = render_body(body, repo, quiz)
        out_html = build(meta, sections, quiz, src)
    except RuntimeError as e:
        print(f"오류: {e}", file=sys.stderr)
        return 1
    if args.output:
        out_path = args.output
    else:
        stamp = datetime.date.today().strftime("%Y-%m-%d")
        slug = meta.get("slug") or slugify(meta.get("title", ""))
        out_path = Path(f"/tmp/{stamp}-plan-{slug}.html")
    out_path.write_text(out_html, encoding="utf-8")
    print(str(out_path))

    if args.open:
        subprocess.run(["open", str(out_path)], check=False)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
