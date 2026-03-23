# Chess Editor Constitution

## Project

**Name**: chess-editor
**Description**: 터미널 기반 체스 보드 에디터 — 커스텀 체스 포지션을 생성하고 탐색하기 위한 TUI 도구.
**Entry Point**: `uv run chess-editor`

## Core Principles

### Terminal-First

모든 UI는 터미널 환경에서 동작해야 한다. Rich 라이브러리를 활용하여 아름답고 기능적인 TUI를 제공한다.

### Spec-Driven Development

구현 전에 반드시 스펙을 작성한다. 스펙은 사용자 관점에서 "무엇을"/"왜"를 기술하며, "어떻게"는 plan.md에서 다룬다.

### Simplicity First

가장 단순한 해결책을 먼저 시도한다. 불필요한 추상화, 조기 최적화, 과도한 설계를 피한다.

### Chess Standards Compliance

FEN 형식, 표준 체스 규칙, 유니코드 체스 기호(♔♕♖♗♘♙ / ♚♛♜♝♞♟) 등 기존 체스 표준을 준수한다.

### Python Idioms

Python 3.13+ 기능을 활용하고 타입 힌트를 사용한다. uv로 의존성을 관리한다. 공개 메서드에만 docstring을 작성한다.

### Separation of Concerns

데이터 모델(board.py)과 렌더링(main.py)을 분리한다. 비즈니스 로직은 UI 레이어에 포함되어서는 안 된다.

## Development Workflow

새 기능 개발 순서:
1. `.specify/specs/NN-feature-name.md` 에 스펙 파일 작성
2. `.specify/specs/NN-feature-name-plan.md` 에 플랜 파일 작성
3. `.specify/specs/NN-feature-name-tasks.md` 에 태스크 파일 작성
4. 태스크 순서대로 구현 (Foundational → User Stories → Polish)
5. 모든 Success Criteria 충족 확인 후 커밋

## Architecture Patterns

- **데이터 모델**: `Enum` 기반 타입 정의 (PieceColor, PieceType)
- **보드 상태**: `list[list[Optional[Piece]]]` — 8×8 격자
- **렌더링**: Rich `Table` + 셀별 배경색 스타일로 체커보드 구현
- **파일 구조**: `src/chess_editor/{board,main}.py` + `utils/` 서브패키지

## Tech Stack

- **언어**: Python 3.13+
- **패키지 관리**: uv
- **TUI**: Rich ≥ 14.2.0
- **테스트**: pytest (`uv run pytest`)

## Governance

이 헌법은 프로젝트의 모든 기술적 결정의 기준이 된다. 변경 시 버전을 업데이트한다.

**Version**: 1.1.0 | **Ratified**: 2026-03-16 | **Last Amended**: 2026-03-23
