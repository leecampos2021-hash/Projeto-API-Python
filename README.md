API de Livros em Flask
Este projeto é uma API REST desenvolvida em Flask para gerenciar uma lista de livros.
 A API permite listar, buscar, criar e deletar livros, utilizando banco de dados SQLite com SQLAlchemy.

Tecnologias Utilizadas
Python 3


Flask


SQLAlchemy


SQLite



Como Executar o Projeto
Clone este repositório:

 git clone https://github.com/seu-usuario/seu-repo.git


Instale as dependências:

 pip install -r requirements.txt


Execute a aplicação:

 python app.py


A API será iniciada em:
http://127.0.0.1:5000

Na primeira execução, o banco SQLite será criado e carregado com uma lista inicial de livros.

Estrutura do Projeto
/seu-projeto
│ app.py
│ models.py
│ livros.py
│ livro.db
│ README.md

models.py: contém o modelo Livro e a configuração do SQLAlchemy


livros.py: lista inicial de livros para popular o banco


app.py: rotas e lógica da API



Endpoints da API
1. Listar todos os livros
GET /livros
Exemplo de resposta:
[
  {
    "id": 1,
    "nome": "Exemplo",
    "autor": "Autor",
    "editora": "Editora",
    "publicacao": "2020"
  }
]


2. Criar um livro
POST /livros
Body JSON:
{
  "nome": "Novo Livro",
  "autor": "Autor",
  "editora": "Editora",
  "publicacao": "2023"
}

Resposta 201:
{
  "id": 5,
  "nome": "Novo Livro",
  "autor": "Autor",
  "editora": "Editora",
  "publicacao": "2023"
}


3. Buscar livro por nome
GET /livro?nome=termo
Busca por nome usando correspondência parcial (ilike).
Possíveis respostas:
Lista de livros encontrados


400 se nenhum nome for informado


404 se nada for encontrado



4. Buscar livro por editora
GET /livro/editora?editora=nome
Funcionamento igual à busca por nome, mas filtrando por editora.

5. Deletar livro por ID
DELETE /livros/<id>
Resposta:
{
  "mensagem": "Livro 'Nome do Livro' deletado"
}

Se o ID não existir:
{
  "erro": "Livro não encontrado"
}


Melhorias Futuras
Criação de front-end simples para visualização dos dados

