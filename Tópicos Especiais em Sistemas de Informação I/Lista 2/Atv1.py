import tkinter as tk

class PackSimples(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pack Simples")
        self.topo = tk.Label(self, text="TOPO", bg="yellow", fg="black")
        self.esquerda = tk.Label(self, text="ESQUERDA", bg="red", fg="white")
        self.direita = tk.Label(self, text="DIREITA", bg="green", fg="white")
        self.rodape = tk.Label(self, text="RODAPÉ", bg="cyan", fg="black")

        self.topo.pack(fill=tk.X, ipady=15)
        self.rodape.pack(side=tk.BOTTOM, fill=tk.X, ipady=15)
        self.esquerda.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.direita.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

class GerenciadorGrid(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gerenciador Grid")
        self.button1 = tk.Button(self, text="1")
        self.button2 = tk.Button(self, text="2")
        self.button3 = tk.Button(self, text="3")
        self.button4 = tk.Button(self, text="4")
        self.button5 = tk.Button(self, text="5")
        self.button6 = tk.Button(self, text="6")
        self.button1.grid(row=0, column=2, sticky="nsew")
        self.button2.grid(row=1, column=1, sticky="nsew")
        self.button3.grid(row=1, column=3, sticky="nsew")
        self.button4.grid(row=2, column=0, sticky="nsew")
        self.button5.grid(row=2, column=2, sticky="nsew")
        self.button6.grid(row=2, column=4, sticky="nsew")


pack_simples = PackSimples()
gerenciador_grid = GerenciadorGrid()
pack_simples.mainloop()
gerenciador_grid.mainloop()