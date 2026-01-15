
# Enum pra guardar as formas de pagamento que o povo usa
# Feito por: Os Lascados
# Se inventar outra forma, só colocar aqui!
from enum import Enum


class FormaPagamento(Enum):
    DINHEIRO = 'Dinheiro'           # Pagou na mão
    CARTAO_CREDITO = 'Cartão de Crédito'  # Parcelou ou passou no crédito
    CARTAO_DEBITO = 'Cartão de Débito'    # Passou no débito
    PIX = 'Pix'                     # Transferência rápida
    OUTRO = 'Outro'                 # Qualquer coisa diferente
