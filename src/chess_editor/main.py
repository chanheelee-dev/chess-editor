"""Main entry point for the chess board editor."""

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.layout import Layout
from rich.text import Text

from chess_editor.board import ChessBoard, Piece, PieceType, PieceColor


class ChessBoardRenderer:
    """Renders a chess board using Rich."""

    LIGHT_SQUARE = "white"
    DARK_SQUARE = "bright_black"

    def __init__(self, board: ChessBoard):
        self.board = board
        self.console = Console()

    def render(self) -> Table:
        """Render the chess board as a Rich Table."""
        table = Table(
            show_header=True,
            show_edge=True,
            box=None,
            padding=(0, 1),
        )

        # Add column headers (a-h)
        table.add_column("", justify="center", style="bold", width=3)
        for col in "abcdefgh":
            table.add_column(col, justify="center", width=4)

        # Add rows (8-1)
        for row in range(8):
            row_cells = [str(8 - row)]  # Row number

            for col in range(8):
                piece = self.board.get_piece(row, col)

                # Determine square color (checkerboard pattern)
                is_light = (row + col) % 2 == 0
                bg_color = self.LIGHT_SQUARE if is_light else self.DARK_SQUARE

                # Get piece symbol or empty space
                symbol = str(piece) if piece else " "

                # Create styled cell
                cell = Text(symbol, style=f"on {bg_color}")
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

    # Create a board with standard starting position
    board = ChessBoard()
    board.setup_standard_position()

    # Render and display
    renderer = ChessBoardRenderer(board)

    console.print("\n[bold green]Welcome to Chess Board Editor![/bold green]\n")
    renderer.display()

    console.print("\n[dim]This is a basic rendering demo.[/dim]")
    console.print("[dim]Future features: interactive editing, save/load, custom positions[/dim]\n")


if __name__ == "__main__":
    main()
