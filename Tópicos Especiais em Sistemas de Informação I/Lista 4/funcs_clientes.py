import tkinter as tk
from tkinter import messagebox, ttk
from back_cliente import Cliente


def listar_clientes(self):
    self.janela_clientes = tk.Toplevel(self.janela)
    self.janela_clientes.title('Lista de Clientes')
    self.janela_clientes.geometry('600x300')
    self.janela_clientes.grab_set()
    self.janela_clientes.focus()

    self.trw_clientes = ttk.Treeview(self.janela_clientes, columns=('CPF', 'Nome', 'Endereço'), show='headings')
    self.trw_clientes.heading('CPF', text='CPF')
    self.trw_clientes.heading('Nome', text='Nome')
    self.trw_clientes.heading('Endereço', text='Endereço')

    self.trw_clientes.column('CPF', width=50)
    self.trw_clientes.column('Nome', width=100)
    self.trw_clientes.column('Endereço', width=100)

    scr = ttk.Scrollbar(self.janela_clientes, orient='vertical', command=self.trw_clientes.yview)
    self.trw_clientes.configure(yscrollcommand=scr.set)
    scr.pack(side=tk.RIGHT, fill=tk.Y)

    self.trw_clientes.pack(fill=tk.BOTH, expand=True)

    for cliente in self.lista_clientes:
        self.trw_clientes.insert('', 'end', values=(cliente.get_cpf(), cliente.get_nome(), cliente.get_endereco()))

    btn_frame = ttk.Frame(self.janela_clientes)
    btn_frame.pack(fill=tk.X)

    btn_frame.grid_columnconfigure(0, weight=1)
    btn_frame.grid_columnconfigure(1, weight=1)
    btn_frame.grid_columnconfigure(2, weight=1)

    btn_cadastrar = tk.Button(btn_frame, text='Cadastrar',
                              font=('Arial', 9, 'bold'), bg='#003594', fg='white',
                              command=self.cadastrar_cliente)
    btn_cadastrar.grid(row=0, column=0, sticky='e', padx=10)

    btn_remover = tk.Button(btn_frame, text='Remover',
                            font=('Arial', 9, 'bold'), bg='#003594', fg='white',
                            command=self.remover_cliente)
    btn_remover.grid(row=0, column=1, padx=10)

    btn_atualizar = tk.Button(btn_frame, text='Atualizar',
                              font=('Arial', 9, 'bold'), bg='#003594', fg='white',
                              command=self.atualizar_cliente)
    btn_atualizar.grid(row=0, column=2, sticky='w', padx=10)


def cadastrar_cliente(self):
    def salvar_cliente():
        nome = ent_nome.get()
        endereco = ent_endereco.get()
        cpf = ent_cpf.get()
        try:
            cliente = Cliente(nome, endereco, cpf)
            self.lista_clientes.append(cliente)
            messagebox.showinfo('Sucesso', 'Cliente cadastrado com sucesso!')
            self.trw_clientes.insert('', 'end', values=(cpf, nome, endereco))
            self.atualizar_totais()
            janela_cadastro_cliente.destroy()
        except ValueError:
            pass

    janela_cadastro_cliente = tk.Toplevel(self.janela_clientes)
    janela_cadastro_cliente.title('Cadastrar Cliente')

    lbl_nome = ttk.Label(janela_cadastro_cliente, text='Nome')
    lbl_nome.grid(row=0, column=0)
    ent_nome = ttk.Entry(janela_cadastro_cliente)
    ent_nome.grid(row=0, column=1)

    lbl_endereco = ttk.Label(janela_cadastro_cliente, text='Endereço')
    lbl_endereco.grid(row=1, column=0)
    ent_endereco = ttk.Entry(janela_cadastro_cliente)
    ent_endereco.grid(row=1, column=1)

    lbl_cpf = ttk.Label(janela_cadastro_cliente, text='CPF')
    lbl_cpf.grid(row=2, column=0)
    ent_cpf = ttk.Entry(janela_cadastro_cliente)
    ent_cpf.grid(row=2, column=1)

    btn_salvar = ttk.Button(janela_cadastro_cliente, text='Salvar', command=salvar_cliente)
    btn_salvar.grid(row=3, column=1)


def remover_cliente(self):
    selected_item = self.trw_clientes.selection()
    if not selected_item:
        messagebox.showerror('Erro', 'Nenhum cliente selecionado.')
        return

    cliente_valores = self.trw_clientes.item(selected_item, 'values')
    cpf = cliente_valores[0]

    for banco in self.lista_bancos:
        for conta in banco.get_contas():
            if conta.get_titular().get_cpf() == cpf:
                messagebox.showerror('Erro', 'Não é possível remover o cliente. Ele possui contas ativas.')
                return

    confirmar = messagebox.askyesno('Confirmação',
                                    f'Tem certeza de que deseja remover o cliente: {cliente_valores[1]}?')
    if confirmar:
        for cliente in self.lista_clientes:
            if cliente.get_cpf() == cpf:
                self.lista_clientes.remove(cliente)
                self.trw_clientes.delete(selected_item)
                messagebox.showinfo('Sucesso', 'Cliente removido com sucesso!')
                self.atualizar_totais()
                return

        messagebox.showerror('Erro', 'Cliente não encontrado.')


def atualizar_cliente(self):
    selected_item = self.trw_clientes.selection()
    if not selected_item:
        messagebox.showerror('Erro', 'Nenhum cliente selecionado.')
        return

    cliente_valores = self.trw_clientes.item(selected_item, 'values')
    cpf = cliente_valores[0]

    def atualizar():
        nome = ent_nome.get()
        endereco = ent_endereco.get()

        for cliente in self.lista_clientes:
            if cliente.get_cpf() == cpf:
                if nome:
                    cliente.set_nome(nome)
                if endereco:
                    cliente.set_endereco(endereco)
                self.trw_clientes.item(selected_item, values=(cpf, nome, endereco))
                messagebox.showinfo('Sucesso', 'Cliente atualizado com sucesso!')
                janela_atualizar.destroy()
                return
        messagebox.showerror('Erro', 'Cliente não encontrado.')

    janela_atualizar = tk.Toplevel(self.janela_clientes)
    janela_atualizar.title('Atualizar Cliente')

    lbl_nome = ttk.Label(janela_atualizar, text='Novo Nome')
    lbl_nome.grid(row=0, column=0)
    ent_nome = ttk.Entry(janela_atualizar)
    ent_nome.insert(0, cliente_valores[1])
    ent_nome.grid(row=0, column=1)

    lbl_endereco = ttk.Label(janela_atualizar, text='Novo Endereço')
    lbl_endereco.grid(row=1, column=0)
    ent_endereco = ttk.Entry(janela_atualizar)
    ent_endereco.insert(0, cliente_valores[2])
    ent_endereco.grid(row=1, column=1)

    btn_atualizar = ttk.Button(janela_atualizar, text='Atualizar', command=atualizar)
    btn_atualizar.grid(row=2, column=1)
