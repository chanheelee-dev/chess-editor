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
    """Represents a chess board with customizable piece positions."""

    def __init__(self):
        # 8x8 board, None represents empty square
        self.board: list[list[Optional[Piece]]] = [[None for _ in range(8)] for _ in range(8)]

    def get_piece(self, row: int, col: int) -> Optional[Piece]:
        """Get piece at position (row, col)."""
        if 0 <= row < 8 and 0 <= col < 8:
            return self.board[row][col]
        return None

    def set_piece(self, row: int, col: int, piece: Optional[Piece]) -> bool:
        """Set piece at position (row, col). Returns True if successful."""
        if 0 <= row < 8 and 0 <= col < 8:
            self.board[row][col] = piece
            return True
        return False

    def clear(self):
        """Clear the entire board."""
        self.board = [[None for _ in range(8)] for _ in range(8)]

    def setup_standard_position(self):
        """Set up standard chess starting position."""
        self.clear()

        # Black pieces (row 0, 1)
        back_row = [
            PieceType.ROOK, PieceType.KNIGHT, PieceType.BISHOP, PieceType.QUEEN,
            PieceType.KING, PieceType.BISHOP, PieceType.KNIGHT, PieceType.ROOK
        ]
        for col, piece_type in enumerate(back_row):
            self.board[0][col] = Piece(piece_type, PieceColor.BLACK)
            self.board[1][col] = Piece(PieceType.PAWN, PieceColor.BLACK)

        # White pieces (row 6, 7)
        for col, piece_type in enumerate(back_row):
            self.board[7][col] = Piece(piece_type, PieceColor.WHITE)
            self.board[6][col] = Piece(PieceType.PAWN, PieceColor.WHITE)
