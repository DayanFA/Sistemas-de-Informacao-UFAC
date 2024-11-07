import tkinter as tk
from tkinter import messagebox
from ui_helpers import create_treeview_with_scrollbars

def create_cadastro_chaves_window(app):
    cadastro_chaves_window = tk.Toplevel(app.root)
    cadastro_chaves_window.title("Cadastro de Chaves")
    cadastro_chaves_window.geometry("600x400")
    cadastro_chaves_window.resizable(True, True)

    frame = tk.Frame(cadastro_chaves_window)
    frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

    label = tk.Label(frame, text="Cadastro de Chaves", font=("Helvetica", 14))
    label.pack(pady=10)

    # Exibir dados em uma Treeview com scrollbars
    tree = create_treeview_with_scrollbars(frame)
    tree["columns"] = ("Nome", "Número de Cópias", "Descrição")
    for col in tree["columns"]:
        tree.heading(col, text=col)
        tree.column(col, width=150)

    # Botões
    button_frame = tk.Frame(frame)
    button_frame.pack(pady=10)

    add_button = tk.Button(button_frame, text="Adicionar", command=lambda: add_chave(app, tree))
    add_button.pack(side=tk.LEFT, padx=5)

    edit_button = tk.Button(button_frame, text="Editar", command=lambda: edit_chave(app, tree))
    edit_button.pack(side=tk.LEFT, padx=5)

    delete_button = tk.Button(button_frame, text="Deletar", command=lambda: delete_chave(app, tree))
    delete_button.pack(side=tk.LEFT, padx=5)

    # Carregar dados iniciais
    load_chaves(tree, app.chave_info)

def load_chaves(tree, chave_info):
    for chave, info in chave_info.items():
        tree.insert("", tk.END, values=(chave, info["num_copias"], info["descricao"]))

def add_chave(app, tree):
    def save():
        nome = nome_var.get()
        num_copias = num_copias_var.get() or 1
        descricao = descricao_var.get() or ""
        if nome:
            app.chave_info[nome] = {"num_copias": num_copias, "descricao": descricao, "reservas": [], "status": "green"}
            tree.insert("", tk.END, values=(nome, num_copias, descricao))
            app.update_chaves_ui()
            app.update_chaves_list()
            app.salvar_chave_no_banco(nome, num_copias, descricao)
            app.update_chaves_combobox()
            add_window.destroy()
        else:
            messagebox.showerror("Erro", "O campo 'Nome' é obrigatório.")

    add_window = tk.Toplevel(app.root)
    add_window.title("Adicionar Chave")
    add_window.geometry("400x300")

    tk.Label(add_window, text="Nome:").pack(pady=5)
    nome_var = tk.StringVar()
    tk.Entry(add_window, textvariable=nome_var).pack(pady=5)

    tk.Label(add_window, text="Número de Cópias:").pack(pady=5)
    num_copias_var = tk.StringVar()
    tk.Entry(add_window, textvariable=num_copias_var).pack(pady=5)

    tk.Label(add_window, text="Descrição:").pack(pady=5)
    descricao_var = tk.StringVar()
    tk.Entry(add_window, textvariable=descricao_var).pack(pady=5)

    tk.Button(add_window, text="Salvar", command=save).pack(pady=10)

def edit_chave(app, tree):
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Erro", "Selecione uma chave para editar.")
        return

    item = tree.item(selected_item)
    nome, num_copias, descricao = item["values"]

    def save():
        new_nome = nome_var.get()
        new_num_copias = num_copias_var.get() or 1
        new_descricao = descricao_var.get() or ""
        if new_nome:
            if nome in app.chave_info:
                app.chave_info.pop(nome)
            app.chave_info[new_nome] = {"num_copias": new_num_copias, "descricao": new_descricao, "reservas": [], "status": "green"}
            tree.item(selected_item, values=(new_nome, new_num_copias, new_descricao))
            app.update_chaves_ui()
            app.update_chaves_list()
            app.salvar_chave_no_banco(new_nome, new_num_copias, new_descricao)
            app.update_chaves_combobox()
            edit_window.destroy()
        else:
            messagebox.showerror("Erro", "O campo 'Nome' é obrigatório.")

    edit_window = tk.Toplevel(app.root)
    edit_window.title("Editar Chave")
    edit_window.geometry("400x300")

    tk.Label(edit_window, text="Nome:").pack(pady=5)
    nome_var = tk.StringVar(value=nome)
    tk.Entry(edit_window, textvariable=nome_var).pack(pady=5)

    tk.Label(edit_window, text="Número de Cópias:").pack(pady=5)
    num_copias_var = tk.StringVar(value=num_copias)
    tk.Entry(edit_window, textvariable=num_copias_var).pack(pady=5)

    tk.Label(edit_window, text="Descrição:").pack(pady=5)
    descricao_var = tk.StringVar(value=descricao)
    tk.Entry(edit_window, textvariable=descricao_var).pack(pady=5)

    tk.Button(edit_window, text="Salvar", command=save).pack(pady=10)

def delete_chave(app, tree):
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Erro", "Selecione uma chave para deletar.")
        return

    item = tree.item(selected_item)
    nome = item["values"][0]

    if messagebox.askyesno("Deletar", f"Tem certeza que deseja deletar a chave {nome}?"):
        if nome in app.chave_info:
            app.chave_info.pop(nome)
        tree.delete(selected_item)
        app.update_chaves_ui()
        app.update_chaves_list()
        app.deletar_chave_do_banco(nome)
        app.update_chaves_combobox()