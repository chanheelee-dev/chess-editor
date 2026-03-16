"""Flask web server for the chess board editor."""

import os
from flask import Flask
from chess_editor.board import ChessBoard


def render_board_html(board: ChessBoard) -> str:
    """Render the chess board as an HTML page."""
    LIGHT = "#f0d9b5"
    DARK = "#b58863"
    LABEL_BG = "#1a1a1a"

    rows_html = ""
    for row in range(8):
        rank = str(8 - row)
        cells = f'<td style="background:{LABEL_BG};color:#ccc;font-size:0.9rem;padding:0 6px;text-align:center;">{rank}</td>'
        for col in range(8):
            piece = board.get_piece(row, col)
            symbol = str(piece) if piece else ""
            bg = LIGHT if (row + col) % 2 == 0 else DARK
            cells += (
                f'<td style="background:{bg};width:2.5rem;height:2.5rem;'
                f'text-align:center;font-size:2.2rem;line-height:2.5rem;">{symbol}</td>'
            )
        rows_html += f"<tr>{cells}</tr>"

    file_labels = "".join(
        f'<td style="background:{LABEL_BG};color:#ccc;font-size:0.9rem;'
        f'text-align:center;padding:4px 0;">{c}</td>'
        for c in " abcdefgh"
    )

    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Chess Board Editor</title>
  <style>
    body {{ margin: 0; background: #2b2b2b; display: flex; justify-content: center; align-items: center; min-height: 100vh; }}
    .board-wrap {{ max-width: 100vmin; width: 100%; padding: 1rem; box-sizing: border-box; }}
    h1 {{ color: #e0c97f; text-align: center; font-family: sans-serif; margin: 0 0 0.75rem; font-size: 1.2rem; }}
    table {{ border-collapse: collapse; width: 100%; }}
    td {{ padding: 0; }}
  </style>
</head>
<body>
  <div class="board-wrap">
    <h1>Chess Board Editor</h1>
    <table>
      {rows_html}
      <tr>{file_labels}</tr>
    </table>
  </div>
</body>
</html>"""


def create_app() -> Flask:
    """Create and configure the Flask application."""
    app = Flask(__name__)

    @app.route("/")
    def index():
        board = ChessBoard()
        board.setup_standard_position()
        return render_board_html(board), 200, {"Content-Type": "text/html; charset=utf-8"}

    return app


def run():
    """Run the Flask development server."""
    port = int(os.environ.get("PORT", 5000))
    app = create_app()
    app.run(host="0.0.0.0", port=port)
