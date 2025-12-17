UNIVERSIDADE FEDERAL DO CARIRI
Curso de Tecnologia em Banco de Dados
ENTREGA 1 - PROJETO DE PROGRAMAÇÃO ORIENTADA A OBJETOS
Equipe: Os Lascados
Integrantes:

Antônia Bruna Silva dos Santos
Francisco Nunes Lopes da Silva
Rodrigo Pereira Oliveira
Professor: Jayr Alencar Pereira
Data: 16/12/2025 (Dados atualizados)

1. Lista das Principais Classes do Sistema
Aqui foram adicionadas aulas essenciais para atender aos requisitos de configurações ( settings.json), interface (CLI) e gerenciamento de múltiplos meses (histórico).

Categoria: Representa categorias financeiras (receita ou despesa), contendo nome, tipo, limite mensal (para despesas) e descrição.
Lancamento (Abstrata): Classe base para registros financeiros. Defina atributos comuns (valor, data, descrição) e a FormaPagamento (Enum).
Receita: Especialização de Lançamento para Entradas Financeiras.
Despesa: Especialização de Lançamento para Saídas. Inclui validação de saldo disponível e verificação de limite da categoria.
OrcamentoMensal: Representa o orçamento de um mês específico. Agrupa os lançamentos daquele mês e calcula os saldos locais.
Gerenciador Financeiro: Controla uma lista de orçamentos (histórico de meses), realiza comparativos entre meses e gerencia a troca de competência vigente.
Alerta: Representa notificações automáticas do sistema (ex: "limite excedido", "déficit orçamentário").
Relacionador: Responsável pela compilação de dados e geração de estatísticas para exibição (ex: gastos por categoria, mês mais econômico).
Configuração: Classe responsável por carregar e salvar parâmetros globais do sistema (arquivo settings.json), como metas de economia e limites de alerta.
InterfaceUsuario (CLI): Gerencia a interação com o usuário via terminal, processando comandos e exibindo menus.
Persistência: Gerencia o salvamento e recuperação de dados (JSON ou SQLite) para orçamentos, categorias e configurações.
2. Descrição das Responsabilidades dos Membros
As responsabilidades foram ajustadas para incluir as novas classes de forma equilibrada.

Antônia Bruna Silva dos Santos
Foco: Núcleo da Modelagem (Domínio Core).
Aulas: Lancamento, Receita, Despesa, Categoria.
Tarefas: Implementação da herança, validações de tipos (setters), criação do Enum de Pagamento e encapsulamento dos dados básicos.
Francisco Nunes Lopes da Silva
Foco: Regras de Negócio e Controle.
Aulas: OrcamentoMensal, GerenciadorFinanceiro, Alerta.
Tarefas: Lógica de cálculo de saldos, gerenciamento de múltiplos meses, lógica de disparo de alertas e verificação de limites.
Rodrigo Pereira Oliveira
Foco: Infraestrutura e Interface.
Aulas: Persistência, Relacionamento, Configuração, InterfaceUsuario.
Tarefas: Leitura/escrita de arquivos, implementação da CLI (menus), carregamento de configurações ( settings.json) e formatação de relatórios.
 
