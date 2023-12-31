from banco import Banco
from conta import Conta
from cliente import Cliente
from emprestimo import Emprestimo
class TesteBanco:
    def __init__(self):
        self.banco = Banco(1, "Banco XYZ")

    def criar_clientes_contas(self):
        cliente1 = Cliente("João", "Rua A", "111.444.777-35", 30)
        cliente2 = Cliente("Maria", "Rua B", "222.555.888-46", 25)

        conta1 = Conta(cliente1, 1000, 500)
        conta2 = Conta(cliente2, 2000, 1000)

        self.banco.incluir_conta(conta1)
        self.banco.incluir_conta(conta2)

    def realizar_transacoes(self):
        contas = self.banco._contas
        conta1, conta2 = contas[0], contas[1]

        conta1.depositar(500)  
        conta2.depositar(1000) 

        conta1.sacar(200)  
        conta2.sacar(500)  

        emprestimo1 = Emprestimo(3000, 12, 0.05, conta1)
        emprestimo2 = Emprestimo(2000, 6, 0.03, conta2)

        emprestimo1.pagar_parcela()
        emprestimo2.pagar_parcela()

    def imprimir_relatorio(self):
        self.banco.listar_contas()

    def testar_validacao_cpf(self):
        cliente = Cliente('Nome', 'Endereco', '111.111.111-11', 30)
        try:
            cliente.validarCPF(cliente._CPF)
            print("Teste de validação de CPF passou.")
        except ValueError:
            print("Teste de validação de CPF falhou.")  
                  
    def testar_encerramento_conta(self):
        conta = Conta(Cliente('Nome', 'Endereco', '111.111.111-11', 30), 0, 1000)
        try:
            conta.encerrar_conta()
            print("Teste de encerramento de conta passou.")
        except ValueError:
            print("Teste de encerramento de conta falhou.")

    def testar_emprestimo(self):
        conta = Conta(Cliente('Nome', 'Endereco', '111.111.111-11', 30), 5000, 1000)
        emprestimo = Emprestimo(3000, 13, 0.05, conta)
        emprestimo.pagar_parcela()
        if emprestimo.parcelas_restantes() == 11: 
            print("Teste de empréstimo passou.")
        else:
            print("Teste de empréstimo falhou.")
                
teste_banco = TesteBanco()
teste_banco.criar_clientes_contas()
teste_banco.realizar_transacoes()
teste_banco.imprimir_relatorio()
teste_banco.testar_validacao_cpf()
teste_banco.testar_emprestimo()
teste_banco.testar_encerramento_conta()


