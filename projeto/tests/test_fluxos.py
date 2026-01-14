import pytest
from datetime import date
from categoria import Categoria
from receita import Receita
from despesa import Despesa
from orcamento_mensal import OrcamentoMensal
from gerenciador_financeiro import GerenciadorFinanceiro
from excecoes import LimiteCategoriaExcedido, SaldoInsuficiente
from forma_pagamento import FormaPagamento


def test_categoria_receita_despesa():
    cat_r = Categoria('Salário', 'receita')
    cat_d = Categoria('Alimentação', 'despesa', limite_mensal=500)
    assert cat_r.tipo == 'receita'
    assert cat_d.tipo == 'despesa'
    assert cat_d.limite_mensal == 500


def test_receita_e_despesa():
    cat_r = Categoria('Salário', 'receita')
    cat_d = Categoria('Alimentação', 'despesa', limite_mensal=100)
    r = Receita(1000, date.today(), 'Salário', cat_r, FormaPagamento.PIX)
    d = Despesa(50, date.today(), 'Almoço', cat_d, FormaPagamento.DINHEIRO)
    assert r.valor == 1000
    assert d.valor == 50
    assert r.tipo() == 'receita'
    assert d.tipo() == 'despesa'


def test_limite_categoria_excedido():
    cat = Categoria('Lanche', 'despesa', limite_mensal=10)
    with pytest.raises(LimiteCategoriaExcedido):
        Despesa(
            20, date.today(), 'Lanche caro', cat, FormaPagamento.DINHEIRO
        )


def test_saldo_insuficiente():
    orc = OrcamentoMensal(2026, 1)
    cat_r = Categoria('Salário', 'receita')
    cat_d = Categoria('Alimentação', 'despesa', limite_mensal=100)
    orc.adicionar_receita(
        Receita(50, date.today(), 'Salário', cat_r, FormaPagamento.PIX)
    )
    with pytest.raises(SaldoInsuficiente):
        orc.adicionar_despesa(
            Despesa(60, date.today(), 'Almoço', cat_d, FormaPagamento.DINHEIRO)
        )


def test_orcamento_mensal_saldo():
    orc = OrcamentoMensal(2026, 1)
    cat_r = Categoria('Salário', 'receita')
    cat_d = Categoria('Alimentação', 'despesa', limite_mensal=100)
    orc.adicionar_receita(
        Receita(200, date.today(), 'Salário', cat_r, FormaPagamento.PIX)
    )
    orc.adicionar_despesa(
        Despesa(50, date.today(), 'Almoço', cat_d, FormaPagamento.DINHEIRO)
    )
    assert orc.saldo() == 150


def test_gerenciador_financeiro():
    gf = GerenciadorFinanceiro()
    orc = gf.novo_orcamento(2026, 1)
    assert gf.competencia_atual == orc
    assert orc.ano == 2026 and orc.mes == 1


def test_repr_eq_lt_add():
    cat = Categoria('Salário', 'receita')
    r1 = Receita(100, date(2026, 1, 1), 'A', cat, FormaPagamento.PIX)
    r2 = Receita(200, date(2026, 1, 2), 'B', cat, FormaPagamento.PIX)
    assert repr(r1)
    assert r1 != r2
    assert r1 < r2
    assert (r1 + r2) == 300


def test_alerta_automatico_alto_valor():
    from gerenciador_financeiro import GerenciadorFinanceiro
    gf = GerenciadorFinanceiro()
    gf.novo_orcamento(2026, 1)
    cat_r = Categoria('Salário', 'receita')
    cat = Categoria('Alimentação', 'despesa', limite_mensal=1000)
    gf.competencia_atual.adicionar_receita(
        Receita(1000, date.today(), 'Salário', cat_r, FormaPagamento.PIX)
    )
    d = Despesa(600, date.today(), 'Jantar', cat, FormaPagamento.PIX)
    gf.adicionar_despesa_com_alerta(d)
    assert any('alto valor' in a.mensagem for a in gf.alertas)


def test_alerta_automatico_deficit():
    gf = GerenciadorFinanceiro()
    gf.novo_orcamento(2026, 1)
    cat_r = Categoria('Salário', 'receita')
    cat_d = Categoria('Alimentação', 'despesa', limite_mensal=1000)
    gf.competencia_atual.adicionar_receita(
        Receita(100, date.today(), 'Salário', cat_r, FormaPagamento.PIX)
    )
    gf.competencia_atual.adicionar_receita(
        Receita(50, date.today(), 'Extra', cat_r, FormaPagamento.PIX)
    )
    # Primeiro, zera o saldo
    d1 = Despesa(150, date.today(), 'Jantar', cat_d, FormaPagamento.PIX)
    gf.adicionar_despesa_com_alerta(d1)
    # Agora, tenta adicionar uma despesa para ficar negativo
    d2 = Despesa(50, date.today(), 'Lanche', cat_d, FormaPagamento.PIX)
    try:
        gf.adicionar_despesa_com_alerta(d2)
    except Exception:
        pass
    assert any(
        'Déficit orçamentário' in a.mensagem for a in gf.alertas
    )


def test_categoria_eq():
    c1 = Categoria('Salário', 'receita')
    c2 = Categoria('Salário', 'receita')
    c3 = Categoria('Alimentação', 'despesa')
    assert c1 == c2
    assert c1 != c3
