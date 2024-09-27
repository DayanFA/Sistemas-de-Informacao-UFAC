import tkinter as tk
from datetime import datetime
from tkinter import Menu, ttk
from back_banco import Banco
from back_contas import ContaPoupanca, ContaCorrente
from back_cliente import Cliente
import funcs_banco
import funcs_clientes
import funcs_contas
import funcs_operacoes

# Bancos pré-cadastrados
BB = Banco('001', 'Banco do Brasil')
CF = Banco('104', 'Caixa Econômica Federal')
BD = Banco('237', 'Bradesco')
ST = Banco('033', 'Santander')

# Clientes pré-cadastrados
Andre = Cliente('André F. Santana', 'Rua sem nome, Brasileia', '01771244232')
Dayan = Cliente('Dayan Alves', 'Cidade Nova, Rio Branco', '24571244201')
Limeira = Cliente('Manoel Limeira de Lima', 'Algum lugar, Rio Branco', '88971244217')
Geirto = Cliente('Geirto da Informação', 'Sistema de Informação, Ufac', '19071244283')

# Contas pré-cadastradas
andre_corrente = ContaCorrente('00001', Andre, 1500, 0.04, BB)
BB.adicionar_conta(andre_corrente)
andre_poupanca = ContaPoupanca('00002', Andre, 4500, 0.01, BB)
BB.adicionar_conta(andre_poupanca)

dayan_corrente = ContaCorrente('00003', Dayan, 2500, 0.03, CF)
CF.adicionar_conta(dayan_corrente)
dayan_pupanca = ContaPoupanca('00004', Dayan, 3500, 0.02, CF)
CF.adicionar_conta(dayan_pupanca)

limeira_corrente = ContaCorrente('00005', Limeira, 4200, 0.05, BD)
BD.adicionar_conta(limeira_corrente)
limeira_poupanca = ContaPoupanca('00006', Limeira, 10900, 0.03, BD)
BD.adicionar_conta(limeira_poupanca)

geirto_corrente = ContaCorrente('00007', Geirto, 3700, 0.04, ST)
ST.adicionar_conta(geirto_corrente)
geirto_poupanca = ContaPoupanca('00008', Geirto, 6300, 0.03, ST)
ST.adicionar_conta(geirto_poupanca)

# OPERAÇÕES
limeira_poupanca.saque(100)
limeira_corrente.saque(100)
limeira_poupanca.deposito(100)
limeira_corrente.deposito(300)
limeira_poupanca.saque(300)
limeira_corrente.deposito(500)
limeira_poupanca.deposito(500)
limeira_corrente.saque(100)


