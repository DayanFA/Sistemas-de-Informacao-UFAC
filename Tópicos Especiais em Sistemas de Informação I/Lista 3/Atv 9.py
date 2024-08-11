import tkinter as tk
from tkinter import ttk, messagebox

funcionarios = []

def salvar_funcionario():
    nome = entry_nome.get()
    data_nascimento = entry_data_nascimento.get()
    documento = entry_documento.get()
    email = entry_email.get()
    telefone = entry_telefone.get()

    if not (nome and data_nascimento and documento and email and telefone):
        messagebox.showwarning("Aviso", "Todos os campos são obrigatórios!")
        return

    funcionario = {
        "Nome": nome,
        "Data de Nascimento": data_nascimento,
        "Documento": documento,
        "Email": email,
        "Telefone": telefone
    }
    funcionarios.append(funcionario)
    atualizar_treeview()
    limpar_campos()

def atualizar_treeview():
    for row in tree.get_children():
        tree.delete(row)
    for funcionario in funcionarios:
        tree.insert("", "end", values=(funcionario["Nome"], funcionario["Data de Nascimento"], funcionario["Documento"], funcionario["Email"], funcionario["Telefone"]))

def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_data_nascimento.delete(0, tk.END)
    entry_documento.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)

def mostrar_cadastro():
    frame_cadastro.tkraise()

def mostrar_visualizacao():
    frame_visualizacao.tkraise()

root = tk.Tk()
root.title("Cadastro de Funcionários")
root.geometry("600x400")

menu = tk.Menu(root)
root.config(menu=menu)
menu.add_command(label="Cadastro", command=mostrar_cadastro)
menu.add_command(label="Visualização", command=mostrar_visualizacao)

frame_cadastro = tk.Frame(root)
frame_cadastro.place(relwidth=1, relheight=1)

tk.Label(frame_cadastro, text="Nome:").grid(row=0, column=0, padx=10, pady=10)
entry_nome = tk.Entry(frame_cadastro)
entry_nome.grid(row=0, column=1, padx=10, pady=10)

tk.Label(frame_cadastro, text="Data de Nascimento:").grid(row=1, column=0, padx=10, pady=10)
entry_data_nascimento = tk.Entry(frame_cadastro)
entry_data_nascimento.grid(row=1, column=1, padx=10, pady=10)

tk.Label(frame_cadastro, text="Documento:").grid(row=2, column=0, padx=10, pady=10)
entry_documento = tk.Entry(frame_cadastro)
entry_documento.grid(row=2, column=1, padx=10, pady=10)

tk.Label(frame_cadastro, text="Email:").grid(row=3, column=0, padx=10, pady=10)
entry_email = tk.Entry(frame_cadastro)
entry_email.grid(row=3, column=1, padx=10, pady=10)

tk.Label(frame_cadastro, text="Telefone:").grid(row=4, column=0, padx=10, pady=10)
entry_telefone = tk.Entry(frame_cadastro)
entry_telefone.grid(row=4, column=1, padx=10, pady=10)

tk.Button(frame_cadastro, text="Salvar", command=salvar_funcionario).grid(row=5, column=0, columnspan=2, pady=20)

frame_visualizacao = tk.Frame(root)
frame_visualizacao.place(relwidth=1, relheight=1)

tree = ttk.Treeview(frame_visualizacao, columns=("Nome", "Data de Nascimento", "Documento", "Email", "Telefone"), show="headings")
tree.heading("Nome", text="Nome")
tree.heading("Data de Nascimento", text="Data de Nascimento")
tree.heading("Documento", text="Documento")
tree.heading("Email", text="Email")
tree.heading("Telefone", text="Telefone")
tree.pack(fill=tk.BOTH, expand=True)

mostrar_cadastro()
root.mainloop()