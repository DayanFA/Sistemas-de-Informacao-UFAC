salario=float(input('Digite o salário:'))
if 1000 <=salario <=15000:
     inss=salario*0.11
     imposto_renda=salario*0.275
     print('INSS:', inss, 'Imposto de Renda', imposto_renda)
     print('Salário Líquido:', (salario-inss-imposto_renda))
else:
     print('Salário está fora da facha de impostos')