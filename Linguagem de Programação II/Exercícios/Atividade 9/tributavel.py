import abc

class TributavelMixin(abc.ABC):
    @abc.abstractmethod
    def valor_imposto(self):
        pass