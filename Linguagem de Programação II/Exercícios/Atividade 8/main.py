from presidente import Presidente
from gerente import Gerente
from diretor import Diretor
from secretaria import SecretariaExecutiva, SecretariaAdministrativa

presidente = Presidente(5000)
gerente = Gerente(5000)
diretor = Diretor(5000)
secretaria_executiva = SecretariaExecutiva(3000)
secretaria_administrativa = SecretariaAdministrativa(2000)

print("Bonificação do Presidente: ", presidente.get_bonus())
print("Bonificação do Gerente: ", gerente.get_bonus())
print("Bonificação do Diretor: ", diretor.get_bonus())
print("Bonificação da Secretária Executiva: ", secretaria_executiva.get_bonus())
print("Bonificação da Secretária Administrativa: ", secretaria_administrativa.get_bonus())