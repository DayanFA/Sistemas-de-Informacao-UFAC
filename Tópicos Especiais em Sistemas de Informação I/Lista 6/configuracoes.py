import tkinter as tk
from tkinter import ttk
#import ttkbootstrap as tb
def create_configuracoes_window(app):
    configuracoes_window = tk.Toplevel(app.root)
    configuracoes_window.title("Configurações")
    configuracoes_window.geometry("400x300")
    configuracoes_window.resizable(True, True)
    frame = tk.Frame(configuracoes_window)
    frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
    label = tk.Label(frame, text="Configurações Gerais", font=("Helvetica", 14))
    label.pack(pady=10)
    # Temas
    app.tema_var = tk.StringVar(value="Padrão")
    frame_temas = ttk.Labelframe(frame, text="Temas do TTk Bootstrap", padding=10)
    frame_temas.pack(fill="x", pady=10)
    temas = ["Padrão", "morph", "journal", "darkly", "superhero", "solar", "cyborg", "vapor", "simplex", "cerculean", "cosmo", "flatly", "litera", "minty", "lumen", "sandstone", "yeti", "pulse", "united"]
    for i, tema in enumerate(temas):
        ttk.Radiobutton(frame_temas, text=tema, variable=app.tema_var, value=tema, command=lambda: mudar_tema(app)).grid(row=i//4, column=i%4, padx=5, pady=5)
def mudar_tema(app):
    tema_selecionado = app.tema_var.get()
    if tema_selecionado == "Padrão":
        if app.style:
            app.style = None
            app.root.option_clear()
            for widget in app.root.winfo_children():
                widget.destroy()
            app.__init__(app.root)
    else:
        app.style = tb.Style(tema_selecionado)
    app.update_chaves_ui()