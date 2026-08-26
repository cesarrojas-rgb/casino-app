# main.py
import tkinter as tk
from config import COLOR_BG, COLOR_GOLD, COLOR_TEXT, FONT_TITLE
from modules.slots import SlotsView
from modules.roulette import RouletteView

class CasinoApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Casino App - TCL/TK UI")
        self.geometry("800x500")
        self.configure(bg=COLOR_BG)

        self.create_layout()

    def create_layout(self):
        # Encabezado
        header = tk.Frame(self, bg=COLOR_BG)
        header.pack(fill="x", pady=10, padx=20)
        
        lbl_brand = tk.Label(
            header, text="ROYAL CASINO", 
            font=FONT_TITLE, bg=COLOR_BG, fg=COLOR_GOLD
        )
        lbl_brand.pack(side="left")

        # Contenedor principal
        main_container = tk.Frame(self, bg=COLOR_BG)
        main_container.pack(fill="both", expand=True, padx=20, pady=10)

        # Instanciar las vistas de la UI
        self.slots_ui = SlotsView(main_container)
        self.slots_ui.pack(side="left", fill="both", expand=True, padx=5)

        self.roulette_ui = RouletteView(main_container)
        self.roulette_ui.pack(side="right", fill="both", expand=True, padx=5)

if __name__ == "__main__":
    app = CasinoApp()
    app.mainloop()