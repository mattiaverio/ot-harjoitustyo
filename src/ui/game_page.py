
import tkinter as tk
from tkinter import messagebox
import chess
from services.chess_core import ChessGame

# UI constants
SQUARE_SIZE = 72
LIGHT_COLOR = "#F0D9B5"
DARK_COLOR = "#B58863"
SEL_COLOR = "#EEDD82"
LAST_COLOR = "#B6CE4B"
DOT_COLOR = "#3A7D44"

UNICODE_PIECES = {
    chess.PAWN: ("\u2659", "\u265f"),
    chess.KNIGHT: ("\u2658", "\u265e"),
    chess.BISHOP: ("\u2657", "\u265d"),
    chess.ROOK: ("\u2656", "\u265c"),
    chess.QUEEN: ("\u2655", "\u265b"),
    chess.KING: ("\u2654", "\u265a"),
}


def piece_to_unicode(piece_type, is_white):
    w, b = UNICODE_PIECES[piece_type]
    return w if is_white else b


class GamePage(tk.Frame):
    def __init__(self, master, ui):
        super().__init__(master)
        self.ui = ui
        self.game = ChessGame()

        # Initialize UI state
        self._init_state()
        self._build_toolbar()
        self._build_canvas()
        self._build_status_bar()
        self._bind_events()

        # Initial render
        self.redraw()
        self.update_status()

    # ---------- Initialization helpers ----------
    def _init_state(self):
        self.flipped = False
        self.selected_sq = None

    def _build_toolbar(self):
        top = tk.Frame(self)
        top.pack(padx=8, pady=6, anchor="w")
        tk.Button(top, text="Restart Game", command=self.on_new).pack(
            side="left", padx=(0, 6))
        tk.Button(top, text="Flip board", command=self.on_flip).pack(
            side="left", padx=(0, 12))
        tk.Button(top, text="Back", command=self.ui.show_menu).pack(side="left")

    def _build_canvas(self):
        size = SQUARE_SIZE * 8
        self.canvas = tk.Canvas(
            self, width=size, height=size, highlightthickness=0)
        self.canvas.pack(padx=8, pady=6)

    def _build_status_bar(self):
        self.status = tk.StringVar()
        tk.Label(self, textvariable=self.status, anchor="w").pack(
            fill="x", padx=8, pady=(0, 8))

    def _bind_events(self):
        self.canvas.bind("<Button-1>", self.on_click)
        self.canvas.bind("<Button-3>", self.on_cancel)

    def on_new(self):
        self.game.reset()
        self.clear_selection()
        self.redraw()
        self.update_status()

    def on_flip(self):
        self.flipped = not self.flipped
        self.redraw()

    def on_click(self, event):
        sq = self._pixel_to_square(event.x, event.y)
        if sq is None:
            return

        if self.selected_sq is None:
            self._try_select_piece(sq)
            return

        if self.game.is_square_own(sq):
            self.select_square(sq)
            return

        self._attempt_move(sq)

    def _try_select_piece(self, sq):

        if self.game.is_square_own(sq):
            self.select_square(sq)
        else:
            self.clear_selection()

    def _attempt_move(self, target_sq):
        result = self.game.move_or_prompt(
            self.selected_sq, target_sq, prompt_callback=self._prompt_promotion)
        if not result.ok:
            self.clear_selection()
            return
        self._finalize_move()

    def _finalize_move(self):
        self.clear_selection()
        self.redraw()
        self.update_status()

        if self.game.state.is_game_over and self.game.state.result:
            messagebox.showinfo(
                "Game Over", f"Result: {self.game.state.result}")

    def on_cancel(self):
        self.clear_selection()
        self.redraw()

    def redraw(self):
        self.canvas.delete("all")
        self._draw_board()
        self._draw_pieces()
        self._draw_legal_moves()

    def _draw_board(self):
        for rank in range(8):
            for file in range(8):
                sq = chess.square(file, rank)
                x, y = self._square_to_xy(file, rank)
                color = self._get_square_color(sq, file, rank)
                self.canvas.create_rectangle(
                    x, y, x + SQUARE_SIZE, y + SQUARE_SIZE, fill=color, outline=color)

    def _get_square_color(self, sq, file, rank):
        base = LIGHT_COLOR if (file + rank) % 2 == 0 else DARK_COLOR
        if self.game.state.last_move and sq in (self.game.state.last_move.from_square, self.game.state.last_move.to_square):
            return LAST_COLOR
        if self.selected_sq == sq:
            return SEL_COLOR
        return base

    def _draw_pieces(self):
        for sq, piece_type, is_white in self.game.pieces():
            file = chess.square_file(sq)
            rank = chess.square_rank(sq)
            x, y = self._square_to_xy(file, rank)
            self.canvas.create_text(
                x + SQUARE_SIZE / 2,
                y + SQUARE_SIZE / 2,
                text=piece_to_unicode(piece_type, is_white),
                font=("DejaVu Sans", int(SQUARE_SIZE * 0.55))
            )

    def _draw_legal_moves(self):
        r = SQUARE_SIZE * 0.12
        for t in self.game.legal_targets_from(self.selected_sq):
            f = chess.square_file(t)
            rnk = chess.square_rank(t)
            x, y = self._square_to_xy(f, rnk)
            cx, cy = x + SQUARE_SIZE / 2, y + SQUARE_SIZE / 2
            self.canvas.create_oval(
                cx - r, cy - r, cx + r, cy + r, fill=DOT_COLOR, outline="")

    def update_status(self):
        if self.game.state.is_game_over:
            self.status.set(f"Game over • {self.game.state.result or ''}")
        else:
            side = "White" if self.game.state.turn_white else "Black"
            text = f"{side} to move"
            if self.game.state.is_check:
                text += " • Check!"
            self.status.set(text)

    def select_square(self, sq):
        self.selected_sq = sq
        self.redraw()

    def clear_selection(self):
        self.selected_sq = None
        self.redraw()

    def _square_to_xy(self, file_idx, rank_idx):
        if self.flipped:
            df = 7 - file_idx
            dr = rank_idx
        else:
            df = file_idx
            dr = 7 - rank_idx
        return df * SQUARE_SIZE, dr * SQUARE_SIZE

    def _pixel_to_square(self, x, y):
        if not (0 <= x < SQUARE_SIZE * 8 and 0 <= y < SQUARE_SIZE * 8):
            return None
        df = x // SQUARE_SIZE
        dr = y // SQUARE_SIZE
        if self.flipped:
            file_idx = 7 - int(df)
            rank_idx = int(dr)
        else:
            file_idx = int(df)
            rank_idx = 7 - int(dr)
        return chess.square(file_idx, rank_idx)

    def _prompt_promotion(self, allowed):
        if not allowed:
            return None

        top = tk.Toplevel(self)
        top.title("Promote to")
        top.transient(self)

        choice = {"val": None}

        def set_choice(pt):
            choice["val"] = pt
            top.destroy()

        frame = tk.Frame(top, padx=12, pady=12)
        frame.pack()

        mapping = [
            (chess.QUEEN, "Queen"),
            (chess.ROOK, "Rook"),
            (chess.BISHOP, "Bishop"),
            (chess.KNIGHT, "Knight"),
        ]

        row, col = 0, 0
        for pt, label in mapping:
            if pt in allowed:
                symbol = UNICODE_PIECES[pt][0] if self.game.state.turn_white else UNICODE_PIECES[pt][1]
                btn = tk.Button(frame, text=f"{symbol} {label}", width=10,
                                command=lambda p=pt: set_choice(p))
                btn.grid(row=row, column=col, padx=6, pady=6)
                col += 1
                if col > 1:
                    col = 0
                    row += 1

        top.update_idletasks()
        top.grab_set()
        self.wait_window(top)
        return choice["val"]
