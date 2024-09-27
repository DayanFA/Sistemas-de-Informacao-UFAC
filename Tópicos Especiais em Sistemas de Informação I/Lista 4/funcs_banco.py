import tkinter as tk
from tkinter import messagebox, ttk
from back_banco import Banco


def listar_bancos(self):
    self.janela_bancos = tk.Toplevel(self.janela)
    self.janela_bancos.title('Lista de Bancos')
    self.janela_bancos.geometry('400x300')
    self.janela_bancos.grab_set()
    self.janela_bancos.focus()

    trw_bancos = ttk.Treeview(self.janela_bancos, columns=('Número', 'Nome'), show='headings')
    trw_bancos.heading('Número', text='Número')
    trw_bancos.heading('Nome', text='Nome')

    trw_bancos.column('Número', width=40)
    trw_bancos.column('Nome', width=100)

    scrollbar_bancos = ttk.Scrollbar(self.janela_bancos, orient='vertical', command=trw_bancos.yview)
    trw_bancos.configure(yscrollcommand=scrollbar_bancos.set)
    scrollbar_bancos.pack(side=tk.RIGHT, fill=tk.Y)

    trw_bancos.pack(fill=tk.BOTH, expand=True)

    self.carregar_bancos_treeview(trw_bancos)

    btn_frame = tk.Frame(self.janela_bancos)
    btn_frame.pack(fill=tk.X)

    btn_cadastrar = tk.Button(btn_frame, text='Cadastrar', font=('Arial', 9, 'bold'), bg='#003594', fg='white',
                              command=lambda: self.cadastrar_banco(trw_bancos))
    btn_cadastrar.grid(row=0, column=0, sticky='e', padx=10)
    btn_atualizar = tk.Button(btn_frame, text='Atualizar', font=('Arial', 9, 'bold'), bg='#003594', fg='white',
                              command=lambda: self.atualizar_banco(trw_bancos))
    btn_atualizar.grid(row=0, column=1, sticky='w', padx=10)
    btn_frame.grid_columnconfigure(0, weight=1)
    btn_frame.grid_columnconfigure(1, weight=1)


def carregar_bancos_treeview(self, trw_bancos):
    for item in trw_bancos.get_children():
        trw_bancos.delete(item)
    for banco in self.lista_bancos:
        trw_bancos.insert('', 'end', values=(banco.get_numero(), banco.get_nome()))


def cadastrar_banco(self, trw_bancos):
    def salvar_banco():
        numero = ent_numero.get()
        nome = ent_nome.get()
        novo_banco = Banco(str(numero), nome)
        self.lista_bancos.append(novo_banco)
        messagebox.showinfo('Sucesso', 'Banco cadastrado com sucesso!')
        self.carregar_bancos_treeview(trw_bancos)
        self.atualizar_totais()
        janela_cadastro.destroy()

    janela_cadastro = tk.Toplevel(self.janela_bancos)
    janela_cadastro.title('Cadastrar Banco')
    janela_cadastro.transient(self.janela)

    tk.Label(janela_cadastro, text='Número:').grid(row=0, column=0)
    ent_numero = ttk.Entry(janela_cadastro)
    ent_numero.grid(row=0, column=1)

    tk.Label(janela_cadastro, text='Nome:').grid(row=1, column=0)
    ent_nome = tk.Entry(janela_cadastro)
    ent_nome.grid(row=1, column=1)

    tk.Button(janela_cadastro, text='Salvar', command=salvar_banco).grid(row=2, columnspan=2)


def atualizar_banco(self, trw_bancos):
    selecao = trw_bancos.selection()
    if selecao:
        banco_selecionado = trw_bancos.item(selecao)['values']
        numero = str(banco_selecionado[0])
        nome_atual = banco_selecionado[1]

        def salvar():
            novo_nome = ent_nome.get()
            for banco in self.lista_bancos:
                if banco.get_numero() == numero:
                    banco.set_nome(novo_nome)
                    self.carregar_bancos_treeview(trw_bancos)
                    messagebox.showinfo('Sucesso', 'Banco atualizado com sucesso!')
                    self.atualizar_totais()
                    janela_atualizar.destroy()
                    return

        janela_atualizar = tk.Toplevel(self.janela_bancos)
        janela_atualizar.title(f'Atualizar Banco {nome_atual}')

        ttk.Label(janela_atualizar, text='Nome:').grid(row=0, column=0, padx=10)
        ent_nome = ttk.Entry(janela_atualizar)
        ent_nome.insert(0, nome_atual)
        ent_nome.grid(row=0, column=1, padx=10)

        ttk.Button(janela_atualizar, text='Salvar', command=salvar).grid(row=1, columnspan=2)

    else:
        messagebox.showerror('Erro', 'Selecione um banco para atualizar.')
