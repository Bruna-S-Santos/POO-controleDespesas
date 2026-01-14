

# Receita - representa tudo que entra de dinheiro no sistema
# Feito por: Os Lascados
# Aqui é só pra facilitar a vida e separar o que é receita

from lancamento import Lancamento


class Receita(Lancamento):
    """
    Classe para lançamentos de receita.
    Aqui só entra dinheiro: salário, mesada, bico, etc.
    """

    def tipo(self) -> str:
        # Só pra diferenciar na hora de mostrar no menu
        return 'receita'

    def __repr__(self):
        return Lancamento.__repr__(self)

    def __eq__(self, other):
        return Lancamento.__eq__(self, other)

    def __lt__(self, other):
        return Lancamento.__lt__(self, other)

    def __add__(self, other):
        return Lancamento.__add__(self, other)
