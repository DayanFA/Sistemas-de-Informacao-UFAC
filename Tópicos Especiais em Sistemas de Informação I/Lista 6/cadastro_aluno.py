import tkinter as tk
from ui_helpers import create_treeview_with_scrollbars

def create_cadastro_alunos_window(app):
    cadastro_window = tk.Toplevel(app.root)
    cadastro_window.title("Cadastro de Alunos")
    cadastro_window.geometry("600x400")
    cadastro_window.resizable(True, True)

    frame = tk.Frame(cadastro_window)
    frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

    label = tk.Label(frame, text="Cadastro de Alunos", font=("Helvetica", 14))
    label.pack(pady=10)

    # Exibir dados em uma Treeview com scrollbars
    tree = create_treeview_with_scrollbars(frame)
    app.alunos_tree = tree

    # Carregar dados iniciais
    caminho_inicial = app.ler_caminho_importacao("caminho_alunos")
    if caminho_inicial:
        app.load_data(tree, caminho_inicial)
    else:
        app.load_data(tree, "cadastro_alunos.xlsx")

    # Botão para importar planilha
    import_button = tk.Button(frame, text="Importar", command=lambda: app.import_data(tree, "cadastro_alunos.xlsx", "caminho_alunos"))
    import_button.pack(pady=10)