# modules/roulette.py
import tkinter as tk
from config import COLOR_CARD, COLOR_ACCENT, COLOR_GOLD, COLOR_TEXT, FONT_TITLE, FONT_MAIN

class RouletteView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=COLOR_CARD, bd=2, relief="ridge")
        self.create_widgets()

    def create_widgets(self):
        lbl_title = tk.Label(
            self, text="🎡 Ruleta de la Suerte", 
            font=FONT_TITLE, bg=COLOR_CARD, fg=COLOR_GOLD
        )
        lbl_title.pack(pady=10)

        # Simulación del tablero
        board_frame = tk.Frame(self, bg=COLOR_CARD)
        board_frame.pack(pady=10)

        btn_red = tk.Button(
            board_frame, text="Aposta a Rojo", bg=COLOR_ACCENT, 
            fg=COLOR_TEXT, font=FONT_MAIN, width=15, height=2
        )
        btn_red.pack(side="left", padx=10)

        btn_black = tk.Button(
            board_frame, text="Aposta a Negro", bg="#000000", 
            fg=COLOR_TEXT, font=FONT_MAIN, width=15, height=2
        )
        btn_black.pack(side="left", padx=10)