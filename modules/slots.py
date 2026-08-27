# modules/slots.py
import random
import tkinter as tk
from config import COLOR_CARD, COLOR_GOLD, COLOR_TEXT, FONT_TITLE, FONT_MAIN

class SlotsView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=COLOR_CARD, bd=3, relief="ridge")
        # Emojis simples para evitar recuadros raros en Windows
        self.symbols = ["🍒", "🍋", "🔔", "💎", "⭐", "🍇"]
        self.create_widgets()

    def create_widgets(self):
        lbl_title = tk.Label(
            self, text="🎰 Tragamonedas", 
            font=FONT_TITLE, bg=COLOR_CARD, fg=COLOR_GOLD
        )
        lbl_title.pack(pady=10)

        reels_frame = tk.Frame(self, bg=COLOR_CARD)
        reels_frame.pack(pady=15)

        self.reels = []
        for i in range(3):
            lbl_symbol = tk.Label(
                reels_frame, text="❓", font=("Segoe UI Emoji", 32),
                bg="#052110", fg=COLOR_TEXT, width=4, height=2, relief="sunken", bd=2
            )
            lbl_symbol.pack(side="left", padx=8)
            self.reels.append(lbl_symbol)

        btn_spin = tk.Button(
            self, text="¡GIRAR!", font=FONT_MAIN,
            bg=COLOR_GOLD, fg="#000000", activebackground="#e6c200",
            padx=20, pady=6, cursor="hand2", relief="raised", bd=3,
            command=self.spin
        )
        btn_spin.pack(pady=10)

        self.lbl_result = tk.Label(self, text="", font=FONT_MAIN, bg=COLOR_CARD, fg=COLOR_GOLD)
        self.lbl_result.pack(pady=5)

    def spin(self):
        results = [random.choice(self.symbols) for _ in range(3)]
        for i in range(3):
            self.reels[i].config(text=results[i])
        
        if results[0] == results[1] == results[2]:
            self.lbl_result.config(text="¡JACKPOT! 🎉", fg=COLOR_GOLD)
        else:
            self.lbl_result.config(text="¡Sigue intentando!", fg=COLOR_TEXT)