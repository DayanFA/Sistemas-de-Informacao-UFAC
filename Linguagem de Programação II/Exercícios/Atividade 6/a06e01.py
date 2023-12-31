# Em Python, não existem atributos privados no sentido estrito, mas há uma convenção de 
#adicionar um sublinhado simples (_) como prefixo para indicar que um atributo é "protegido". 
#Entretanto, a modificação e leitura desses atributos ainda é possível, embora não seja 
#considerada uma boa prática fazer isso diretamente. A recomendação é utilizar métodos 
#getters e setters para acessar e modificar atributos.
# Fonte: https://www.alura.com.br/apostila-python-orientacao-a-objetos/encapsulamento
class Cliente:
    # No exemplo, o atributo _nome é protegido, mas ainda é possível acessá-lo
    def __init__(self, n, e, cpf, i): 
        self._nome = n
        self._endereco = e
        self._CPF = cpf
        self._idade = i

    # Métodos getters e setters em baixo
    def get_nome(self):
        return self._nome

    def set_nome(self, novo_nome):
        self._nome = novo_nome