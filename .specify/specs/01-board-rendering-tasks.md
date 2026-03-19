# Tasks 01: 체스 보드 렌더링

**Status**: All Complete
**Plan**: 01-board-rendering-plan.md

---

## Phase 1: Setup

- [x] [T001] [US1] `pyproject.toml`에 rich 의존성 추가
- [x] [T002] [US1] `src/chess_editor/__init__.py` 생성

## Phase 2: Foundational

- [x] [T003] [P] [US1] `board.py` — `PieceColor`, `PieceType` Enum 정의
- [x] [T004] [P] [US1] `board.py` — `Piece` 클래스 + 유니코드 심볼 매핑 구현
- [x] [T005] [US1] `board.py` — `ChessBoard` 클래스 구현 (get/set/clear)
- [x] [T006] [US1] `board.py` — `setup_standard_position()` 구현

## Phase 3: User Stories

- [x] [T007] [P] [US1, US2] `main.py` — `ChessBoardRenderer.render()` 구현 (Rich Table, 체커보드 패턴)
- [x] [T008] [P] [US1] `main.py` — `ChessBoardRenderer.display()` 구현 (Rich Panel 래핑)
- [x] [T009] [US1] `main.py` — `main()` 엔트리포인트 구현

## Phase Final: Polish

- [x] [T010] [US1] `pyproject.toml` scripts에 `chess-editor` 커맨드 등록
