import chess
from chess_core import ChessGame

UNICODE_PIECES = {
    chess.PAWN:   ("♙", "♟"),
    chess.KNIGHT: ("♘", "♞"),
    chess.BISHOP: ("♗", "♝"),
    chess.ROOK:   ("♖", "♜"),
    chess.QUEEN:  ("♕", "♛"),
    chess.KING:   ("♔", "♚"),
}

def glyph(piece_type, is_white):
    w, b = UNICODE_PIECES[piece_type]
    return w if is_white else b

def render_board(game: ChessGame):
    grid = [["." for _ in range(8)] for _ in range(8)]

    for sq, piece_type, is_white in game.pieces():
        f = chess.square_file(sq)
        r = chess.square_rank(sq)
        pr = 7 - r
        pc = f
        grid[pr][pc] = glyph(piece_type, is_white)

    for row in grid:
        print(" ".join(row))

def main():
    game = ChessGame()

    print("Move with SAN notation. Type 'quit' to exit.")
    while True:
        render_board(game)
        st = game.get_state()
        if st.is_game_over:
            print("Game over:", st.result or "")
            break
        side = "White" if st.turn_white else "Black"
        status = side + " to move"
        print(status)

        try:
            move_txt = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if not move_txt:
            continue
        if move_txt.lower() == "quit":
            break

        res = game.move_by_san(move_txt)
        if not res.ok:
            print("Invalid move:", res.reason or "")

    print("Bye!")

if __name__ == "__main__":
    main()