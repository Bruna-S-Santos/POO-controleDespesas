# Persistência - salva e carrega os dados do sistema
# Feito por: Os Lascados
# Aqui é onde a mágica acontece pra não perder nada!
import json
from orcamento_mensal import OrcamentoMensal
from receita import Receita
from despesa import Despesa
from categoria import Categoria
from forma_pagamento import FormaPagamento


class Persistencia:
    def __init__(self, caminho_arquivo='orcamentos.json'):
        # Aqui define o nome do arquivo onde tudo vai ser salvo
        self.caminho_arquivo = caminho_arquivo

    def salvar(self, orcamentos):
        # Salva todos os orçamentos no arquivo (receitas e despesas)
        with open(self.caminho_arquivo, 'w') as f:
            json.dump(
                [self._orcamento_para_dict(o) for o in orcamentos],
                f, indent=4, default=str
            )

    def carregar(self):
        # Tenta carregar os dados do arquivo.
        # Se não existir, retorna lista vazia.
        try:
            with open(self.caminho_arquivo, 'r') as f:
                dados = json.load(f)
                return [self._dict_para_orcamento(d) for d in dados]
        except FileNotFoundError:
            return []

    def _orcamento_para_dict(self, orcamento: OrcamentoMensal):
        # Transforma o orçamento em dicionário pra salvar no JSON
        return {
            'ano': orcamento.ano,
            'mes': orcamento.mes,
            'receitas': [
                self._lancamento_para_dict(r)
                for r in orcamento.receitas
            ],
            'despesas': [
                self._lancamento_para_dict(d)
                for d in orcamento.despesas
            ]
        }

    def _lancamento_para_dict(self, lanc):
        # Transforma cada lançamento em dicionário
        return {
            'valor': lanc.valor,
            'data': lanc.data.isoformat(),
            'descricao': lanc.descricao,
            'categoria': {
                'nome': lanc.categoria.nome,
                'tipo': lanc.categoria.tipo,
                'limite_mensal': lanc.categoria.limite_mensal,
                'descricao': lanc.categoria.descricao
            },
            'forma_pagamento': lanc.forma_pagamento.name,
            'tipo': lanc.tipo()
        }

    def _dict_para_orcamento(self, d):
        # Reconstrói o orçamento a partir do dicionário lido do JSON
        o = OrcamentoMensal(d['ano'], d['mes'])
        for r in d.get('receitas', []):
            cat = Categoria(
                r['categoria']['nome'],
                r['categoria']['tipo'],
                r['categoria'].get('limite_mensal'),
                r['categoria'].get('descricao', '')
            )
            receita = Receita(
                r['valor'],
                self._parse_data(r['data']),
                r['descricao'],
                cat,
                FormaPagamento[r['forma_pagamento']]
            )
            o.adicionar_receita(receita)
        for d_ in d.get('despesas', []):
            cat = Categoria(
                d_['categoria']['nome'],
                d_['categoria']['tipo'],
                d_['categoria'].get('limite_mensal'),
                d_['categoria'].get('descricao', '')
            )
            despesa = Despesa(
                d_['valor'],
                self._parse_data(d_['data']),
                d_['descricao'],
                cat,
                FormaPagamento[d_['forma_pagamento']]
            )
            o.adicionar_despesa(despesa)
        return o

    def _parse_data(self, data_str):
        # Converte a data do formato texto para objeto date
        from datetime import date
        return date.fromisoformat(data_str)
