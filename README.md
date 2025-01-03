# Nome do Projeto

Uma API para gerenciamento de tarefas.

## Índice

- [Sobre](#sobre)
- [Funcionalidades](#funcionalidades)
- [Tecnologias Usadas](#tecnologias-usadas)
- [Instalação](#instalacao)
- [Uso](#uso)

## Sobre

Uma API para funcionalidade de gerenciamento de tarefas, TODO List. Utilizando **FastAPI** para o desenvolvimento, organizando o projeto em escopos de funcionalidade `routes`, `services`, `models`, etc, facilitando a manutenção do código.

## Funcionalidades

Liste as principais funcionalidades do projeto. Exemplos:
- Criação, listagem, atualização e exclusão de tarefa.
- Geração e autenticação através de tokens

## Tecnologias Usadas

- [Python](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [PostgreSQL 16.4](https://www.postgresql.org/)
- [Pydantic](https://docs.pydantic.dev/latest/)
- [JWT](https://pyjwt.readthedocs.io/en/stable/)

## Instalação e Configuração

Instruções para instalar o projeto e suas dependências. Exemplo:

1. Clone o repositório:
    ```bash
    git clone https://github.com/lucasgpalves/api-to-do-list.git
    ```

2. Navegue até o diretório do projeto:
    ```bash
    cd api-to-do-list
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Acesse o seu sistema gerenciador de banco de dados e crie um SCHEMA ou DATABASE:
    ```sql
    CREATE DATABASE nome_database;
    ```

5. Configure seu `.env` conforme o [`.env.example`](.env.example):
    ```bash
    DB_NAME="database_name_here"
    DB_USER="user_here"
    DB_PASSWORD="password_here"
    DB_ADDRESS="127.0.0.1"
    DB_PORT="5432"

    SECRET_KEY="your_secret_key"
    ```

6. Realize as migrations do projeto:
    ```bash
    alembic upgrade head
    ```

## Uso

Instruções para usar o projeto. Exemplos:

1. Inicie o aplicativo:
    ```bash
    fastapi dev main.py
    ```

2. Acesse a aplicação em `http://localhost:8000`.
3. Acesse a documentação Swagger em `http://localhost:8000/docs`.

## Endpoints && Request

### Task
- GET `http://localhost:8000/tasks`
- GET `http://localhost:8000/tasks/{id}`
- GET `http://localhost:8000/tasks/state/{state}`
- GET `http://localhost:8000/tasks/page/?skip=0&limit=10`
- POST `http://localhost:8000/tasks/{id}`
```bash
curl --request POST \
  --url http://localhost:8000/tasks \
  --header 'Authorization: Bearer <token_here>' \
  --header 'Content-Type: application/json' \
  --header 'User-Agent: insomnia/10.3.0' \
  --data '{
	"title": "Teste",
	"description": "Teste",
	"state": "PENDENTE"
}'
```
- PUT `http://localhost:8000/tasks/{id}`
```bash
curl --request PUT \
  --url http://localhost:8000/tasks/<id> \
  --header 'Authorization: Bearer <token_here>' \
  --header 'Content-Type: application/json' \
  --header 'User-Agent: insomnia/10.3.0' \
  --data '{
	"title": "Teste",
	"description": "Teste",
	"state": "EM_ANDAMENTO"
}'
```
- DELETE `http://localhost:8000/tasks/{id}`

### Token
- GET `http://localhost:8000/token`
