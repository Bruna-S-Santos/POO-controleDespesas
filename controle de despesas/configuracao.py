"""
Configuracao - salva e carrega as configurações do sistema
Feito por: Os Lascados
Aqui é onde guarda as preferências, tipo onde salva os dados
"""

import json


class Configuracao:
    def __init__(self, caminho_arquivo='settings.json'):
        # Caminho do arquivo de configurações
        self.caminho_arquivo = caminho_arquivo
        # Dicionário pra guardar os parâmetros
        self.parametros = {}
        self.carregar()

    def carregar(self):
        # Tenta carregar as configurações do arquivo
        try:
            with open(self.caminho_arquivo, 'r') as f:
                self.parametros = json.load(f)
        except FileNotFoundError:
            # Se não achar o arquivo, começa vazio
            self.parametros = {}

    def salvar(self):
        # Salva as configurações no arquivo
        with open(self.caminho_arquivo, 'w') as f:
            json.dump(self.parametros, f, indent=4)

    def get(self, chave, padrao=None):
        # Pega o valor de uma configuração, se não tiver retorna o padrão
        return self.parametros.get(chave, padrao)

    def set(self, chave, valor):
        # Define um valor e já salva no arquivo
        self.parametros[chave] = valor
        self.salvar()
