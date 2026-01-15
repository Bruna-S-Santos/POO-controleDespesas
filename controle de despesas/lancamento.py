
# Essa classe é tipo a base pra tudo que é lançamento (receita ou despesa)
# Feito por: Os Lascados
# Aqui a gente guarda o valor, data, descrição, categoria e forma de pagamento
from abc import ABC, abstractmethod
from datetime import date
from forma_pagamento import FormaPagamento
from categoria import Categoria


class Lancamento(ABC):
    def __add__(self, other):
        if not isinstance(other, Lancamento):
            return NotImplemented
        if self.tipo() != other.tipo():
            raise TypeError("Só é possível somar lançamentos do mesmo tipo.")
        return self.valor + other.valor

    def __le__(self, other):
        return self.data <= other.data

    def __gt__(self, other):
        return self.data > other.data

    def __ge__(self, other):
        return self.data >= other.data

    def __init__(
        self, valor: float, data: date, descricao: str,
        categoria: Categoria, forma_pagamento: FormaPagamento
    ):
        # Quando cria um lançamento, já coloca tudo que precisa
        self.valor = valor
        self.data = data
        self.descricao = descricao
        self.categoria = categoria
        self.forma_pagamento = forma_pagamento

    @property
    def valor(self):
        # Pega o valor do lançamento
        return self._valor

    @valor.setter
    def valor(self, value):
        # Só aceita número positivo, senão dá ruim!
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError(
                "Valor deve ser um número positivo."
            )
        self._valor = value

    @property
    def data(self):
        # Pega a data do lançamento
        return self._data

    @data.setter
    def data(self, value):
        # Tem que ser uma data certinha
        if not isinstance(value, date):
            raise ValueError(
                "Data deve ser um objeto datetime.date."
            )
        self._data = value

    @property
    def descricao(self):
        # Pega a descrição (pode ser vazio)
        return self._descricao

    @descricao.setter
    def descricao(self, value):
        # Se não passar nada, fica vazio
        self._descricao = value or ""

    @property
    def categoria(self):
        # Pega a categoria do lançamento
        return self._categoria

    @categoria.setter
    def categoria(self, value):
        # Tem que ser uma categoria válida
        if not isinstance(value, Categoria):
            raise ValueError(
                "Categoria deve ser uma instância de Categoria."
            )
        self._categoria = value

    @property
    def forma_pagamento(self):
        # Pega a forma de pagamento
        return self._forma_pagamento

    @forma_pagamento.setter
    def forma_pagamento(self, value):
        # Tem que ser uma forma de pagamento válida
        if not isinstance(value, FormaPagamento):
            raise ValueError(
                "Forma de pagamento deve ser uma instância de FormaPagamento."
            )
        self._forma_pagamento = value

    @abstractmethod
    def tipo(self):
        # Cada lançamento tem um tipo (receita ou despesa)
        pass

    def __str__(self):
        # Mostra tudo bonitinho pra imprimir na tela
        return (
            f"{self.data} | {self.categoria.nome} | {self.valor:.2f} | "
            f"{self.descricao} | {self.forma_pagamento.value}"
        )

        def __repr__(self):
            return (
                f"Lancamento(valor={self.valor}, data={self.data}, "
                f"descricao='{self.descricao}', "
                f"categoria={repr(self.categoria)}, "
                f"forma_pagamento={self.forma_pagamento})"
            )

        def __eq__(self, other):
            if not isinstance(other, Lancamento):
                return False
            return (
                self.data == other.data and self.descricao == other.descricao
            )

        def __lt__(self, other):
            if not isinstance(other, Lancamento):
                return NotImplemented
            return self.data < other.data

        def __add__(self, other):
            if not isinstance(other, Lancamento):
                return NotImplemented
            if self.tipo() != other.tipo():
                raise TypeError(
                    "Só é possível somar lançamentos do mesmo tipo."
                )
            return self.valor + other.valor
