from conta import ContaCorrente, ContaInvestimento
from seguro import SeguroDeVida
from manipulador import ManipuladorDeTributaveis
from banco import Banco

cc1 = ContaCorrente(1, 'Cliente 1', 1000)
cc2 = ContaCorrente(2, 'Cliente 2', 2000)
ci = ContaInvestimento(3, 'Cliente 3', 3000)
sdv = SeguroDeVida(4, 4000, 'Cliente 4')

tributaveis = [cc1, cc2, ci, sdv]

manipulador = ManipuladorDeTributaveis()
total_impostos = manipulador.calcular_impostos(tributaveis)
print(f'Total de impostos: {total_impostos}')

banco = Banco(1, 'Banco 1')
banco.adicionar_conta(cc1)
banco.adicionar_conta(cc2)
banco.adicionar_conta(ci)

total_impostos_banco = banco.calcular_impostos(manipulador)
print(f'Total de impostos do banco: {total_impostos_banco}')