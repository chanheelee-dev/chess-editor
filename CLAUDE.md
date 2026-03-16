# Chess Editor — Development Guidelines

## Project Overview

터미널 기반 체스 보드 에디터. Rich 라이브러리를 사용한 TUI.

## Commands

```bash
uv sync          # 의존성 설치
uv run chess-editor  # 실행
uv run pytest    # 테스트 (테스트 파일 존재 시)
```

## Active Technologies

- Python 3.13+, uv, Rich

## Project Structure

```
src/chess_editor/
├── __init__.py
├── board.py     # ChessBoard, Piece, PieceColor, PieceType
├── main.py      # ChessBoardRenderer, main()
└── utils/
```

---

## Spec-Driven Development Workflow

> **모바일 사용 시 중요**: 슬래시 커맨드(`/speckit.*`) 대신 아래 워크플로우를 직접 따른다.
> 데스크탑에서는 `/speckit.specify`, `/speckit.plan`, `/speckit.tasks`, `/speckit.implement` 슬래시 커맨드를 사용할 수 있다.

### 핵심 규칙

**스펙 없이 구현을 시작하지 않는다.**

모든 새 기능은 반드시 이 순서를 따른다:
```
Specify → Plan → Tasks → Implement
```

---

### Step 1: Specify (요구사항 정의)

**목적**: 사용자 관점에서 "무엇을"/"왜"를 정의. 기술 결정 X.

```bash
# 새 스펙 파일 생성
.specify/scripts/create-spec.sh <feature-name>
# 예: .specify/scripts/create-spec.sh fen-support
```

또는 수동으로:
```
.specify/specs/NN-feature-name.md  (NN = 순서 번호)
```

**스펙 파일 내용** (`.specify/templates/spec-template.md` 참조):
- User Stories (Given/When/Then 형식)
- Functional Requirements (FR-001, FR-002...)
- Success Criteria (측정 가능한 기준)
- 불명확한 항목: `[NEEDS CLARIFICATION]` 표시

**품질 기준**:
- 각 User Story는 독립적으로 가치를 제공해야 함
- 기술 구현 방법 언급 X (대신 plan.md에서)
- `[NEEDS CLARIFICATION]` 최대 3개

---

### Step 2: Plan (기술 구현 계획)

**목적**: 스펙을 기술적 구현 방법으로 변환.

파일: `.specify/specs/NN-feature-name-plan.md`
템플릿: `.specify/templates/plan-template.md`

**플랜 파일 내용**:
- Technical Context (언어, 프레임워크, 의존성)
- Constitution Check (`.specify/memory/constitution.md` 원칙 준수 확인)
- Architecture (수정/생성할 파일 목록, 데이터 모델)
- Complexity Justification (단순한 대안이 있음에도 복잡도가 필요한 이유)

**규칙**: 미해결 `[NEEDS CLARIFICATION]` 항목이 있으면 플랜 시작 금지.

---

### Step 3: Tasks (태스크 분해)

**목적**: 플랜을 구체적인 체크박스 태스크로 분해.

파일: `.specify/specs/NN-feature-name-tasks.md`
템플릿: `.specify/templates/tasks-template.md`

**태스크 형식**:
```
- [ ] [T001] [P] [US1] src/chess_editor/fen.py 에 parse_fen() 함수 구현
```
- `[TID]`: 고유 태스크 ID
- `[P]`: 병렬 실행 가능 표시 (다른 파일, 의존성 없음)
- `[USN]`: 어느 User Story 소속인지

**Phase 순서**:
1. Setup
2. Foundational (블로킹 전제조건 — 반드시 먼저 완료)
3-N. User Stories (P1→P2→P3 순)
Final. Polish

---

### Step 4: Implement (구현)

**목적**: 태스크 파일을 기준으로 순서대로 구현.

**규칙**:
- Phase 2 (Foundational)를 반드시 먼저 완료
- 각 태스크 완료 시 `- [x]` 로 체크
- `[P]` 표시 태스크는 같은 응답에서 병렬 처리 가능
- 스펙의 Acceptance Criteria를 기준으로 검증

**완료 후**:
- 모든 User Story Acceptance Criteria 충족 확인
- `uv run pytest` 실행 (테스트 있을 시)
- 커밋 메시지 제안

---

### Spec 파일 관리

```
.specify/
├── memory/
│   └── constitution.md     # 프로젝트 원칙 (변경 시 버전 업데이트)
├── specs/
│   ├── 01-fen-support.md           # 스펙
│   ├── 01-fen-support-plan.md      # 플랜
│   └── 01-fen-support-tasks.md     # 태스크
├── templates/
│   ├── spec-template.md
│   ├── plan-template.md
│   └── tasks-template.md
└── scripts/
    └── create-spec.sh
```

---

## Code Style

- 타입 힌트 사용 (Python 3.13+)
- docstring: 공개 메서드에만
- 의존성 추가 시 `uv add <package>`

<!-- MANUAL ADDITIONS START -->
<!-- MANUAL ADDITIONS END -->
