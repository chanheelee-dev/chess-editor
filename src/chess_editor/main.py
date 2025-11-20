"""Main entry point for the chess board editor."""

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.layout import Layout
from rich.text import Text

from chess_editor.board import ChessBoard, Piece, PieceType, PieceColor


class ChessBoardRenderer:
    """Renders a chess board using Rich, supporting irregular board shapes."""

    LIGHT_SQUARE = "white"
    DARK_SQUARE = "bright_black"
    HOLE_SQUARE = "black"  # Color for holes (non-existent cells)

    def __init__(self, board: ChessBoard):
        self.board = board
        self.console = Console()

    def _get_column_labels(self, min_col: int, max_col: int) -> list[str]:
        """Generate column labels. Use a-z for 0-25, then numbers."""
        labels = []
        for col in range(min_col, max_col + 1):
            if 0 <= col <= 25:
                labels.append(chr(ord('a') + col))
            else:
                labels.append(str(col))
        return labels

    def render(self) -> Table:
        """Render the chess board as a Rich Table, supporting irregular shapes."""
        # Get board bounds
        min_row, max_row, min_col, max_col = self.board.get_bounds()

        # Handle empty board
        if not self.board.get_all_cells():
            table = Table(show_header=False)
            table.add_column("", justify="center")
            table.add_row("[dim]Empty board[/dim]")
            return table

        table = Table(
            show_header=True,
            show_edge=True,
            box=None,
            padding=(0, 1),
        )

        # Add column headers
        table.add_column("", justify="center", style="bold", width=3)
        col_labels = self._get_column_labels(min_col, max_col)
        for label in col_labels:
            table.add_column(label, justify="center", width=4)

        # Add rows
        for row in range(min_row, max_row + 1):
            row_cells = [str(row)]  # Row number

            for col in range(min_col, max_col + 1):
                if self.board.cell_exists(row, col):
                    # Cell exists - show piece or empty square
                    piece = self.board.get_piece(row, col)

                    # Determine square color (checkerboard pattern)
                    is_light = (row + col) % 2 == 0
                    bg_color = self.LIGHT_SQUARE if is_light else self.DARK_SQUARE

                    # Get piece symbol or empty space
                    symbol = str(piece) if piece else " "

                    # Create styled cell
                    cell = Text(symbol, style=f"on {bg_color}")
                else:
                    # Hole - cell doesn't exist
                    cell = Text("·", style=f"dim on {self.HOLE_SQUARE}")

                row_cells.append(cell)

            table.add_row(*row_cells)

        return table

    def display(self):
        """Display the chess board."""
        board_table = self.render()

        panel = Panel(
            board_table,
            title="[bold cyan]Chess Board Editor[/bold cyan]",
            subtitle="[dim]Press Ctrl+C to exit[/dim]",
            border_style="cyan",
        )

        self.console.print(panel)


def main():
    """Main function to run the chess board editor."""
    console = Console()

    console.print("\n[bold green]Welcome to Chess Board Editor![/bold green]\n")

    # Example 1: Standard 8x8 board
    console.print("[bold cyan]Example 1: Standard 8×8 Chess Board[/bold cyan]")
    board1 = ChessBoard()
    board1.setup_standard_position()
    renderer1 = ChessBoardRenderer(board1)
    renderer1.display()

    # Example 2: Irregular cross-shaped board
    console.print("\n[bold cyan]Example 2: Irregular Cross-Shaped Board[/bold cyan]")
    console.print("[dim]Note: '·' represents holes (non-existent cells)[/dim]\n")
    board2 = ChessBoard()
    board2.setup_irregular_example()
    renderer2 = ChessBoardRenderer(board2)
    renderer2.display()

    # Example 3: Custom irregular board
    console.print("\n[bold cyan]Example 3: Custom Irregular Board[/bold cyan]")
    console.print("[dim]A diagonal pattern with some pieces[/dim]\n")
    board3 = ChessBoard()
    # Create diagonal cells
    for i in range(7):
        board3.add_cell(i, i)
        board3.add_cell(i, i + 1)
        board3.add_cell(i + 1, i)
    # Add some pieces
    board3.set_piece(0, 0, Piece(PieceType.KING, PieceColor.WHITE))
    board3.set_piece(3, 3, Piece(PieceType.QUEEN, PieceColor.BLACK))
    board3.set_piece(6, 6, Piece(PieceType.KING, PieceColor.BLACK))
    renderer3 = ChessBoardRenderer(board3)
    renderer3.display()

    console.print("\n[dim]The board now supports irregular shapes with holes![/dim]")
    console.print("[dim]Future features: interactive editing, save/load, custom positions[/dim]\n")


if __name__ == "__main__":
    main()
