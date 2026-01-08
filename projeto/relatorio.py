
# Relatório - Funções para mostrar os gastos do mês
# Feito por: Os Lascados
# Aqui é só pra organizar e facilitar a vida na hora de ver os gastos

from orcamento_mensal import OrcamentoMensal
from typing import List, Dict


class Relatorio:
    # Esse método mostra todas as despesas separadas por categoria.
    # Inclui descrição, valor e forma de pagamento.
    # Bem útil pra saber onde gastou!
    @staticmethod
    def detalhes_por_categoria(orcamento: OrcamentoMensal):
        """
        Retorna um dicionário:
        {categoria: [ (descricao, valor, forma_pagamento), ... ] }
        """
        categorias = {}
        for despesa in orcamento.despesas:
            nome = despesa.categoria.nome
            if nome not in categorias:
                categorias[nome] = []
            categorias[nome].append(
                (
                    despesa.descricao,
                    despesa.valor,
                    despesa.forma_pagamento.value
                )
            )
        return categorias

    # Esse aqui só mostra o total gasto por categoria, sem detalhes
    @staticmethod
    def gastos_por_categoria(
        orcamento: OrcamentoMensal
    ) -> Dict[str, float]:
        categorias = {}
        for despesa in orcamento.despesas:
            nome = despesa.categoria.nome
            categorias[nome] = categorias.get(nome, 0) + despesa.valor
        return categorias

    # Esse aqui retorna o mês que teve o maior saldo (mais econômico)
    @staticmethod
    def mes_mais_economico(
        orcamentos: List[OrcamentoMensal]
    ) -> OrcamentoMensal:
        return min(orcamentos, key=lambda o: o.saldo(), default=None)
