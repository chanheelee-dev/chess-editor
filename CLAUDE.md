# CLAUDE.md - Chess Editor Project Guide

> **AI Assistant Reference**: This document provides comprehensive guidance for AI assistants working with the chess-editor codebase.

## Project Overview

**Chess Editor** is a terminal-based chess board editor for creating custom chess positions. The project is in early development, currently supporting visualization of standard chess positions with plans for interactive editing capabilities.

**Key Characteristics:**
- Written in Python 3.13+
- Uses `uv` for modern Python package management
- Rich library for beautiful terminal UI
- Clean, modular architecture
- Korean language support in documentation

## Codebase Structure

```
chess-editor/
├── src/
│   └── chess_editor/
│       ├── __init__.py         # Package init (hello() demo function)
│       ├── main.py             # Entry point & rendering logic
│       ├── board.py            # Chess board model & piece definitions
│       └── utils/              # Utility modules (currently empty)
│           └── __init__.py
├── pyproject.toml              # Project configuration & dependencies
├── uv.lock                     # Locked dependencies
├── .python-version             # Python version (3.13)
├── .gitignore                  # Git ignore rules
└── README.md                   # Project documentation (Korean)
```

**Note:** The following directories are planned but not yet created:
- `tests/` - Test files
- `data/` - Saved board files
- `examples/` - Example board configurations

## Architecture

### Component Breakdown

#### 1. **board.py** - Core Domain Model
```
Location: src/chess_editor/board.py

Key Classes:
- PieceColor(Enum): WHITE, BLACK
- PieceType(Enum): KING, QUEEN, ROOK, BISHOP, KNIGHT, PAWN
- Piece: Represents individual chess pieces with Unicode symbols
- ChessBoard: 8x8 board representation with position management
```

**ChessBoard API:**
- `get_piece(row, col)` - Retrieve piece at position
- `set_piece(row, col, piece)` - Place/remove piece
- `clear()` - Empty the board
- `setup_standard_position()` - Set up standard chess starting position

**Coordinate System:**
- Internal: 0-indexed rows and columns (row 0 = rank 8, row 7 = rank 1)
- Display: Standard chess notation (a-h for files, 1-8 for ranks)

#### 2. **main.py** - Rendering & Application Entry

```
Location: src/chess_editor/main.py

Key Classes:
- ChessBoardRenderer: Converts ChessBoard to Rich Table visualization
  - render() → Table: Creates Rich table representation
  - display() → void: Shows board in panel with title/subtitle

Entry Points:
- main(): Application entry point (referenced in pyproject.toml)
- Command: uv run chess-editor
```

**Rendering Details:**
- Checkerboard pattern: (row + col) % 2 == 0 determines light squares
- Light squares: white background
- Dark squares: bright_black background
- Unicode chess symbols from Piece class

#### 3. **__init__.py** - Package Interface

Currently contains a simple `hello()` function for testing. Will likely be extended for package-level exports.

## Technology Stack

### Core Dependencies

| Tool | Version | Purpose |
|------|---------|---------|
| Python | 3.13+ | Programming language |
| uv | latest | Fast Python package manager (replaces pip/poetry) |
| Rich | >=14.2.0 | Terminal UI rendering library |

### Package Management with uv

**Why uv?**
- Extremely fast dependency resolution
- Built-in virtual environment management
- Compatible with pip/PyPI ecosystem
- Modern alternative to pip/poetry/conda

**Common Commands:**
```bash
uv sync              # Install/sync dependencies
uv add <package>     # Add new dependency
uv remove <package>  # Remove dependency
uv run <command>     # Run command in project environment
uv pip list          # List installed packages
```

### Build System

- Build backend: `uv_build` (version 0.8.17-0.9.0)
- Entry point: Defined in `[project.scripts]` section
- Command: `chess-editor` → `chess_editor.main:main`

## Development Workflows

### Initial Setup

```bash
# Clone repository
git clone <repository-url>
cd chess-editor

# Verify Python version
cat .python-version  # Should be 3.13

# Install dependencies
uv sync

# Run application
uv run chess-editor
```

### Running the Application

```bash
# Standard run
uv run chess-editor

# Direct Python execution
uv run python -m chess_editor.main
```

### Adding Dependencies

```bash
# Add runtime dependency
uv add <package-name>

# Add development dependency
uv add --dev <package-name>

# Example: Add pytest for testing
uv add --dev pytest
```

### Testing (Future)

Currently no tests exist. When implementing:

```bash
# Add pytest
uv add --dev pytest pytest-cov

# Create tests/ directory
mkdir tests

# Run tests
uv run pytest

# With coverage
uv run pytest --cov=chess_editor
```

## Code Conventions

### Python Style

**Style Guide:** Follow PEP 8 conventions

**Key Patterns Observed:**
1. **Type Hints:** Comprehensive use of type annotations
   ```python
   def get_piece(self, row: int, col: int) -> Optional[Piece]:
   ```

