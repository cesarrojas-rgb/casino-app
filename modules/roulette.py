# modules/roulette.py
import random
import tkinter as tk
from config import COLOR_CARD, COLOR_ACCENT, COLOR_BLACK, COLOR_GOLD, COLOR_TEXT, FONT_TITLE, FONT_MAIN

class RouletteView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=COLOR_CARD, bd=3, relief="ridge")
        self.create_widgets()

    def create_widgets(self):
        lbl_title = tk.Label(
            self, text="🎡 Ruleta Real", 
            font=FONT_TITLE, bg=COLOR_CARD, fg=COLOR_GOLD
        )
        lbl_title.pack(pady=10)

        board_frame = tk.Frame(self, bg=COLOR_CARD)
        board_frame.pack(pady=15)

        btn_red = tk.Button(
            board_frame, text="Aposta a Rojo", bg=COLOR_ACCENT, 
            fg=COLOR_TEXT, font=FONT_MAIN, width=13, height=2,
            cursor="hand2", relief="raised", bd=3,
            command=lambda: self.play_roulette("Rojo")
        )
        btn_red.pack(side="left", padx=8)

        btn_black = tk.Button(
            board_frame, text="Aposta a Negro", bg=COLOR_BLACK, 
            fg=COLOR_TEXT, font=FONT_MAIN, width=13, height=2,
            cursor="hand2", relief="raised", bd=3,
            command=lambda: self.play_roulette("Negro")
        )
        btn_black.pack(side="left", padx=8)

        self.lbl_result = tk.Label(self, text="", font=FONT_MAIN, bg=COLOR_CARD, fg=COLOR_TEXT)
        self.lbl_result.pack(pady=15)

    def play_roulette(self, user_choice):
        winner = random.choice(["Rojo", "Negro"])
        if user_choice == winner:
            self.lbl_result.config(text=f"¡Salió {winner}! ¡Ganaste! 🏆", fg=COLOR_GOLD)
        else:
            self.lbl_result.config(text=f"Salió {winner}. Perdiste ❌", fg=COLOR_TEXT)