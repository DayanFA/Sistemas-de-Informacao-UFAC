import tkinter as tk

class SomaSimples(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Soma Simples")
        self.label_numero1 = tk.Label(self, text="Número 1:")
        self.label_numero1.grid(row=0, column=0)
        self.entry_numero1 = tk.Entry(self)
        self.entry_numero1.grid(row=0, column=1)
        self.label_numero2 = tk.Label(self, text="Número 2:")
        self.label_numero2.grid(row=1, column=0)
        self.entry_numero2 = tk.Entry(self)
        self.entry_numero2.grid(row=1, column=1)
        self.button_somar = tk.Button(self, text="Somar >>", command=self.somar)
        self.button_somar.grid(row=2, column=0, padx=5, pady=5)
        self.resultado = tk.Label(self, text="", bg="white", width=20, anchor="w")
        self.resultado.grid(row=2, column=1, padx=5, pady=5)

    def somar(self):
        try:
            numero1 = float(self.entry_numero1.get())
            numero2 = float(self.entry_numero2.get())
            resultado = numero1 + numero2
            self.resultado.config(text=f"{resultado}")
        except ValueError:
            self.resultado.config(text="Entrada inválida.")

class CalculadoraSimples(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora Simples")

        self.display = tk.Entry(self, width=30, borderwidth=5)
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        button_list = [
            "7", "8", "9", "+",
            "4", "5", "6", "-",
            "1", "2", "3", "*",
            "0", ".", "C", "/"
        ]

        row = 1
        col = 0

        for button_text in button_list:
            button = tk.Button(self, text=button_text, width=5)
            button.grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

        self.button_igual = tk.Button(self, text="=", fg="white", width=30, bg="green")
        self.button_igual.grid(row=5, column=0, columnspan=4, padx=5, pady=5)

class GerenciadorPack(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gerenciador Pack")

        self.frame_red = tk.Frame(self, bg="red", height=50)
        self.frame_red.pack(fill=tk.X)
        tk.Label(self.frame_red, text="Red", bg="red", fg="white").pack()

        self.frame_green = tk.Frame(self, bg="green", height=50)
        self.frame_green.pack(fill=tk.X)
        tk.Label(self.frame_green, text="Green", bg="green", fg="white").pack()

        self.frame_blue = tk.Frame(self, bg="blue", height=50)
        self.frame_blue.pack(fill=tk.X)
        tk.Label(self.frame_blue, text="Blue", bg="blue", fg="white").pack()

        self.frame_bottom = tk.Frame(self)
        self.frame_bottom.pack(fill=tk.BOTH, expand=True)

        self.frame_bottom.grid_rowconfigure(0, weight=1)
        self.frame_bottom.grid_rowconfigure(1, weight=1)
        self.frame_bottom.grid_columnconfigure(1, weight=1)
        self.frame_bottom.grid_columnconfigure(2, weight=1)
        self.frame_bottom.grid_columnconfigure(3, weight=1)

        self.frame_gray1 = tk.Frame(self.frame_bottom, bg="gray", width=50, height=50)
        self.frame_gray1.grid(row=0, column=0, rowspan=2, sticky="ns")
        tk.Label(self.frame_gray1, text="Gray", bg="gray", fg="white").pack()

        self.frame_cyan = tk.Frame(self.frame_bottom, bg="cyan", width=50, height=50)
        self.frame_cyan.grid(row=0, column=1, sticky="nsew")
        tk.Label(self.frame_cyan, text="Cyan", bg="cyan").pack()

        self.frame_magenta = tk.Frame(self.frame_bottom, bg="magenta", width=50, height=50)
        self.frame_magenta.grid(row=0, column=2, sticky="nsew")
        tk.Label(self.frame_magenta, text="Magenta", bg="magenta").pack()

        self.frame_yellow = tk.Frame(self.frame_bottom, bg="yellow", width=50, height=50)
        self.frame_yellow.grid(row=0, column=3, sticky="nsew")
        tk.Label(self.frame_yellow, text="Yellow", bg="yellow").pack()

        self.frame_black = tk.Frame(self.frame_bottom, bg="black", width=50, height=50)
        self.frame_black.grid(row=1, column=1, columnspan=3, sticky="nsew")
        tk.Label(self.frame_black, text="Black", bg="black", fg="white").pack()

        self.frame_gray2 = tk.Frame(self.frame_bottom, bg="gray", width=50, height=50)
        self.frame_gray2.grid(row=0, column=4, rowspan=2, sticky="ns")
        tk.Label(self.frame_gray2, text="Gray", bg="gray", fg="white").pack()


soma_simples = SomaSimples()
calculadora_simples = CalculadoraSimples()
gerenciador_pack = GerenciadorPack()
soma_simples.mainloop()
calculadora_simples.mainloop()
gerenciador_pack.mainloop()