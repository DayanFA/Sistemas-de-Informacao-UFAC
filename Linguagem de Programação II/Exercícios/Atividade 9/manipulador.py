from tributavel import TributavelMixin

class ManipuladorDeTributaveis:
    def calcular_impostos(self, lista_tributaveis):
        total = 0
        for t in lista_tributaveis:
            if isinstance(t, TributavelMixin):
                total += t.valor_imposto()
            else:
                print(f"O objeto {type(t).__name__} não é tributável")
        return total