"""Chess board model and piece definitions."""

from enum import Enum
from typing import Optional


class PieceColor(Enum):
    """Chess piece colors."""
    WHITE = "white"
    BLACK = "black"


class PieceType(Enum):
    """Chess piece types."""
    KING = "king"
    QUEEN = "queen"
    ROOK = "rook"
    BISHOP = "bishop"
    KNIGHT = "knight"
    PAWN = "pawn"


class Piece:
    """Represents a chess piece."""

    # Unicode chess pieces
    SYMBOLS = {
        (PieceColor.WHITE, PieceType.KING): "♔",
        (PieceColor.WHITE, PieceType.QUEEN): "♕",
        (PieceColor.WHITE, PieceType.ROOK): "♖",
        (PieceColor.WHITE, PieceType.BISHOP): "♗",
        (PieceColor.WHITE, PieceType.KNIGHT): "♘",
        (PieceColor.WHITE, PieceType.PAWN): "♙",
        (PieceColor.BLACK, PieceType.KING): "♚",
        (PieceColor.BLACK, PieceType.QUEEN): "♛",
        (PieceColor.BLACK, PieceType.ROOK): "♜",
        (PieceColor.BLACK, PieceType.BISHOP): "♝",
        (PieceColor.BLACK, PieceType.KNIGHT): "♞",
        (PieceColor.BLACK, PieceType.PAWN): "♟",
    }

    def __init__(self, piece_type: PieceType, color: PieceColor):
        self.piece_type = piece_type
        self.color = color

    def __str__(self) -> str:
        return self.SYMBOLS[(self.color, self.piece_type)]

    def __repr__(self) -> str:
        return f"Piece({self.piece_type.value}, {self.color.value})"


class ChessBoard:
    """Represents an irregular chess board with customizable piece positions and shape.

    The board can have any shape - not limited to 8x8. Cells can exist at any coordinate,
    and there can be holes (missing cells) anywhere on the board.

    Representation:
    - Dictionary maps (row, col) coordinates to cell states
    - If coordinate exists in dict: cell exists (value is None for empty, Piece for occupied)
    - If coordinate not in dict: hole (cell doesn't exist)
    """

    def __init__(self):
        # Dictionary-based board: {(row, col): Optional[Piece]}
        # If (row, col) is in dict: cell exists (None = empty, Piece = occupied)
        # If (row, col) not in dict: hole (cell doesn't exist)
        self.board: dict[tuple[int, int], Optional[Piece]] = {}

    def cell_exists(self, row: int, col: int) -> bool:
        """Check if a cell exists at the given position."""
        return (row, col) in self.board

    def add_cell(self, row: int, col: int) -> bool:
        """Add a cell at the given position. Returns True if added, False if already exists."""
        if not self.cell_exists(row, col):
            self.board[(row, col)] = None
            return True
        return False

    def remove_cell(self, row: int, col: int) -> bool:
        """Remove a cell (create a hole) at the given position. Returns True if removed."""
        if self.cell_exists(row, col):
            del self.board[(row, col)]
            return True
        return False

    def get_piece(self, row: int, col: int) -> Optional[Piece]:
        """Get piece at position (row, col). Returns None if cell is empty or doesn't exist."""
        return self.board.get((row, col))

    def set_piece(self, row: int, col: int, piece: Optional[Piece]) -> bool:
        """Set piece at position (row, col). Returns True if successful, False if cell doesn't exist."""
        if self.cell_exists(row, col):
            self.board[(row, col)] = piece
            return True
        return False

    def get_bounds(self) -> tuple[int, int, int, int]:
        """Get the bounding box of the board: (min_row, max_row, min_col, max_col).
        Returns (0, 0, 0, 0) if board is empty."""
        if not self.board:
            return (0, 0, 0, 0)

        rows = [pos[0] for pos in self.board.keys()]
        cols = [pos[1] for pos in self.board.keys()]
        return (min(rows), max(rows), min(cols), max(cols))

    def get_all_cells(self) -> list[tuple[int, int]]:
        """Get all cell coordinates that exist on the board."""
        return list(self.board.keys())

    def clear(self):
        """Clear the entire board (removes all cells)."""
        self.board = {}

    def setup_standard_position(self):
        """Set up standard 8x8 chess starting position."""
        self.clear()

        # Create 8x8 board
        for row in range(8):
            for col in range(8):
                self.board[(row, col)] = None

        # Black pieces (row 0, 1)
        back_row = [
            PieceType.ROOK, PieceType.KNIGHT, PieceType.BISHOP, PieceType.QUEEN,
            PieceType.KING, PieceType.BISHOP, PieceType.KNIGHT, PieceType.ROOK
        ]
        for col, piece_type in enumerate(back_row):
            self.board[(0, col)] = Piece(piece_type, PieceColor.BLACK)
            self.board[(1, col)] = Piece(PieceType.PAWN, PieceColor.BLACK)

        # White pieces (row 6, 7)
        for col, piece_type in enumerate(back_row):
            self.board[(7, col)] = Piece(piece_type, PieceColor.WHITE)
            self.board[(6, col)] = Piece(PieceType.PAWN, PieceColor.WHITE)

    def setup_irregular_example(self):
        """Set up an example irregular board with holes and non-standard shape."""
        self.clear()

        # Create a cross-shaped board (9x9 with holes in corners)
        for row in range(9):
            for col in range(9):
                # Skip corners to create cross shape
                if (row < 3 and col < 3) or (row < 3 and col > 5) or \
                   (row > 5 and col < 3) or (row > 5 and col > 5):
                    continue  # Create holes
                self.board[(row, col)] = None

        # Add some pieces
        self.board[(4, 4)] = Piece(PieceType.KING, PieceColor.WHITE)
        self.board[(0, 4)] = Piece(PieceType.QUEEN, PieceColor.BLACK)
        self.board[(8, 4)] = Piece(PieceType.QUEEN, PieceColor.WHITE)
        self.board[(4, 0)] = Piece(PieceType.ROOK, PieceColor.BLACK)
        self.board[(4, 8)] = Piece(PieceType.ROOK, PieceColor.WHITE)