class BancoApp:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry('600x500')
        self.janela.resizable(False, False)
        self.janela.title(f'Bank System')
        self.lista_bancos = [BB, CF, BD, ST]
        self.lista_clientes = [Andre, Dayan, Limeira, Geirto]
        self.total_bancos = 0
        self.total_clientes = 0
        self.total_correntes = 0
        self.total_poupancas = 0
        self.total_caixa = 0

        menu = Menu(self.janela)
        self.janela.config(menu=menu)

        # MENUS BANCOS E CLIENTES
        menu.add_command(label='Bancos', command=self.listar_bancos)
        menu.add_command(label='Clientes', command=self.listar_clientes)

        # MENU CONTA
        conta_menu = Menu(menu, tearoff=0)
        menu.add_cascade(label='Contas', menu=conta_menu)
        conta_menu.add_command(label='Listar Contas', command=self.listar_contas)
        conta_menu.add_command(label='Cadastrar Conta Poupança', command=self.listar_contas)
        conta_menu.add_command(label='Cadastrar Conta Corrente', command=self.listar_contas)
        conta_menu.add_command(label='Encerrar Conta', command=self.listar_contas)

        # MENU OPERACOES
        operacoes_menu = Menu(menu, tearoff=0)
        menu.add_cascade(label='Operações', menu=operacoes_menu)
        operacoes_menu.add_command(label='Saque', command=self.operacoes)
        operacoes_menu.add_command(label='Depósito', command=self.operacoes)

        # MENU RELATORIO
        relatorio_menu = Menu(menu, tearoff=0)
        menu.add_cascade(label='Relatório', menu=relatorio_menu)
        relatorio_menu.add_command(label='Gerar Relatório', command=self.gerar_relatorio)

        # TELA INICIAL
        frame_principal = tk.Frame(self.janela, bg='#e7f1ff')
        frame_principal.pack(fill=tk.BOTH, expand=True)

        frame_vazio = tk.Frame(frame_principal)
        frame_vazio.pack(fill=tk.X, padx=10, pady=5)

        # data e hora
        frame_data_hora = tk.Frame(frame_principal, bg='#e7f1ff')
        frame_data_hora.pack(fill=tk.X, padx=11)
        lbl_hora = tk.Label(frame_data_hora, text=f'Hora: {datetime.now().strftime('%H:%M')}',
                            font=('Arial', 11), bg='#e7f1ff')
        lbl_hora.pack(side=tk.LEFT)
        lbl_data = tk.Label(frame_data_hora, text=f'Data: {datetime.now().strftime('%d/%m/%Y')}',
                            font=('Arial', 11), bg='#e7f1ff')
        lbl_data.pack(side=tk.RIGHT)

        # infos
        style_frame = {'bg': '#003594', 'padx': 10, 'pady': 5, 'bd': 2, 'relief': 'groove'}
        frame_bancos = tk.Frame(frame_principal, **style_frame)
        frame_bancos.pack(fill=tk.X, padx=10, pady=5)
        frame_clientes = tk.Frame(frame_principal, **style_frame)
        frame_clientes.pack(fill=tk.X, padx=10, pady=5)
        frame_correntes = tk.Frame(frame_principal, **style_frame)
        frame_correntes.pack(fill=tk.X, padx=10, pady=5)
        frame_poupancas = tk.Frame(frame_principal, **style_frame)
        frame_poupancas.pack(fill=tk.X, padx=10, pady=5)
        frame_total = tk.Frame(frame_principal, **style_frame)
        frame_total.pack(fill=tk.X, padx=10, pady=5)

        self.lbl_bancos = tk.Label(frame_bancos, text=f'Bancos Cadastrados: {len(self.lista_bancos)}',
                                   font=('Arial', 11, 'bold'), fg='white', bg='#003594')
        self.lbl_bancos.pack(pady=5)
        self.lbl_clientes = tk.Label(frame_clientes, text=f'Clientes Ativos: {len(self.lista_clientes)}',
                                     font=('Arial', 11, 'bold'), fg='white', bg='#003594')
        self.lbl_clientes.pack(pady=5)

        self.lbl_correntes = tk.Label(frame_correntes, text=f'Contas Correntes: {self.total_correntes}',
                                      font=('Arial', 11, 'bold'), fg='white', bg='#003594')
        self.lbl_correntes.pack(pady=5)
        self.lbl_poupancas = tk.Label(frame_poupancas, text=f'Contas Poupança: {self.total_poupancas}',
                                      font=('Arial', 11, 'bold'), fg='white', bg='#003594')
        self.lbl_poupancas.pack(pady=5)
        self.lbl_total_caixa = tk.Label(frame_total, text=f'TOTAL EM CAIXA: R$ {self.total_caixa:.2f}',
                                        font=('Arial', 11, 'bold'), fg='white', bg='#003594')
        self. lbl_total_caixa.pack(pady=5)

        # logo
        self.logo = tk.PhotoImage(file='Logo.png')
        lbl_logo = ttk.Label(self.janela, image=self.logo, background='#e7f1ff')
        lbl_logo.pack(pady=20)

        self.atualizar_totais()

    def atualizar_totais(self):
        self.total_bancos = len(self.lista_bancos)
        self.total_clientes = len(self.lista_clientes)
        self.total_caixa, self.total_correntes, self.total_poupancas = 0, 0, 0
        for banco in self.lista_bancos:
            for conta in banco.get_contas():
                self.total_caixa += conta.get_saldo()
                if isinstance(conta, ContaCorrente):
                    self.total_correntes += 1
                elif isinstance(conta, ContaPoupanca):
                    self.total_poupancas += 1

        self.lbl_bancos.config(text=f'Bancos Cadastrados: {self.total_bancos}')
        self.lbl_clientes.config(text=f'Clientes Ativos: {self.total_clientes}')
        self.lbl_correntes.config(text=f'Contas Correntes: {self.total_correntes}')
        self.lbl_poupancas.config(text=f'Contas Poupança: {self.total_poupancas}')
        self.lbl_total_caixa.config(text=f'TOTAL EM CAIXA: R$ {self.total_caixa:.2f}')

    # BANCOS
    def listar_bancos(self):
        funcs_banco.listar_bancos(self)

    def carregar_bancos_treeview(self, treeview_bancos):
        funcs_banco.carregar_bancos_treeview(self, treeview_bancos)

    def cadastrar_banco(self, treeview_bancos):
        funcs_banco.cadastrar_banco(self, treeview_bancos)

    def atualizar_banco(self, treeview_bancos):
        funcs_banco.atualizar_banco(self, treeview_bancos)

    # CLIENTES
    def listar_clientes(self):
        funcs_clientes.listar_clientes(self)

    def cadastrar_cliente(self):
        funcs_clientes.cadastrar_cliente(self)

    def remover_cliente(self):
        funcs_clientes.remover_cliente(self)

    def atualizar_cliente(self):
        funcs_clientes.atualizar_cliente(self)

    # CONTAS
    def listar_contas(self):
        funcs_contas.listar_contas(self)

    def cadastrar_conta_corrente(self):
        funcs_contas.cadastrar_conta_corrente(self)

    def cadastrar_conta_poupanca(self):
        funcs_contas.cadastrar_conta_poupanca(self)

    def encerrar_conta(self):
        funcs_contas.encerrar_conta(self)

    # OPERAÇÕES
    def operacoes(self):
        funcs_operacoes.operacoes(self)

    def saque(self):
        funcs_operacoes.saque(self)

    def deposito(self):
        funcs_operacoes.deposito(self)

    def gerar_relatorio(self):
        funcs_operacoes.gerar_relatorio(self)

    def buscar_conta(self, numero):
        funcs_operacoes.buscar_conta(self, numero)
