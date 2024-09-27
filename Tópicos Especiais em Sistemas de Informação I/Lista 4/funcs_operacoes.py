import tkinter as tk
from tkinter import messagebox, ttk


def operacoes(self):
    self.janela_operacoes = tk.Toplevel(self.janela)
    self.janela_operacoes.title('Operações Bancárias')
    self.janela_operacoes.geometry('600x400')
    self.janela_operacoes.grab_set()
    self.janela_operacoes.focus()

    self.trw_operacoes = ttk.Treeview(self.janela_operacoes,
                                      columns=('Conta', 'Titular', 'Saldo'), show='headings')
    self.trw_operacoes.heading('Conta', text='Conta')
    self.trw_operacoes.heading('Titular', text='Titular')
    self.trw_operacoes.heading('Saldo', text='Saldo')

    self.trw_operacoes.column('Conta', width=100)
    self.trw_operacoes.column('Titular', width=200)
    self.trw_operacoes.column('Saldo', width=100)

    scr = ttk.Scrollbar(self.janela_operacoes, orient='vertical', command=self.trw_operacoes.yview)
    self.trw_operacoes.configure(yscrollcommand=scr.set)
    scr.pack(side=tk.RIGHT, fill=tk.Y)

    self.trw_operacoes.pack(fill=tk.BOTH, expand=True)

    for banco in self.lista_bancos:
        for conta in banco.get_contas():
            self.trw_operacoes.insert('', 'end', values=(conta.get_numero(),
                                                         conta.get_titular().get_nome(),
                                                         f'{conta.get_saldo():.2f}'))

    btn_frame = ttk.Frame(self.janela_operacoes)
    btn_frame.pack(fill=tk.X)

    btn_frame.grid_columnconfigure(0, weight=1)
    btn_frame.grid_columnconfigure(1, weight=1)

    btn_saque = tk.Button(btn_frame, text='Saque', command=self.saque,
                          font=('Arial', 9, 'bold'), bg='#003594', fg='white')
    btn_saque.grid(row=0, column=0, sticky='e', padx=10)

    btn_deposito = tk.Button(btn_frame, text='Depósito', command=self.deposito,
                             font=('Arial', 9, 'bold'), bg='#003594', fg='white')
    btn_deposito.grid(row=0, column=1, sticky='w', padx=10)


def saque(self):
    selecionado = self.trw_operacoes.selection()

    if not selecionado:
        messagebox.showerror('Erro', 'É necessário selecionar uma conta.')
        return

    conta_valores = self.trw_operacoes.item(selecionado, 'values')
    numero = conta_valores[0]

    def realizar_saque():
        valor = float(ent_valor.get())
        conta = None
        for banco in self.lista_bancos:
            for conta_for in banco.get_contas():
                if conta_for.get_numero() == str(numero):
                    conta = conta_for
        if conta:
            try:
                conta.saque(valor)
                atualizar_saldo(self, numero)
                self.atualizar_totais()
                janela_saque.destroy()
            except ValueError:
                pass
        else:
            messagebox.showerror('Erro', 'Conta não encontrada.')

    janela_saque = tk.Toplevel(self.janela_operacoes)
    janela_saque.title('Realizar Saque')

    lbl_valor = ttk.Label(janela_saque, text='Valor do Saque')
    lbl_valor.grid(row=0, column=0)
    ent_valor = ttk.Entry(janela_saque)
    ent_valor.grid(row=0, column=1)

    btn_sacar = ttk.Button(janela_saque, text='Sacar', command=realizar_saque)
    btn_sacar.grid(row=1, column=1)


def deposito(self):
    selecionado = self.trw_operacoes.selection()

    if not selecionado:
        messagebox.showerror('Erro', 'É necessário selecionar uma conta.')
        return

    conta_valores = self.trw_operacoes.item(selecionado, 'values')
    numero = conta_valores[0]

    def realizar_deposito():
        valor = float(ent_valor.get())
        conta = None
        for banco in self.lista_bancos:
            for conta_for in banco.get_contas():
                if conta_for.get_numero() == str(numero):
                    conta = conta_for
        if conta:
            conta.deposito(valor)
            atualizar_saldo(self, numero)
            self.atualizar_totais()
            janela_deposito.destroy()
        else:
            messagebox.showerror('Erro', 'Conta não encontrada.')

    janela_deposito = tk.Toplevel(self.janela_operacoes)
    janela_deposito.title('Realizar Depósito')

    lbl_valor = ttk.Label(janela_deposito, text='Valor do Depósito')
    lbl_valor.grid(row=0, column=0)
    ent_valor = ttk.Entry(janela_deposito)
    ent_valor.grid(row=0, column=1)

    btn_depositar = ttk.Button(janela_deposito, text='Depositar', command=realizar_deposito)
    btn_depositar.grid(row=1, column=1)


