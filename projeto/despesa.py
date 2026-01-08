"""
Despesa - representa o gasto do mês
Feito por: Os Lascados
Aqui é onde a grana vai embora!
"""

from lancamento import Lancamento
from excecoes import LimiteCategoriaExcedido


class Despesa(Lancamento):
    def __init__(self, valor, data, descricao, categoria, forma_pagamento):
        super().__init__(valor, data, descricao, categoria, forma_pagamento)
        # Se passar do limite da categoria, já dá erro!
        if (
            categoria.limite_mensal is not None and
            valor > categoria.limite_mensal
        ):
            raise LimiteCategoriaExcedido(
                f"Despesa de R${valor:.2f} excede o limite da categoria "
                f"'{categoria.nome}' (R${categoria.limite_mensal:.2f})"
            )

    def tipo(self):
        # Diz que isso aqui é uma despesa
        return 'despesa'
