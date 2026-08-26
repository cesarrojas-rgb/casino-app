# modules/slots.py
import tkinter as tk
from config import COLOR_CARD, COLOR_GOLD, COLOR_TEXT, FONT_TITLE, FONT_MAIN

class SlotsView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=COLOR_CARD, bd=2, relief="ridge")
        self.create_widgets()

    def create_widgets(self):
        # Título del juego
        lbl_title = tk.Label(
            self, text="🎰 Máquina Tragamonedas", 
            font=FONT_TITLE, bg=COLOR_CARD, fg=COLOR_GOLD
        )
        lbl_title.pack(pady=10)

        # Contenedor de carretes (UI)
        reels_frame = tk.Frame(self, bg=COLOR_CARD)
        reels_frame.pack(pady=20)

        self.reels = []
        for i in range(3):
            lbl_symbol = tk.Label(
                reels_frame, text="❓", font=("Helvetica", 36),
                bg="#000000", fg=COLOR_TEXT, width=4, height=2, relief="sunken"
            )
            lbl_symbol.pack(side="left", padx=10)
            self.reels.append(lbl_symbol)

        # Botón para jugar
        btn_spin = tk.Button(
            self, text="¡Girar!", font=FONT_MAIN,
            bg=COLOR_GOLD, fg="#000000", activebackground="#b89628",
            padx=20, pady=5, cursor="hand2"
        )
        btn_spin.pack(pady=10)