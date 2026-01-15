
# Trabalho de POO - Controle de Despesas
# Feito por: Os Lascados
# Aqui é onde tudo acontece! :)

from receita import Receita
from despesa import Despesa
from categoria import Categoria
from forma_pagamento import FormaPagamento
from datetime import date
from gerenciador_financeiro import GerenciadorFinanceiro
from interface_usuario import InterfaceUsuario
from relatorio import Relatorio
from excecoes import LimiteCategoriaExcedido, SaldoInsuficiente
from persistencia import Persistencia

if __name__ == "__main__":
    # Exemplo: criamos duas categorias e lançamentos
    # Só pra mostrar que funciona
    cat_salario = Categoria("Salário", "receita")
    cat_alimentacao = Categoria("Alimentação", "despesa", limite_mensal=1000)

    rec = Receita(
        3000, date.today(), "Salário de dezembro",
        cat_salario, FormaPagamento.PIX
    )
    desp = Despesa(
        50, date.today(), "Almoço",
        cat_alimentacao, FormaPagamento.CARTAO_DEBITO
    )

    print("Exemplo de receita criada:")
    print(rec)
    print("Exemplo de despesa criada:")
    print(desp)

    gf = GerenciadorFinanceiro()
    persist = Persistencia()
    # Tenta carregar os orçamentos salvos, se não tiver, cria um novo
    orcs = persist.carregar()
    if orcs:
        gf.orcamentos = orcs
        gf.competencia_atual = orcs[-1]
        print("Orçamentos carregados do arquivo!")
    else:
        ano, mes = date.today().year, date.today().month
        gf.novo_orcamento(ano, mes)
        print(f"Novo orçamento criado para {mes:02d}/{ano}")

    # Loop principal do menu
    while True:
        print("\nBem-vindo ao sistema de controle de despesas!")
        InterfaceUsuario.exibir_menu()
        opcao = InterfaceUsuario.ler_opcao()
        if opcao == '1':
            print("--- Adicionar Receita ---")
            try:
                ano = int(input("Ano da receita: "))
                mes = int(input("Mês da receita: "))
                valor = float(input("Valor da receita: "))
            except ValueError:
                print("Valor, ano ou mês inválido! Tenta de novo.")
                continue
            desc = input("Descrição: ")
            cat = Categoria(input("Categoria: "), "receita")
            print("\n" + "-"*30)
            print("Escolha a forma de pagamento:")
            print("-"*30)
            opcoes_pagamento = list(FormaPagamento)
            for idx, fp in enumerate(opcoes_pagamento, 1):
                emoji = {
                    'Dinheiro': '💵',
                    'Cartão de Crédito': '💳',
                    'Cartão de Débito': '🏧',
                    'Pix': '⚡',
                    'Outro': '❓'
                }.get(fp.value, '')
                print(f"[{idx}] {emoji} {fp.value}")
            try:
                idx_fp = int(input("Digite o número da forma de pagamento: "))
                forma = opcoes_pagamento[idx_fp - 1]
            except (ValueError, IndexError):
                print("Opção inválida de forma de pagamento!")
                continue
            # Busca ou cria orçamento do mês/ano escolhido
            orc = gf.trocar_competencia(ano, mes)
            receita = Receita(valor, date.today(), desc, cat, forma)
            orc.adicionar_receita(receita)
            print(f"Receita adicionada para {mes:02d}/{ano}!")
        elif opcao == '2':
            print("--- Adicionar Despesa ---")
            try:
                ano = int(input("Ano da despesa: "))
                mes = int(input("Mês da despesa: "))
                valor = float(input("Valor da despesa: "))
            except ValueError:
                print("Valor, ano ou mês inválido! Tenta de novo.")
                continue
            desc = input("Descrição: ")
            cat = Categoria(input("Categoria: "), "despesa")
            print("\n" + "-"*30)
            print("Escolha a forma de pagamento:")
            print("-"*30)
            opcoes_pagamento = list(FormaPagamento)
            for idx, fp in enumerate(opcoes_pagamento, 1):
                emoji = {
                    'Dinheiro': '💵',
                    'Cartão de Crédito': '💳',
                    'Cartão de Débito': '🏧',
                    'Pix': '⚡',
                    'Outro': '❓'
                }.get(fp.value, '')
                print(f"[{idx}] {emoji} {fp.value}")
            try:
                idx_fp = int(input("Digite o número da forma de pagamento: "))
                forma = opcoes_pagamento[idx_fp - 1]
            except (ValueError, IndexError):
                print("Opção inválida de forma de pagamento!")
                continue
            # Busca ou cria orçamento do mês/ano escolhido
            orc = gf.trocar_competencia(ano, mes)
            try:
                despesa = Despesa(valor, date.today(), desc, cat, forma)
                orc.adicionar_despesa(despesa)
                print(f"Despesa adicionada para {mes:02d}/{ano}!")
            except LimiteCategoriaExcedido as e:
                print(f"Erro: {e}")
            except SaldoInsuficiente as e:
                print(f"Erro: {e}")
        elif opcao == '3':
            print("--- Saldo do mês/ano atual ---")
            print(gf.competencia_atual)
            print(f"Saldo disponível: R${gf.competencia_atual.saldo():.2f}")
        elif opcao == '4':
            print("--- Ver Saldo de Outro Mês/Ano ---")
            try:
                ano = int(input("De qual ano você quer ver o saldo? "))
                mes = int(input("E de qual mês? (1-12): "))
            except ValueError:
                print("Ano ou mês inválido!")
                continue
            orc = next(
                (o for o in gf.orcamentos if o.ano == ano and o.mes == mes),
                None
            )
            if not orc:
                print(f"Não há lançamentos para {mes:02d}/{ano}!")
            else:
                print(f"Saldo de {mes:02d}/{ano}: R${orc.saldo():.2f}")
        elif opcao == '5':
            print("--- Relatório de Gastos por Categoria ---")
            try:
                ano = int(input("De qual ano você quer ver o relatório? "))
                mes = int(input("E de qual mês? (1-12): "))
            except ValueError:
                print("Ano ou mês inválido!")
                continue
            orc = next(
                (o for o in gf.orcamentos if o.ano == ano and o.mes == mes),
                None
            )
            if not orc:
                print(f"Não há lançamentos para {mes:02d}/{ano}!")
                continue
            categorias = Relatorio.detalhes_por_categoria(orc)
            if not categorias:
                print("Nenhuma despesa cadastrada!")
            else:
                for cat in sorted(categorias):
                    total = sum(item[1] for item in categorias[cat])
                    print(f"{cat}: R${total:.2f}")
                    for desc, valor, forma in categorias[cat]:
                        print(f"  - {desc} | R${valor:.2f} | {forma}")
        elif opcao == '6':
            print("--- Relatório de Saldos Mensais e Anuais ---")
            # Saldos mensais
            if not gf.orcamentos:
                print("Nenhum orçamento cadastrado!")
            else:
                saldos_ano = {}
                for orc in sorted(gf.orcamentos, key=lambda o: (o.ano, o.mes)):
                    print(
                        f"{orc.mes:02d}/{orc.ano}: Saldo = R${orc.saldo():.2f}"
                    )
                    saldos_ano.setdefault(orc.ano, 0)
                    saldos_ano[orc.ano] += orc.saldo()
                print("\nSaldos por ano:")
                for ano, saldo in saldos_ano.items():
                    print(f"Ano {ano}: Saldo acumulado = R${saldo:.2f}")
        elif opcao == '7':
            print("--- Trocar competência ---")
            try:
                ano = int(input("Ano: "))
                mes = int(input("Mês: "))
            except ValueError:
                print("Ano ou mês inválido!")
                continue
            gf.trocar_competencia(ano, mes)
            print(f"Competência alterada para {mes:02d}/{ano}")
        elif opcao == '8':
            print("Salvando dados... até a próxima!")
            persist.salvar(gf.orcamentos)
            break
        elif opcao == '5':
            print("--- Relatório de Saldos Mensais e Anuais ---")
            # Saldos mensais
            if not gf.orcamentos:
                print("Nenhum orçamento cadastrado!")
            else:
                saldos_ano = {}
                for orc in sorted(gf.orcamentos, key=lambda o: (o.ano, o.mes)):
                    print(
                        f"{orc.mes:02d}/{orc.ano}: Saldo = R${orc.saldo():.2f}"
                    )
                    saldos_ano.setdefault(orc.ano, 0)
                    saldos_ano[orc.ano] += orc.saldo()
                print("\nSaldos por ano:")
                for ano, saldo in saldos_ano.items():
                    print(f"Ano {ano}: Saldo acumulado = R${saldo:.2f}")
        elif opcao == '6':
            print("--- Trocar competência ---")
            try:
                ano = int(input("Ano: "))
                mes = int(input("Mês: "))
            except ValueError:
                print("Ano ou mês inválido!")
                continue
            gf.trocar_competencia(ano, mes)
            print(f"Competência alterada para {mes:02d}/{ano}")
        elif opcao == '7':
            print("Salvando dados... até a próxima!")
            persist.salvar(gf.orcamentos)
            break
        else:
            print("Opção inválida! Digita um número do menu, por favor.")
