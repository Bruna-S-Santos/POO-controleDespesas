
# Arquivo só dos erros personalizados do sistema
# Feito por: Os Lascados
# Se der ruim, é aqui que cai!

class LimiteCategoriaExcedido(Exception):
    """
    Dá esse erro quando você tenta gastar mais do que pode numa categoria
    """
    pass


class SaldoInsuficiente(Exception):
    """
    Dá esse erro quando não tem dinheiro suficiente pra pagar a despesa
    """
    pass