2. **Docstrings:** Module and class-level docstrings in triple quotes
   ```python
   """Represents a chess piece."""
   ```

3. **Enums:** Use Enum for constants (PieceColor, PieceType)

4. **Private vs Public:**
   - Public: Regular naming (e.g., `board`, `render()`)
   - Constants: UPPER_CASE (e.g., `SYMBOLS`, `LIGHT_SQUARE`)

### Naming Conventions

| Type | Convention | Example |
|------|------------|---------|
| Classes | PascalCase | `ChessBoard`, `ChessBoardRenderer` |
| Functions/Methods | snake_case | `get_piece()`, `setup_standard_position()` |
| Variables | snake_case | `piece_type`, `row_cells` |
| Constants | UPPER_SNAKE | `LIGHT_SQUARE`, `DARK_SQUARE` |
| Private | Leading underscore | `_internal_method()` |

### Import Organization

Order observed in codebase:
1. Standard library imports
2. Third-party imports (Rich)
3. Local imports (chess_editor modules)

Example from main.py:
```python
# Rich imports
from rich.console import Console
from rich.table import Table
# ... more Rich imports

# Local imports
from chess_editor.board import ChessBoard, Piece, PieceType, PieceColor
```

### File Organization

Each module follows this structure:
1. Module docstring
2. Imports
3. Constants/Enums
4. Classes
5. Functions
6. `if __name__ == "__main__":` block (if applicable)

## Key Components Deep Dive

### Chess Piece Representation

**Unicode Symbols:** The project uses Unicode chess symbols for visual representation:

```python
SYMBOLS = {
    (PieceColor.WHITE, PieceType.KING): "♔",
    (PieceColor.WHITE, PieceType.QUEEN): "♕",
    # ... etc
}
```

**Design Decision:** Symbols are stored as class-level dictionary for O(1) lookup.

### Board Coordinate System

**Important:** The board uses zero-indexed coordinates internally:

- Row 0 = Rank 8 (Black's back rank)
- Row 7 = Rank 1 (White's back rank)
- Col 0 = File 'a'
- Col 7 = File 'h'

**Converting Chess Notation:**
```python
# Chess notation "e4" to internal coordinates:
# 'e' = column 4 (0-indexed)
# '4' = row 4 (rank 4 → 8-4 = row 4)

# Internal (row=4, col=4) to chess notation:
# col 4 → 'e'
# row 4 → rank '4' (8-4 = 4)
```

### Rendering Pipeline

```
ChessBoard → ChessBoardRenderer.render() → Rich Table → Panel → Console Output
```

1. **ChessBoard:** Holds piece positions
2. **render():** Converts to Rich Table with styling
3. **display():** Wraps table in Panel with title/borders
4. **Console:** Outputs to terminal

## Planned Features

From README.md, the following features are planned:

- [ ] Keyboard interaction (arrow key navigation)
- [ ] Piece placement/removal functionality
- [ ] FEN format support (standard chess position notation)
- [ ] Board save/load functionality
- [ ] Custom position templates
- [ ] Chess puzzle creation support

**Priority Areas for Development:**
1. Interactive editing (keyboard input handling)
2. FEN notation support (industry standard)
3. Persistence layer (save/load)

## Working with This Codebase - AI Assistant Guidelines

### Before Making Changes

1. **Read the current state:** Always read files before editing
2. **Understand the architecture:** This is a modular, clean separation between model (board.py) and view (main.py)
3. **Check dependencies:** Review pyproject.toml for current dependencies
4. **Consider the roadmap:** Align changes with planned features in README.md

### When Adding Features

#### DO:
- Maintain separation of concerns (model vs. view)
- Add type hints to all functions
- Include docstrings for new classes/functions
- Use Enums for constants and state
- Follow existing code style
- Update README.md if adding user-facing features
- Use `uv add` for new dependencies

#### DON'T:
- Mix rendering logic with board logic
- Hard-code values that should be configurable
- Add dependencies without justification
- Break the existing API (get_piece, set_piece, etc.)
- Ignore Python 3.13+ features when beneficial

### Testing Strategy

When implementing tests:
1. **Unit tests** for ChessBoard methods (board.py)
2. **Unit tests** for Piece class behavior
3. **Integration tests** for rendering pipeline
4. **Property-based tests** for board invariants (8x8, valid positions)

### Common Tasks

#### Adding a New Piece Type (Hypothetical)

```python
# 1. Update PieceType enum in board.py
class PieceType(Enum):
    # ... existing types ...
    ARCHBISHOP = "archbishop"  # Example fairy chess piece

# 2. Add symbol to Piece.SYMBOLS
SYMBOLS = {
    # ... existing symbols ...
    (PieceColor.WHITE, PieceType.ARCHBISHOP): "🨬",
    (PieceColor.BLACK, PieceType.ARCHBISHOP): "🨭",
}
```

#### Implementing FEN Support

FEN (Forsyth-Edwards Notation) is critical for chess applications:

```python
# Add to ChessBoard class:
def from_fen(self, fen_string: str) -> None:
    """Load position from FEN notation."""
    # Implementation needed

def to_fen(self) -> str:
    """Export position to FEN notation."""
    # Implementation needed
```

**Resources:**
- FEN Spec: https://en.wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation

#### Adding Interactive Controls

Will likely require:
1. Event handling library (Rich supports keyboard input)
2. Cursor position tracking
3. State management for selected piece
4. Command pattern for undo/redo

### Git Workflow

**Current Branch:** `claude/claude-md-mi3wxp5zwfsl8s0q-0164K3npc1cKWFXZs9kuoSSh`

**Important Git Rules:**
- ALWAYS develop on the specified Claude branch
- Use clear, descriptive commit messages
- Push with `-u origin <branch-name>` flag
- Branch names must start with `claude/` and match session ID
- Retry network failures up to 4 times with exponential backoff (2s, 4s, 8s, 16s)

**Commit Message Format:**
```
<type>: <description>

Examples:
feat: Add FEN notation support
fix: Correct board coordinate conversion
refactor: Simplify piece rendering logic
docs: Update README with new features
test: Add ChessBoard unit tests
```

### Language Considerations

**Documentation Language:**
- README.md is in Korean
- Code comments and docstrings are in English
- When updating README.md, maintain Korean language
- For new features, add both Korean (README.md) and English (CLAUDE.md) documentation

### Dependencies Management

**Adding Dependencies:**
```bash
# Runtime dependency
uv add chess  # Example: python-chess library for move validation

# Development dependency
uv add --dev black  # Example: code formatter
```

**Dependency Guidelines:**
- Prefer pure Python libraries (easier to package)
- Check Python 3.13 compatibility
- Consider package size and maintenance status
- Document why each dependency is needed

### Performance Considerations

**Current Scale:** Single board (8x8 = 64 squares)
- Performance is not critical yet
- Prioritize code clarity over optimization

**Future Considerations:**
- Multiple boards (puzzle collections)
- Animation rendering
- Large file I/O (position databases)

### Security Considerations

**Current Risk Level:** Low (local CLI application)

**Best Practices:**
- Validate file paths for save/load features
- Sanitize FEN input to prevent injection
- Be cautious with `eval()` or `exec()` (avoid if possible)
- Validate board coordinates (already implemented)

## File Locations Quick Reference

| Component | File Path | Purpose |
|-----------|-----------|---------|
| Board Model | `src/chess_editor/board.py` | Chess logic & piece definitions |
| Renderer | `src/chess_editor/main.py` | Terminal UI & entry point |
| Package Config | `pyproject.toml` | Dependencies & metadata |
| Init | `src/chess_editor/__init__.py` | Package exports |
| Utils | `src/chess_editor/utils/` | Utility functions (empty) |
| Docs | `README.md` | User documentation (Korean) |
| Version | `.python-version` | Python 3.13 |

## Useful Commands Reference

```bash
# Development
uv sync                          # Sync dependencies
uv run chess-editor              # Run application
uv add <package>                 # Add dependency
uv remove <package>              # Remove dependency
uv pip list                      # List installed packages

# Code Quality (after setup)
uv run black src/                # Format code
uv run ruff check src/           # Lint code
uv run mypy src/                 # Type check

# Testing (after setup)
uv run pytest                    # Run tests
uv run pytest --cov=chess_editor # With coverage
uv run pytest -v                 # Verbose output

# Git
git status                       # Check status
git add .                        # Stage changes
git commit -m "feat: description" # Commit
git push -u origin <branch>      # Push changes
```

## Additional Resources

**Python 3.13 Features:**
- PEP 701: Syntax for f-strings improvements
- PEP 709: Comprehension optimizations
- Better error messages

**Rich Library Documentation:**
- Official Docs: https://rich.readthedocs.io/
- Console API: https://rich.readthedocs.io/en/latest/console.html
- Tables: https://rich.readthedocs.io/en/latest/tables.html

**Chess Programming:**
- Chess notation: https://en.wikipedia.org/wiki/Algebraic_notation_(chess)
- FEN: https://en.wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation
- PGN: https://en.wikipedia.org/wiki/Portable_Game_Notation

## Changelog

**Current Version:** 0.1.0 (Initial Development)

### Recent Commits
- `e2a1abd` - Set up Python project with chess board editor
- `5139e09` - Python 버전을 3.13으로 업그레이드 및 불필요한 파일 제거
- `9ba89e2` - 체스 에디터 프로젝트 초기 세팅
- `a5c3d5b` - Initial commit

---

**Last Updated:** 2025-11-18
**Project Status:** Early Development (Demo Phase)
**Python Version:** 3.13
**License:** MIT
