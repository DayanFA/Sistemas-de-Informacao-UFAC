# 5)
# Para criar uma classe ContaInvestimento, não precisaria alterar o método atualizar_contas(), 
# desde que a classe ContaInvestimento tenha um método atualiza().

# 7) 
# Tentar passar uma instância de uma classe que não é filha de Conta no método atualizar_contas(), 
# vai receberá um AttributeError, pois a instância não terá o método atualiza().

# 8)
# Já fiz polimorfismo. As classes ContaCorrente, ContaPoupanca e ContaEspecial são subclasses de Conta e cada uma delas tem uma implementação 
# diferente do método atualiza(). Isso é um exemplo de polimorfismo, pois o mesmo método tem comportamentos diferentes dependendo 
# da classe do objeto que o está chamando.

from banco import Banco
from conta import Conta, ContaCorrente, ContaPoupanca, ContaEspecial

banco = Banco(1, 'Meu Banco')
conta1 = ContaCorrente(1, 'Cliente 1', 1000)
conta2 = ContaPoupanca(2, 'Cliente 2', 2000)
conta3 = ContaEspecial(3, 'Cliente 3', 3000, 500)

banco._listaContas.append(conta1)
banco._listaContas.append(conta2)
banco._listaContas.append(conta3)

banco.atualizar_contas(0.01)

print(conta1)
print(conta2)
print(conta3)