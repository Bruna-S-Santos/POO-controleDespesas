"""
Categoria - define o tipo de gasto ou receita
Feito por: Os Lascados
Aqui você cria as categorias, tipo 'lanche', 'salário', 'transporte'...
"""


class Categoria:
    def __init__(
        self, nome: str, tipo: str,
        limite_mensal: float = None, descricao: str = ""
    ):
        # Nome da categoria (ex: lanche, salário)
        self._nome = nome
        # Tipo: receita ou despesa
        self.tipo = tipo  # chama o setter
        # Limite mensal (se quiser controlar o gasto)
        self.limite_mensal = limite_mensal
        # Descrição opcional
        self._descricao = descricao

    def __eq__(self, other):
        if not isinstance(other, Categoria):
            return False
        return self.nome == other.nome and self.tipo == other.tipo

    @property
    def nome(self):
        # Pega o nome da categoria
        return self._nome

    @nome.setter
    def nome(self, value):
        # Só aceita nome não vazio e do tipo string
        if not value or not isinstance(value, str):
            raise ValueError(
                "Nome da categoria deve ser uma string não vazia."
            )
        self._nome = value

    @property
    def tipo(self):
        # Pega o tipo da categoria
        return self._tipo

    @tipo.setter
    def tipo(self, value):
        # Só aceita 'receita' ou 'despesa'
        if value not in ("receita", "despesa"):
            raise ValueError(
                "Tipo deve ser 'receita' ou 'despesa'."
            )
        self._tipo = value

    @property
    def limite_mensal(self):
        # Pega o limite mensal da categoria
        return self._limite_mensal

    @limite_mensal.setter
    def limite_mensal(self, value):
        # Só aceita número positivo ou None
        if value is not None and (
            not isinstance(value, (int, float)) or value < 0
        ):
            raise ValueError(
                "Limite mensal deve ser um número positivo ou None."
            )
        self._limite_mensal = value

    @property
    def descricao(self):
        # Pega a descrição da categoria
        return self._descricao

    @descricao.setter
    def descricao(self, value):
        # Se não passar nada, fica vazio
        self._descricao = value or ""

    def __str__(self):
        # Mostra o nome e o tipo da categoria
        return f"{self.nome} ({self.tipo})"

        def __repr__(self):
            return (
                f"Categoria(nome='{self.nome}', tipo='{self.tipo}', "
                f"limite_mensal={self.limite_mensal}, "
                f"descricao='{self.descricao}')"
            )

        def __eq__(self, other):
            if not isinstance(other, Categoria):
                return False
            return self.nome == other.nome and self.tipo == other.tipo
