class Cliente:
    __slots__ = ['_nome', '_endereco', '_CPF', '_idade']

    def __init__(self, n, e, cpf, i):
        self._nome = n
        self._endereco = e
        self._CPF = self.validarCPF(cpf)
        self._idade = i

    def validarCPF(self, cpf):
        cpf = ''.join(filter(str.isdigit, cpf))

        if len(cpf) != 11:
            raise ValueError("CPF deve conter 11 dígitos numéricos.")

        soma = 0
        for i in range(9):
            soma += int(cpf[i]) * (10 - i)
        resto = soma % 11
        digito_verificador1 = 0 if resto < 2 else 11 - resto

        if digito_verificador1 != int(cpf[9]):
            raise ValueError("CPF inválido. Primeiro dígito verificador incorreto.")

        soma = 0
        for i in range(10):
            soma += int(cpf[i]) * (11 - i)
        resto = soma % 11
        digito_verificador2 = 0 if resto < 2 else 11 - resto

        if digito_verificador2 != int(cpf[10]):
            raise ValueError("CPF inválido. Segundo dígito verificador incorreto.")

        return cpf
