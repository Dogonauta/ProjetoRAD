# Sistema de Gerenciamento de Clientes com Interface Gráfica

Este é um projeto de Sistema de Gerenciamento de Clientes desenvolvido com a metodologia RAD (Rapid Application Development). Utilizando Python, PostgreSQL e Tkinter, o sistema permite operações CRUD (Create, Read, Update, Delete) em uma interface gráfica intuitiva e acessível. 

## Índice

- [Descrição do Projeto](#descrição-do-projeto)
- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Como Executar o Projeto](#como-executar-o-projeto)
- [Metodologia - RAD](#metodologia---rad)
- [Modelagem de Dados e Negócio](#modelagem-de-dados-e-negócio)
- [Feito por](#feito-por)

---

## Descrição do Projeto

Este projeto visa desenvolver um sistema para empresas de pequeno e médio porte que buscam uma solução simples para o gerenciamento de clientes. Com o sistema, é possível cadastrar novos clientes, consultar e listar informações, alterar dados e excluir registros de maneira rápida e segura. O sistema foi estruturado seguindo a metodologia RAD, que favorece a criação de protótipos e o aprimoramento contínuo das funcionalidades.

## Funcionalidades

- **Cadastro de Clientes**: Registra clientes com código, CPF, nome e idade.
- **Limitação de CPF**: Implementação da função `limitar_cpf` para assegurar que o CPF seja composto de até 11 dígitos numéricos, filtrando qualquer entrada incorreta.
- **Consulta e Listagem**: Exibe todos os clientes em uma interface de lista, com busca e ordenação.
- **Alteração de Dados**: Permite a edição de dados de clientes selecionados, com confirmação de alteração.
- **Exclusão de Clientes**: Exclui clientes da base de dados, após confirmação do usuário.

## Tecnologias Utilizadas

- **Python 3.x**: Linguagem principal do projeto.
- **PostgreSQL**: Banco de dados relacional utilizado para armazenar os dados dos clientes.
- **Tkinter**: Biblioteca padrão do Python para criação da interface gráfica.
- **psycopg2**: Biblioteca que permite a comunicação entre Python e PostgreSQL.

## Estrutura do Projeto

```bash
├── main.py       # Inicializa o sistema e executa a interface gráfica.
├── funcoes.py    # Contém funções para conexão e operações CRUD com o banco de dados.
├── interface.py  # Define a interface gráfica usando Tkinter.
├── classes.py    # Define a classe Cliente.
└── README.md     # Documentação do projeto.
```

**Explicação dos Arquivos**

 - `main.py`: Este arquivo inicializa o sistema e executa as operações principais.
 
 - `funcoes.py`: O módulo funcoes.py é responsável por todas as operações relacionadas ao banco de dados.

 - `interface.py`: O módulo interface.py define a interface gráfica utilizando Tkinter e permite que o usuário interaja de forma intuitiva com o sistema.

 - `classes.py`: Arquivo responsável por definir a classe Cliente, usada para organizar as informações dos clientes no sistema.

 
## Como Executar o Projeto

**Clone o repositório:**

```bash
git clone https://github.com/seu-usuario/sistema-gerenciamento-clientes.git
cd sistema-gerenciamento-clientes
```

**Instale as dependências:** Certifique-se de que o PostgreSQL e a biblioteca psycopg2 estão instalados.

**Configure o Banco de Dados:** Verifique se o PostgreSQL está em execução e crie um banco de dados com o nome postgres ou altere a configuração no arquivo funcoes.py.

**Execute o programa:** No terminal, execute o seguinte comando:

```bash
python main.py
```
## Metodologia - RAD
O projeto foi desenvolvido com a metodologia RAD, que inclui as seguintes fases:

**1. Planejamento e Definição de Requisitos:** Identificação das necessidades do sistema, como cadastro e consulta de clientes.

**2. Modelagem de Negócio:** Definição do fluxo de operações, garantindo que cada funcionalidade atendesse aos requisitos.

**3. Modelagem de Dados:** Estruturação do banco de dados para suportar as operações CRUD, com a tabela cadastro contendo codigo, cpf, nome e idade.

**4. Construção Rápida:** Desenvolvimento modular em arquivos Python, com testes e ajustes frequentes.

**5. Testes e Validação:** Verificação da funcionalidade de cada operação, especialmente a integridade da interface gráfica e a confirmação das operações críticas.

**6. Feedback e Ajustes:** Melhorias contínuas baseadas em feedback até a versão final.

## Modelagem de Dados e Negócio

### Estrutura da Tabela `cadastro`

| Campo  | Tipo        | Descrição                 |
|--------|-------------|---------------------------|
| codigo | INT (PK)    | Identificador único       |
| cpf    | VARCHAR(11) | CPF do cliente            |
| nome   | TEXT        | Nome completo do cliente  |
| idade  | INT         | Idade do cliente          |

## Modelagem de Negócio

**1. Cadastro:** Insere dados do cliente na tabela cadastro.

**2. Consulta e Listagem:** Exibe todos os registros com opções de busca e ordenação.

**3. Alteração:** Permite atualizar dados de clientes selecionados com confirmação.

**4. Exclusão:** Remove registros após confirmação do usuário.

## Feito por :

|[<img src="arquivos_projeto/assents/eu.png" width=115><br> Gabriel França </sub>](https://github.com/dogonauta)
| :---: |
