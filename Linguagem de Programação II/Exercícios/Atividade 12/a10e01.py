from abc import ABC, abstractmethod

# 1. Transforme a classe Forma da aula sobrecarga e substituição de métodos em uma classe abstrata.
class Forma(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

# 2.Transforme a classe Conta da aula sobre herança
# em uma classe abstrata e o método atualiza()
# em um método abstrato. Em seguida, tente
# instanciar um objeto dessa classe.
class Conta(ABC):
    def __init__(self):
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor

    def get_saldo(self):
        return self.saldo

    @abstractmethod
    def atualiza(self, taxa_selic):
        pass

# 3.Crie uma classe ContaInvestimento que herda
# da classe abstrata Conta e implemente o método
# atualiza() para adicionar um percentual de 10%
# do saldo e subtrair um valor fixo de administração
# de R$ 9,99.
class ContaInvestimento(Conta):
    def atualiza(self, taxa_selic):
        self.saldo += self.saldo * 0.10 
        self.saldo -= 9.99  