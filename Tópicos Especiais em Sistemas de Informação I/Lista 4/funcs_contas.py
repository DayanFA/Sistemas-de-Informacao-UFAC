import tkinter as tk
from tkinter import messagebox, ttk
from back_contas import ContaCorrente, ContaPoupanca


def listar_contas(self):
    self.janela_contas = tk.Toplevel(self.janela)
    self.janela_contas.title('Lista de Contas')
    self.janela_contas.geometry('600x300')
    self.janela_contas.grab_set()
    self.janela_contas.focus()

    self.trw_contas = ttk.Treeview(self.janela_contas,
                                   columns=('Número', 'Titular', 'Tipo', 'Banco',
                                            'Saldo'), show='headings')
    self.trw_contas.heading('Número', text='Número')
    self.trw_contas.heading('Titular', text='Titular')
    self.trw_contas.heading('Tipo', text='Tipo')
    self.trw_contas.heading('Banco', text='Banco')
    self.trw_contas.heading('Saldo', text='Saldo')

    self.trw_contas.column('Número', width=50)
    self.trw_contas.column('Titular', width=150)
    self.trw_contas.column('Tipo', width=80)
    self.trw_contas.column('Banco', width=80)
    self.trw_contas.column('Saldo', width=80)

    scr = ttk.Scrollbar(self.janela_contas, orient='vertical', command=self.trw_contas.yview)
    self.trw_contas.configure(yscrollcommand=scr.set)
    scr.pack(side=tk.RIGHT, fill=tk.Y)

    self.trw_contas.pack(fill=tk.BOTH, expand=True)

    for banco in self.lista_bancos:
        for conta in banco.get_contas():
            tipo_conta = 'Poupança' if isinstance(conta, ContaPoupanca) else 'Corrente'
            self.trw_contas.insert('', 'end', values=(conta.get_numero(),
                                                      conta.get_titular().get_nome(), tipo_conta,
                                                      conta.get_banco().get_nome(), f'{conta.get_saldo():.2f}'))

    btn_frame = ttk.Frame(self.janela_contas)
    btn_frame.pack(fill=tk.X)

    btn_frame.grid_columnconfigure(0, weight=1)
    btn_frame.grid_columnconfigure(1, weight=1)
    btn_frame.grid_columnconfigure(2, weight=1)

    btn_cadastrar_poupanca = tk.Button(btn_frame, text='Cadastrar Conta Poupança',
                                       font=('Arial', 9, 'bold'), bg='#003594', fg='white',
                                       command=self.cadastrar_conta_poupanca)
    btn_cadastrar_poupanca.grid(row=0, column=0, sticky='e', padx=10)

    btn_cadastrar_corrente = tk.Button(btn_frame, text='Cadastrar Conta Corrente',
                                       font=('Arial', 9, 'bold'), bg='#003594', fg='white',
                                       command=self.cadastrar_conta_corrente)
    btn_cadastrar_corrente.grid(row=0, column=1, padx=10)

    btn_encerrar = tk.Button(btn_frame, text='Encerrar Conta',
                             font=('Arial', 9, 'bold'), bg='#003594', fg='white',
                             command=self.encerrar_conta)
    btn_encerrar.grid(row=0, column=2, sticky='w', padx=10)


