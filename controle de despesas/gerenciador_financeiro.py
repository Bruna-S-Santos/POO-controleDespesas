"""
GerenciadorFinanceiro - controla tudo dos orçamentos
Feito por: Os Lascados
Aqui é onde a bagunça vira organização!
"""

from orcamento_mensal import OrcamentoMensal
from typing import List


class GerenciadorFinanceiro:
    def __init__(self):
        # Lista de todos os orçamentos (um pra cada mês/ano)
        self.orcamentos: List[OrcamentoMensal] = []
        # O orçamento que tá sendo usado agora
        self.competencia_atual: OrcamentoMensal = None

    def novo_orcamento(self, ano: int, mes: int):
        # Cria um novo orçamento pra um mês/ano
        orcamento = OrcamentoMensal(ano, mes)
        self.orcamentos.append(orcamento)
        self.competencia_atual = orcamento
        return orcamento

    def registrar_alerta(self, mensagem, tipo="info"):
        from alerta import Alerta
        if not hasattr(self, "alertas"):
            self.alertas = []
        self.alertas.append(Alerta(mensagem, tipo))

    def adicionar_despesa_com_alerta(self, despesa):
        # Despesa acima de R$500
        if despesa.valor > 500:
            self.registrar_alerta(
                f"Despesa de alto valor: R${despesa.valor:.2f} - "
                f"{despesa.descricao}",
                "aviso"
            )
        # Limite excedido já é tratado na classe Despesa (exceção)
        try:
            self.competencia_atual.adicionar_despesa(despesa)
        except Exception as e:
            self.registrar_alerta(str(e), "erro")
            # Se for saldo insuficiente, registra alerta de déficit
            if "Saldo insuficiente" in str(e):
                self.registrar_alerta(
                    f"Déficit orçamentário no mês "
                    f"{self.competencia_atual.mes:02d}/"
                    f"{self.competencia_atual.ano}",
                    "erro"
                )
            raise
        # Saldo negativo (caso permitido)
        if self.competencia_atual.saldo() < 0:
            self.registrar_alerta(
                f"Déficit orçamentário no mês "
                f"{self.competencia_atual.mes:02d}/"
                f"{self.competencia_atual.ano}",
                "erro"
            )

    def trocar_competencia(self, ano: int, mes: int):
        # Troca pro orçamento de outro mês/ano
        for o in self.orcamentos:
            if o.ano == ano and o.mes == mes:
                self.competencia_atual = o
                return o
        # Se não existir, cria um novo
        return self.novo_orcamento(ano, mes)

    def saldo_total(self):
        # Soma o saldo de todos os meses
        return sum(o.saldo() for o in self.orcamentos)

    def comparar_meses(self, ano1, mes1, ano2, mes2):
        # Compara o saldo de dois meses diferentes
        o1 = next(
            (o for o in self.orcamentos if o.ano == ano1 and o.mes == mes1),
            None
        )
        o2 = next(
            (o for o in self.orcamentos if o.ano == ano2 and o.mes == mes2),
            None
        )
        if o1 and o2:
            return o1.saldo() - o2.saldo()
        return None