def atualizar_saldo(self, numero):
    for item in self.trw_operacoes.get_children():
        valores = self.trw_operacoes.item(item, 'values')
        if valores[0] == numero:
            conta = None
            for banco in self.lista_bancos:
                for conta_for in banco.get_contas():
                    if conta_for.get_numero() == str(numero):
                        conta = conta_for
            if conta:
                self.trw_operacoes.item(item, values=(conta.get_numero(),
                                                      conta.get_titular().get_nome(),
                                                      f'{conta.get_saldo():.2f}'))
            break

# Devemos trabalha nisso:
def buscar_conta(self, numero):
    for banco in self.lista_bancos:
        for conta in banco.get_contas():
            if conta.get_numero() == str(numero):
                return conta


def gerar_relatorio(self):
    def salvar_relatorio():
        selecionado = trw_contas.selection()

        if not selecionado:
            messagebox.showerror('Erro', 'É necessário selecionar uma conta.')
            return

        conta_valores = trw_contas.item(selecionado, 'values')
        numero = conta_valores[0]

        conta_sel = None
        for banco in self.lista_bancos:
            for conta_for in banco.get_contas():
                if conta_for.get_numero() == str(numero):
                    conta_sel = conta_for

        if conta_sel:
            relatorio = f'relatorio_conta_{numero}.txt'
            with open(relatorio, 'w') as arquivo:
                arquivo.write(f'Relatório da Conta {numero}\n')
                arquivo.write('Data, Tipo, Valor\n')
                for operacao in conta_sel.get_operacoes():
                    arquivo.write(f'{operacao[0]}, {operacao[1]}, {operacao[2]}\n')
                arquivo.write(f'Saldo Final: {conta_sel.get_saldo()}\n')

            messagebox.showinfo('Sucesso', 'Relatório gerado com sucesso!')
            janela_relatorio.destroy()

            visualizar_relatorio(self, relatorio)

        else:
            messagebox.showerror('Erro', 'Conta não encontrada.')

    janela_relatorio = tk.Toplevel(self.janela)
    janela_relatorio.title('Gerar Relatório de Conta')
    janela_relatorio.geometry('500x300')
    janela_relatorio.grab_set()
    janela_relatorio.focus()

    trw_contas = ttk.Treeview(janela_relatorio, columns=('Conta', 'Titular', 'Operações'), show='headings')
    trw_contas.heading('Conta', text='Conta')
    trw_contas.heading('Titular', text='Titular')
    trw_contas.heading('Operações', text='Operações')

    trw_contas.column('Conta', width=100)
    trw_contas.column('Titular', width=200)
    trw_contas.column('Operações', width=100)

    scr = ttk.Scrollbar(janela_relatorio, orient='vertical', command=trw_contas.yview)
    trw_contas.configure(yscrollcommand=scr.set)
    scr.pack(side=tk.RIGHT, fill=tk.Y)

    trw_contas.pack(fill=tk.BOTH, expand=True)

    for banco in self.lista_bancos:
        for conta in banco.get_contas():
            trw_contas.insert('', 'end', values=(conta.get_numero(),
                                                 conta.get_titular().get_nome(),
                                                 len(conta.get_operacoes())))

    btn_salvar = tk.Button(janela_relatorio, text='Gerar Relatório', command=salvar_relatorio,
                           font=('Arial', 9, 'bold'), bg='#003594', fg='white')
    btn_salvar.pack()


def visualizar_relatorio(self, relatorio):
    try:
        with open(relatorio, 'r') as arquivo:
            conteudo = arquivo.read()

        janela_visualizar = tk.Toplevel(self.janela)
        janela_visualizar.title('Visualizar Relatório')
        janela_visualizar.geometry('600x400')

        text_widget = tk.Text(janela_visualizar, wrap='word')
        text_widget.insert('1.0', conteudo)
        text_widget.config(state='disabled')
        text_widget.pack(fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(janela_visualizar, command=text_widget.yview)
        text_widget['yscrollcommand'] = scrollbar.set
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    except FileNotFoundError:
        messagebox.showerror('Erro', f'Não foi possível encontrar o relatório: {relatorio}')