def cadastrar_conta_poupanca(self):
    def preencher_cpf(event):
        cliente_selecionado = cmb_clientes.get()
        self.cliente = next((cliente for cliente in self.lista_clientes
                             if cliente.get_nome() == cliente_selecionado), None)
        if self.cliente:
            ent_cpf.delete(0, tk.END)
            ent_cpf.insert(0, self.cliente.get_cpf())

    def salvar_conta_poupanca():
        numero = ent_numero.get()
        cpf = ent_cpf.get()
        saldo = ent_saldo.get()
        taxa_juros = ent_juros.get()
        banco_selecionado = cmb_bancos.get()

        if not numero or not cpf or not saldo or not taxa_juros or not banco_selecionado:
            messagebox.showerror('Erro', 'Todos os campos devem ser preenchidos.')
            return
        try:
            saldo = float(saldo)
            taxa_juros = float(taxa_juros)
        except ValueError:
            messagebox.showerror('Erro', 'Saldo e Taxa de Juros devem ser valores numéricos.')
            return

        banco = next((banco for banco in self.lista_bancos if banco.get_nome() == banco_selecionado), None)
        if self.cliente and banco:
            conta = ContaPoupanca(numero, self.cliente, saldo, taxa_juros, banco)
            banco.adicionar_conta(conta)

            self.trw_contas.insert('', 'end', values=(numero, self.cliente.get_nome(),
                                                      'Poupança', banco.get_nome(), f'{saldo:.2f}'))

            messagebox.showinfo('Sucesso', 'Conta Poupança cadastrada com sucesso!')
            self.atualizar_totais()
            janela_cadastro.destroy()
        else:
            messagebox.showerror('Erro', 'Cliente ou banco não encontrado.')

    janela_cadastro = tk.Toplevel(self.janela_contas)
    janela_cadastro.title('Cadastrar Conta Poupança')

    lbl_numero = ttk.Label(janela_cadastro, text='Número da Conta')
    lbl_numero.grid(row=0, column=0)
    ent_numero = ttk.Entry(janela_cadastro, width=30)
    ent_numero.grid(row=0, column=1)

    lbl_cliente = ttk.Label(janela_cadastro, text='Cliente')
    lbl_cliente.grid(row=1, column=0)

    cmb_clientes = ttk.Combobox(janela_cadastro, values=[cliente.get_nome()
                                                         for cliente in self.lista_clientes], width=28)
    cmb_clientes.grid(row=1, column=1)
    cmb_clientes.bind('<<ComboboxSelected>>', preencher_cpf)

    lbl_cpf = ttk.Label(janela_cadastro, text='CPF do Titular')
    lbl_cpf.grid(row=2, column=0)
    ent_cpf = ttk.Entry(janela_cadastro, width=30)
    ent_cpf.grid(row=2, column=1)

    lbl_saldo = ttk.Label(janela_cadastro, text='Saldo Inicial')
    lbl_saldo.grid(row=3, column=0)
    ent_saldo = ttk.Entry(janela_cadastro, width=30)
    ent_saldo.grid(row=3, column=1)

    lbl_juros = ttk.Label(janela_cadastro, text='Taxa de Juros (%)')
    lbl_juros.grid(row=4, column=0)
    ent_juros = ttk.Entry(janela_cadastro, width=30)
    ent_juros.grid(row=4, column=1)

    lbl_banco = ttk.Label(janela_cadastro, text='Banco')
    lbl_banco.grid(row=5, column=0)

    cmb_bancos = ttk.Combobox(janela_cadastro, values=[banco.get_nome() for banco in self.lista_bancos], width=28)
    cmb_bancos.grid(row=5, column=1)

    btn_salvar = ttk.Button(janela_cadastro, text='Salvar', command=salvar_conta_poupanca)
    btn_salvar.grid(row=6, column=1)


