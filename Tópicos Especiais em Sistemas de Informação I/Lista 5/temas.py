import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb


class Tela:
    def __init__(self, master):
        self.app = master
        self.app.title("Widgets Legados do Tkinter com TTk Bootstrap")
        self.app.geometry("840x550")
        self.style = tb.Style("superhero")

        # Titulo
        self.frame_titulo = ttk.Frame(self.app, padding=10)
        self.frame_titulo.pack(fill="x")
        self.label_titulo = ttk.Label(self.frame_titulo, text="Superhero", font=("Helvetica", 24, "bold"))
        self.label_titulo.pack(anchor="w")

        # Tudo
        self.frame_principal = ttk.Labelframe(self.frame_titulo, text="Alguns widgets do tkinter", padding=5)
        self.frame_principal.pack(fill="both", expand=True)
        self.frame_widgets = ttk.Frame(self.frame_principal)
        self.frame_widgets.pack(fill="x")

        # Widget Label
        ttk.Label(self.frame_widgets, text="Widget Label").grid(row=0, column=0, padx=10, pady=5, sticky="EW")
        self.frame_widgets.columnconfigure(0, weight=2)
        self.frame_widgets.columnconfigure(1, weight=3)
        self.frame_widgets.columnconfigure(2, weight=1)
        ttk.Entry(self.frame_widgets).grid(row=1, column=0, padx=5, pady=5, sticky="EW")
        self.entry_widget = ttk.Entry(self.frame_widgets)
        self.entry_widget.grid(row=1, column=0, padx=5, pady=5, sticky="EW")
        self.entry_widget.insert(0, "Widget Entry")
        self.spinbox_widget = ttk.Spinbox(self.frame_widgets, from_=0, to=10, width=10)
        self.spinbox_widget.grid(row=1, column=1, padx=5, pady=5, sticky="EW")
        self.spinbox_widget.set("Spinbox")
        ttk.Button(self.frame_widgets, text="Button").grid(row=1, column=2, padx=5, pady=5, sticky="EW")

        # Temas
        self.tema_var = tk.StringVar(value="superhero")
        self.frame_temas = ttk.Labelframe(self.frame_principal, text="Temas do TTk Bootstrap", padding=10)
        self.frame_temas.pack(fill="x", pady=10)
        ttk.Radiobutton(self.frame_temas, text="morph", variable=self.tema_var, value="morph", command=self.mudar_tema).grid(row=0, column=0, padx=5, pady=5)
        ttk.Radiobutton(self.frame_temas, text="journal", variable=self.tema_var, value="journal", command=self.mudar_tema).grid(row=0, column=1, padx=5, pady=5)
        ttk.Radiobutton(self.frame_temas, text="darkly", variable=self.tema_var, value="darkly", command=self.mudar_tema).grid(row=0, column=2, padx=5, pady=5)
        ttk.Radiobutton(self.frame_temas, text="superhero", variable=self.tema_var, value="superhero", command=self.mudar_tema).grid(row=0, column=3, padx=5, pady=5)
        ttk.Radiobutton(self.frame_temas, text="solar", variable=self.tema_var, value="solar", command=self.mudar_tema).grid(row=0, column=4, padx=5, pady=5)
        ttk.Radiobutton(self.frame_temas, text="cyborg", variable=self.tema_var, value="cyborg", command=self.mudar_tema).grid(row=0, column=5, padx=5, pady=5)
        ttk.Radiobutton(self.frame_temas, text="vapor", variable=self.tema_var, value="vapor", command=self.mudar_tema).grid(row=0, column=6, padx=5, pady=5)
        ttk.Radiobutton(self.frame_temas, text="simplex", variable=self.tema_var, value="simplex", command=self.mudar_tema).grid(row=0, column=7, padx=5, pady=5)
        ttk.Radiobutton(self.frame_temas, text="cerculean", variable=self.tema_var, value="cerculean", command=self.mudar_tema).grid(row=0, column=8, padx=5, pady=5)
        ttk.Radiobutton(self.frame_temas, text="cosmo", variable=self.tema_var, value="cosmo", command=self.mudar_tema).grid(row=1, column=0, padx=5, pady=5)
        ttk.Radiobutton(self.frame_temas, text="flatly", variable=self.tema_var, value="flatly", command=self.mudar_tema).grid(row=1, column=1, padx=5, pady=5)
        ttk.Radiobutton(self.frame_temas, text="litera", variable=self.tema_var, value="litera", command=self.mudar_tema).grid(row=1, column=2, padx=5, pady=5)
        ttk.Radiobutton(self.frame_temas, text="minty", variable=self.tema_var, value="minty", command=self.mudar_tema).grid(row=1, column=3, padx=5, pady=5)
        ttk.Radiobutton(self.frame_temas, text="lumen", variable=self.tema_var, value="lumen", command=self.mudar_tema).grid(row=1, column=4, padx=5, pady=5)
        ttk.Radiobutton(self.frame_temas, text="sandstone", variable=self.tema_var, value="sandstone", command=self.mudar_tema).grid(row=1, column=5, padx=5, pady=5)
        ttk.Radiobutton(self.frame_temas, text="yeti", variable=self.tema_var, value="yeti", command=self.mudar_tema).grid(row=1, column=6, padx=5, pady=5)
        ttk.Radiobutton(self.frame_temas, text="pulse", variable=self.tema_var, value="pulse", command=self.mudar_tema).grid(row=1, column=7, padx=5, pady=5)
        ttk.Radiobutton(self.frame_temas, text="united", variable=self.tema_var, value="united", command=self.mudar_tema).grid(row=1, column=8, padx=5, pady=5)

        # Semanas
        self.frame_dias = ttk.Labelframe(self.frame_principal, text="Widgets Checkbuttons", padding=10, labelanchor='ne')
        self.frame_dias.pack(fill="x", pady=10)
        self.var_segunda = tk.IntVar(value=0)
        self.var_terca = tk.IntVar(value=0)
        self.var_quarta = tk.IntVar(value=0)
        self.var_quinta = tk.IntVar(value=0)
        self.var_sexta = tk.IntVar(value=0)
        self.var_sabado = tk.IntVar(value=0)
        self.var_domingo = tk.IntVar(value=0)
        self.check_segunda = ttk.Checkbutton(self.frame_dias, text="Segunda-feira", variable=self.var_segunda)
        self.check_segunda.grid(row=0, column=0, padx=5, pady=5)
        self.check_terca = ttk.Checkbutton(self.frame_dias, text="Terça-feira", variable=self.var_terca)
        self.check_terca.grid(row=0, column=1, padx=5, pady=5)
        self.check_quarta = ttk.Checkbutton(self.frame_dias, text="Quarta-feira", variable=self.var_quarta)
        self.check_quarta.grid(row=0, column=2, padx=5, pady=5)
        self.check_quinta = ttk.Checkbutton(self.frame_dias, text="Quinta-feira", variable=self.var_quinta)
        self.check_quinta.grid(row=0, column=3, padx=5, pady=5)
        self.check_sexta = ttk.Checkbutton(self.frame_dias, text="Sexta-feira", variable=self.var_sexta)
        self.check_sexta.grid(row=0, column=4, padx=5, pady=5)
        self.check_sabado = ttk.Checkbutton(self.frame_dias, text="Sábado", variable=self.var_sabado)
        self.check_sabado.grid(row=0, column=5, padx=5, pady=5)
        self.check_domingo = ttk.Checkbutton(self.frame_dias, text="Domingo", variable=self.var_domingo)
        self.check_domingo.grid(row=0, column=6, padx=5, pady=5)

        # Scale
        ttk.Label(self.frame_principal, text="Widget Scale").pack(anchor="s")
        self.frame_scale = ttk.Frame(self.frame_principal)
        self.frame_scale.pack(fill="x", padx=5, pady=5)
        self.frame_scale.columnconfigure(0, weight=1)
        self.frame_scale.columnconfigure(1, weight=0)
        self.escala = ttk.Scale(self.frame_scale, from_=0, to=100, orient="horizontal")
        self.escala.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        self.label_valor = ttk.Label(self.frame_scale, text="0")
        self.label_valor.grid(row=0, column=1, padx=5, pady=5)
        self.escala.bind("<Motion>", self.atualizar_valor_escala)
        self.escala.bind("<ButtonRelease-1>", self.atualizar_valor_escala)

        # Text
        ttk.Label(self.frame_principal, text="Widget Text com Scrollbar").pack(anchor="s")
        self.frame_text = ttk.Frame(self.frame_principal)
        self.frame_text.pack(fill="x", padx=5, pady=5)
        self.text_box = tk.Text(self.frame_text, height=6, wrap="word")
        self.text_box.insert("1.0", """The Zen of Python, by Tim Peters\n\nBeautiful is better than ugly.\nExplicit is better than implicit.\nSimple is better than complex.""")
        self.scroll_bar = ttk.Scrollbar(self.frame_text, orient="vertical", command=self.text_box.yview)
        self.text_box.configure(yscrollcommand=self.scroll_bar.set)
        self.text_box.pack(side="left", fill="x", expand=True)
        self.scroll_bar.pack(side="right", fill="y")

    def mudar_tema(self):
        tema_selecionado = self.tema_var.get()
        self.style.theme_use(tema_selecionado)
        self.label_titulo.config(text=tema_selecionado.capitalize())

    def atualizar_valor_escala(self, event):
        valor = self.escala.get()
        self.label_valor.config(text=f"{valor:.0f}")


janela = tk.Tk()
app = Tela(janela)
janela.mainloop()
