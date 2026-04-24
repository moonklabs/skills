---
name: hwp-format
description: HWP/HWPX 파일 형식 및 한국 공문서 서식 규칙을 안내합니다. "HWP", "HWPX", "한글 파일", "문서 내보내기", "파일 변환", "apply-export" 등의 맥락에서 자동 활성화됩니다.
---

# HWP/HWPX 파일 형식 가이드

## HWP vs HWPX

| 항목 | HWP (구형) | HWPX (신형) |
|------|-----------|------------|
| 파일 구조 | 바이너리 (OLE) | ZIP + XML (OOXML 유사) |
| 프로그래밍 처리 | 매우 어려움 | Python/Java로 생성 가능 |
| 한컴오피스 지원 | ✅ | ✅ (한컴오피스 2014+) |
| 정부 제출 | ✅ | ✅ (대부분 허용) |
| 파일 확장자 | .hwp | .hwpx |

**이 플러그인의 기본 출력 포맷:** HWPX

HWP 양식 파일이 있는 경우 `hwp2hwpx`(Java 라이브러리)로 HWPX로 변환 후 처리합니다.

---

## HWPX 파일 구조

HWPX는 ZIP 파일 안에 XML 파일들이 담긴 구조입니다 (DOCX와 유사):

```
document.hwpx (ZIP)
├── Contents/
│   ├── content.hml        ← 본문 내용 (XML)
│   ├── header.xml         ← 문서 헤더 (스타일, 페이지 설정)
│   └── section0.xml       ← 섹션 내용
├── BinData/               ← 이미지 등 바이너리
├── Preview/
│   └── PrvImage.png       ← 미리보기 이미지
└── [Content_Types].xml    ← MIME 타입 정의
```

---

## 한국 정부 공문서 서식 표준

사업계획서 작성 시 다음 서식을 준수합니다:

### 글꼴

| 용도 | 글꼴 | 대체 |
|------|------|------|
| 본문 | 함초롬바탕 | 맑은 고딕, 바탕 |
| 제목/소제목 | 함초롬돋움 | 맑은 고딕, 돋움 |
| 영문/숫자 | HY중고딕 | Arial |

### 글자 크기

| 용도 | 크기 |
|------|------|
| 대제목 | 16pt |
| 소제목 | 13pt |
| 본문 | 11pt |
| 주석/캡션 | 9pt |

### 줄 간격 및 여백

| 항목 | 권장값 |
|------|-------|
| 본문 줄 간격 | 160~180% |
| 용지 | A4 (210×297mm) |
| 여백 상 | 20mm |
| 여백 하 | 15mm |
| 여백 좌/우 | 20mm |
| 머리말 | 10mm |
| 꼬리말 | 10mm |

---

## 사업계획서 레이아웃 규칙

### 표지

```
[상단 여백]
공고명 (16pt, 중앙 정렬)
사업계획서 (20pt, 굵게, 중앙 정렬)

[중앙 공백]

회사명: ○○주식회사
대표자: 홍길동
제출일: 2026년 3월 1일
[하단 여백]
```

### 목차

자동 목차 기능 사용 권장. 수동 작성 시:
- 제목 번호: 1. / 1.1 / 1.1.1 형식
- 점선(……) + 페이지 번호

### 본문

- 제목(대): H1 스타일, 굵게, 밑줄
- 제목(소): H2 스타일, 굵게
- 소제목: H3 스타일, 굵게
- 본문: 기본 스타일
- 페이지 번호: 꼬리말 중앙

---

## hwp2hwpx 변환 안내

구형 .hwp 양식 파일을 .hwpx로 변환:

```
사용 라이브러리: hwp2hwpx (Java)
GitHub: https://github.com/neolord0/hwp2hwpx
```

**요구 환경:**
- Java Runtime Environment (JRE) 11+
- hwp2hwpx.jar

**변환 명령:**
```bash
java -jar hwp2hwpx.jar input.hwp output.hwpx
```

MCP 서버의 `convert_hwp_to_hwpx` 도구가 이 과정을 자동으로 처리합니다.
Java가 없는 환경에서는 변환을 건너뛰고 HWPX 직접 생성 모드로 fallback합니다.

---

## hwp-generator MCP 서버 도구 참조

`/apply-export` 커맨드에서 사용하는 MCP 도구:

| 도구명 | 기능 | 주요 파라미터 |
|-------|------|------------|
| `create_document` | 새 HWPX 문서 생성 | paper_size, margins, styles |
| `add_heading` | 제목 삽입 | text, level (1~3) |
| `add_paragraph` | 본문 텍스트 삽입 | text, bold, italic, underline |
| `add_table` | 표 삽입 | rows, cols, data, merge_cells |
| `add_image` | 이미지 삽입 | file_path, width, height, align |
| `fill_template` | 양식 HWPX 빈 필드 채우기 | template_path, field_map |
| `set_page_setup` | 페이지 설정 | paper, margins, header, footer |
| `convert_hwp_to_hwpx` | HWP → HWPX 변환 | input_path, output_path |
| `export_file` | 최종 파일 저장 | output_path, format (hwpx/pdf) |

---

## 양식 파일 빈 필드 탐지

정부 공고에서 제공하는 HWP 양식의 빈 필드 패턴:

```xml
<!-- 일반적인 빈 필드 패턴 -->
<hp:t>○○○○○</hp:t>      ← 채워야 할 텍스트 필드
<hp:t>[ ]</hp:t>          ← 체크박스 스타일
<hp:t>(                )</hp:t>   ← 괄호 빈 칸
```

`fill_template` 도구가 이 패턴을 자동으로 탐지하고 사업계획서 내용으로 채웁니다.

---

## 한계 및 대안

| 상황 | 대응 방법 |
|------|---------|
| 복잡한 양식 (다단, 특수 레이아웃) | 자동 채우기 실패 시 Markdown 초안 + 수동 복붙 안내 |
| Java 미설치 | HWP 변환 건너뛰고 HWPX 직접 생성 |
| LibreOffice 활용 | LibreOffice headless로 DOCX → HWPX 변환 (백업 경로) |
| 구형 공공기관 .hwp만 수락 | HWPX 생성 후 한컴오피스에서 .hwp로 저장 안내 |
