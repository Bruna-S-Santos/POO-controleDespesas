
"""
Alerta - serve pra avisar o usuário de alguma coisa
Feito por: Os Lascados
Pode ser aviso, erro, ou só informação mesmo
"""


class Alerta:
    def __init__(self, mensagem: str, tipo: str = "info"):
        # Mensagem que vai aparecer pro usuário
        self.mensagem = mensagem
        # Tipo do alerta: info, erro, aviso...
        self.tipo = tipo  # informa aviso e erro

    def __str__(self):
        # Mostra o alerta formatado bonitinho
        return f"[{self.tipo.upper()}] {self.mensagem}"
