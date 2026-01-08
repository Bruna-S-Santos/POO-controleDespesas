# UNIVERSIDADE FEDERAL DO CARIRI
# UNIVERSIDADE FEDERAL DO CARIRI
## Projeto de POO - Controle de Despesas

**Grupo:** Os Lascados
Bruna, Nunes, Rodrigo

**Professor:** Jayr
**Data:** 16/12/2025

---

## Sobre o Projeto
Esse trabalho é um sistema simples para controlar receitas e despesas do mês, feito em Python usando orientação a objetos. Tudo funciona pelo terminal, então é só rodar e usar o menu.

### Principais Classes
- Categoria: define se é receita ou despesa, tem nome, tipo, limite e descrição.
- Lancamento: classe base para receitas e despesas, guarda valor, data, descrição, categoria e forma de pagamento.
- Receita: herda de Lancamento, serve pra entradas de dinheiro.
- Despesa: herda de Lancamento, serve pra saídas, valida limite e saldo.
- OrcamentoMensal: guarda receitas e despesas de um mês, calcula saldo.
- GerenciadorFinanceiro: controla vários meses, troca competência.
- Alerta: mostra avisos tipo limite excedido.
- Relatorio: gera estatísticas, tipo gastos por categoria.
- Configuracao: salva e carrega configs do sistema.
- InterfaceUsuario: mostra menu e lê opção do usuário.
- Persistencia: salva e carrega dados em JSON.

---

## Quem fez o quê

Bruna: modelagem das classes principais (Lancamento, Receita, Despesa, Categoria)
Nunes: regras de negócio, controle de meses, alertas
Rodrigo: persistência, relatórios, configuração, interface

---
- **Foco:** Núcleo da Modelagem (Core Domain).
- **Classes:** Lancamento, Receita, Despesa, Categoria.
- **Tarefas:** Implementação da herança, validações de tipos (setters), criação do Enum de Pagamento e encapsulamento dos dados básicos.

### Francisco Nunes Lopes da Silva
- **Foco:** Regras de Negócio e Controle.
- **Classes:** OrcamentoMensal, GerenciadorFinanceiro, Alerta.
- **Tarefas:** Lógica de cálculo de saldos, gerenciamento de múltiplos meses, lógica de disparo de alertas e verificação de limites.

### Rodrigo Pereira Oliveira
- **Foco:** Infraestrutura e Interface.
- **Classes:** Persistencia, Relatorio, Configuracao, InterfaceUsuario.
- **Tarefas:** Leitura/escrita de arquivos, implementação da CLI (menus), carregamento de configurações (`settings.json`) e formatação dos relatórios.

---

## Diagrama UML (textual)

Diagrama UML (bem simples, só pra ilustrar):

Categoria
   |
Lancamento (base)
   |-- Receita
   |-- Despesa
OrcamentoMensal
GerenciadorFinanceiro
Relatorio
Configuracao
Persistencia
InterfaceUsuario
Alerta
excecoes.py

---

---

## Instruções de Instalação e Execução

Como rodar:
1. Baixe o projeto (pode usar git clone se quiser)
2. Se quiser, crie um ambiente virtual (python3 -m venv venv)
3. Rode o main.py (python3 main.py)


## Exemplo de Uso


Quando rodar, vai aparecer um menu no terminal:
- Adicionar receita (você escolhe o mês/ano da receita)
- Adicionar despesa (também escolhe o mês/ano da despesa)
- Ver saldo do mês/ano atual
- Ver saldo de outro mês/ano (dá pra consultar qualquer período)
- Relatório de gastos por categoria (mostra quanto gastou em cada coisa)
- Relatório de saldos mensais/anuais (dá pra ver o saldo de cada mês e cada ano)
- Trocar competência (mês/ano) para lançar ou consultar dados de outro período
- Sair (salva tudo)


## Dicas e Funcionamento (pra não se perder)

- **Categoria:** é tipo um grupo pra organizar suas receitas e despesas. Exemplo: "Alimentação", "Transporte", "Salário". Quando for cadastrar uma receita ou despesa, você coloca a categoria pra depois ver quanto gastou em cada coisa.
- **Receita:** tudo que entra de dinheiro (ex: salário, mesada, venda de algo).
- **Despesa:** tudo que sai (ex: conta de luz, lanche, transporte).
- **Limite da categoria:** se quiser, pode colocar um valor máximo pra gastar numa categoria (tipo, não gastar mais de 200 reais com lanche no mês). Se passar, o sistema avisa.

- **Competência:** é o mês/ano que você está controlando. Dá pra trocar e ver outros meses e anos, tanto pra lançar quanto pra consultar receitas/despesas.
- **Datas:** sempre que for lançar uma receita ou despesa, você escolhe o mês e o ano certinho. Assim, dá pra organizar tudo por período e consultar depois.
- **Relatório:** mostra quanto você gastou em cada categoria no mês, e também tem opção de ver o saldo de cada mês/ano.
- **Saldo:** dá pra ver o saldo do mês/ano atual ou consultar o saldo de qualquer outro mês/ano que já cadastrou.
- **Tudo é salvo automaticamente** quando você escolhe sair, então não precisa se preocupar em perder os dados.


Qualquer dúvida, só mexer no menu e testar! Se errar, o sistema avisa e você pode tentar de novo. Dá pra cadastrar receitas/despesas em qualquer mês/ano, consultar saldos antigos, ver relatórios detalhados e controlar tudo certinho!


## Dados de Teste

Os dados são todos cadastrados pelo menu, não tem nada automático.


## Decisões de Design

O sistema usa orientação a objetos, tem exceções próprias, salva tudo em JSON e pode ser adaptado pra SQLite se quiser. O menu é simples pra facilitar a vida.

---

---
