"""
OrcamentoMensal - guarda tudo que acontece no mês
Feito por: Os Lascados
Aqui ficam as receitas e despesas de cada mês, pra não se perder!
"""
from receita import Receita
from despesa import Despesa
from typing import List
from excecoes import SaldoInsuficiente


class OrcamentoMensal:
    def __init__(self, ano: int, mes: int):
        # Guarda o ano e o mês desse orçamento
        self.ano = ano
        self.mes = mes
        # Listas para receitas e despesas do mês
        self.receitas: List[Receita] = []
        self.despesas: List[Despesa] = []

    def adicionar_receita(self, receita: Receita):
        # Adiciona uma receita na lista
        self.receitas.append(receita)

    def adicionar_despesa(self, despesa: Despesa):
        # Só adiciona se tiver saldo suficiente
        if despesa.valor > self.saldo():
            raise SaldoInsuficiente(
                f"Saldo insuficiente para despesa de R${despesa.valor:.2f}. "
                f"Saldo disponível: R${self.saldo():.2f}"
            )
        self.despesas.append(despesa)

    def saldo(self) -> float:
        # Calcula o saldo do mês (receitas - despesas)
        total_receitas = sum(r.valor for r in self.receitas)
        total_despesas = sum(d.valor for d in self.despesas)
        return total_receitas - total_despesas

    def __str__(self):
        # Mostra o mês/ano e o saldo formatado
        return (
            f"Orçamento {self.mes:02d}/{self.ano} | "
            f"Saldo: R${self.saldo():.2f}"
        )