def cadastrar_conta_corrente(self):
    def preencher_cpf(event):
        cliente_selecionado = cmb_clientes.get()
        self.cliente = next((cliente for cliente in self.lista_clientes
                             if cliente.get_nome() == cliente_selecionado), None)
        if self.cliente:
            ent_cpf.delete(0, tk.END)
            ent_cpf.insert(0, self.cliente.get_cpf())

    def salvar_conta_corrente():
        numero = ent_numero.get()
        cpf = ent_cpf.get()
        saldo = ent_saldo.get()
        taxa_desconto = ent_desconto.get()
        banco_selecionado = cmb_bancos.get()

        if not numero or not cpf or not saldo or not taxa_desconto or not banco_selecionado:
            messagebox.showerror('Erro', 'Todos os campos devem ser preenchidos.')
            return

        try:
            saldo = float(saldo)
            taxa_desconto = float(taxa_desconto)
        except ValueError:
            messagebox.showerror('Erro', 'Saldo e Taxa de Desconto devem ser valores numéricos.')
            return

        banco = next((banco for banco in self.lista_bancos if banco.get_nome() == banco_selecionado), None)
        if self.cliente and banco:
            conta = ContaCorrente(numero, self.cliente, saldo, taxa_desconto, banco)
            banco.adicionar_conta(conta)

            self.trw_contas.insert('', 'end', values=(numero, self.cliente.get_nome(),
                                                      'Corrente', banco.get_nome(), f'{saldo:.2f}'))

            messagebox.showinfo('Sucesso', 'Conta Corrente cadastrada com sucesso!')
            self.atualizar_totais()
            janela_cadastro.destroy()
        else:
            messagebox.showerror('Erro', 'Cliente ou banco não encontrado.')

    janela_cadastro = tk.Toplevel(self.janela_contas)
    janela_cadastro.title('Cadastrar Conta Corrente')

    lbl_numero = ttk.Label(janela_cadastro, text='Número da Conta')
    lbl_numero.grid(row=0, column=0)
    ent_numero = ttk.Entry(janela_cadastro, width=30)
    ent_numero.grid(row=0, column=1)

    lbl_cliente = ttk.Label(janela_cadastro, text='Cliente')
    lbl_cliente.grid(row=1, column=0)

    cmb_clientes = ttk.Combobox(janela_cadastro, values=[cliente.get_nome()
                                                         for cliente in self.lista_clientes], width=28)
    cmb_clientes.grid(row=1, column=1)
    cmb_clientes.bind('<<ComboboxSelected>>', preencher_cpf)

    lbl_cpf = ttk.Label(janela_cadastro, text='CPF do Titular')
    lbl_cpf.grid(row=2, column=0)
    ent_cpf = ttk.Entry(janela_cadastro, width=30)
    ent_cpf.grid(row=2, column=1)

    lbl_saldo = ttk.Label(janela_cadastro, text='Saldo Inicial')
    lbl_saldo.grid(row=3, column=0)
    ent_saldo = ttk.Entry(janela_cadastro, width=30)
    ent_saldo.grid(row=3, column=1)

    lbl_desconto = ttk.Label(janela_cadastro, text='Taxa de Desconto (%)')
    lbl_desconto.grid(row=4, column=0)
    ent_desconto = ttk.Entry(janela_cadastro, width=30)
    ent_desconto.grid(row=4, column=1)

    lbl_banco = ttk.Label(janela_cadastro, text='Banco')
    lbl_banco.grid(row=5, column=0)

    cmb_bancos = ttk.Combobox(janela_cadastro, values=[banco.get_nome() for banco in self.lista_bancos], width=28)
    cmb_bancos.grid(row=5, column=1)

    btn_salvar = ttk.Button(janela_cadastro, text='Salvar', command=salvar_conta_corrente)
    btn_salvar.grid(row=6, column=1)


def encerrar_conta(self):
    selecionado = self.trw_contas.selection()

    if not selecionado:
        messagebox.showerror('Erro', 'É necessário selecionar uma conta.')
        return

    conta_valores = self.trw_contas.item(selecionado, 'values')
    self.numero = conta_valores[0]

    conta = None
    for banco in self.lista_bancos:
        for conta_for in banco.get_contas():
            if conta_for.get_numero() == str(self.numero):
                conta = conta_for

    if conta:
        banco_associado = conta.get_banco()
        confirmacao = messagebox.askyesno('Confirmar Encerramento',
                                          f'Deseja realmente encerrar a conta {self.numero}?')
        if confirmacao:
            banco_associado.excluir_conta(self.numero)
            self.trw_contas.delete(selecionado)
            self.atualizar_totais()
    else:
        messagebox.showerror('Erro', 'Conta não encontrada.')
