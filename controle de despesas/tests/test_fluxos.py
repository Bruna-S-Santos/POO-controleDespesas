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
    # Testa se a categoria de receita e despesa
    # está sendo criada corretamente
    cat_r = Categoria('Salário', 'receita')
    cat_d = Categoria('Alimentação', 'despesa', limite_mensal=500)
    assert cat_r.tipo == 'receita'
    assert cat_d.tipo == 'despesa'
    assert cat_d.limite_mensal == 500


def test_receita_e_despesa():
    # Testa se as classes Receita e Despesa estão funcionando
    # e retornando os valores certos
    cat_r = Categoria('Salário', 'receita')
    cat_d = Categoria('Alimentação', 'despesa', limite_mensal=100)
    r = Receita(1000, date.today(), 'Salário', cat_r, FormaPagamento.PIX)
    d = Despesa(50, date.today(), 'Almoço', cat_d, FormaPagamento.DINHEIRO)
    assert r.valor == 1000
    assert d.valor == 50
    assert r.tipo() == 'receita'
    assert d.tipo() == 'despesa'


def test_limite_categoria_excedido():
    # Testa se a exceção é lançada quando o valor da despesa
    # passa do limite da categoria
    cat = Categoria('Lanche', 'despesa', limite_mensal=10)
    with pytest.raises(LimiteCategoriaExcedido):
        Despesa(
            20, date.today(), 'Lanche caro', cat, FormaPagamento.DINHEIRO
        )


def test_saldo_insuficiente():
    # Testa se a exceção de saldo insuficiente é lançada
    # ao tentar gastar mais do que tem
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
    # Testa se o saldo do orçamento mensal está correto
    # após receitas e despesas
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
    # Testa se o gerenciador financeiro cria um novo orçamento
    # corretamente
    gf = GerenciadorFinanceiro()
    orc = gf.novo_orcamento(2026, 1)
    assert gf.competencia_atual == orc
    assert orc.ano == 2026 and orc.mes == 1


def test_repr_eq_lt_add():
    # Testa os métodos mágicos de representação, igualdade,
    # menor que e soma das receitas
    cat = Categoria('Salário', 'receita')
    r1 = Receita(100, date(2026, 1, 1), 'A', cat, FormaPagamento.PIX)
    r2 = Receita(200, date(2026, 1, 2), 'B', cat, FormaPagamento.PIX)
    assert repr(r1)
    assert r1 != r2
    assert r1 < r2
    assert (r1 + r2) == 300


def test_alerta_automatico_alto_valor():
    # Testa se o alerta de alto valor é gerado automaticamente
    # ao adicionar uma despesa alta
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
    # Testa se o alerta de déficit orçamentário é gerado
    # quando o saldo fica negativo
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
    # O método pode lançar exceção, mas queremos apenas garantir o alerta
    try:
        gf.adicionar_despesa_com_alerta(d2)
    except Exception:
        pass
    assert any(
        'Déficit orçamentário' in a.mensagem for a in gf.alertas
    )


def test_categoria_eq():
    # Testa se a comparação de igualdade entre categorias
    # funciona corretamente
    c1 = Categoria('Salário', 'receita')
    c2 = Categoria('Salário', 'receita')
    c3 = Categoria('Alimentação', 'despesa')
    assert c1 == c2
    assert c1 != c3

