# Sistema de Cadastro e Gerenciamento de Clientes

Este é um projeto simples de sistema de cadastro e gerenciamento de clientes, desenvolvido em Python e utilizando SQLite como banco de dados. O sistema permite a inserção, alteração, consulta e exclusão de clientes.

## Índice

- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Como Executar o Projeto](#como-executar-o-projeto)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Contribuições](#contribuições)
- [Licença](#licença)

## Funcionalidades

- **Cadastro de clientes**: Insere novos clientes no banco de dados.
- **Listar clientes**: Exibe todos os clientes cadastrados.
- **Alterar dados**: Permite modificar informações de um cliente existente.
- **Excluir cliente**: Remove um cliente do banco de dados.
- **Confirmações de ações críticas**: Garante que alterações e exclusões não sejam feitas sem uma confirmação prévia.

## Tecnologias Utilizadas

- **Python 3.x**: Linguagem de programação principal do projeto.
- **SQLite**: Banco de dados relacional leve para armazenar os dados dos clientes.
- **Bibliotecas**:

  - `sqlite3`: Para manipulação do banco de dados.

  - `classes`: Módulo personalizado com as classes usadas no sistema.

## Como Executar o Projeto

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio

2. **Crie o banco de dados SQLite**: O banco de dados será criado automaticamente quando o sistema for executado pela primeira vez.

3. **Execute o programa**: No terminal, execute o arquivo principal:
    ``` bash
    python main.py

4. **Utilize o sistema**:

 - O sistema irá solicitar as ações de cadastro, alteração, exclusão ou listagem de clientes.

 **Estrutura do Projeto**

   ```bash
    ├── classes.py         # Define as classes Cliente e outras, caso necessário.
    ├── main.py            # Arquivo principal com as funções CRUD e lógica do sistema.
    ├── README.md          # Documentação do projeto.
    └── academia.db        # Banco de dados SQLite (será criado automaticamente).
```

 **Explicação dos Arquivos**

 - `main.py`: Contém toda a lógica de cadastro, alteração, exclusão e listagem de clientes. As operações são feitas diretamente no banco de dados SQLite.
 
 - `classes.py`: Arquivo responsável por definir a classe Cliente, usada para organizar as informações dos clientes no sistema.

 - `academia.db`: Banco de dados SQLite onde os dados são armazenados. Será gerado automaticamente ao executar o sistema.