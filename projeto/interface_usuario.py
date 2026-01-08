"""
InterfaceUsuario - só pra conversar com o usuário
Feito por: Os Lascados
Aqui é onde aparece o menu e lê o que o usuário quer fazer
"""


class InterfaceUsuario:
    @staticmethod
    def exibir_menu():
        # Mostra o menu principal, agora mais bonito!
        print("\n" + "="*40)
        print("   💸  SISTEMA DE DESPESAS PESSOAIS  💸")
        print("="*40)
        print("[1] ➕ Adicionar Receita")
        print("[2] ➖ Adicionar Despesa")
        print("[3] 💰 Ver Saldo do Mês/Ano Atual")
        print("[4] 📅 Ver Saldo de Outro Mês/Ano")
        print("[5] 📊 Relatório de Gastos por Categoria")
        print("[6] 📈 Relatório de Saldos Mensais/Anuais")
        print("[7] 🔄 Trocar Competência (Mês/Ano)")
        print("[8] 🚪 Sair")
        print("="*40)

    @staticmethod
    def ler_opcao():
        # Lê a opção que o usuário digitou
        return input("Escolha uma opção: ")
