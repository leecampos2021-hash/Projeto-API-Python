from flask import Flask, jsonify, request
from models import db, Livro
from livros import Livros 

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///livro.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


# Criar tabela + inserir a lista 
with app.app_context():
    db.create_all()

    if Livro.query.count() == 0:  # tabela vazia inserir a lista
        for item in Livros:
            novo = Livro(
                nome=item["nome"],
                autor=item["autor"],
                editora=item["editora"],
                publicacao=item["publicação"]
            )
            db.session.add(novo)
        db.session.commit()
        print("Livros iniciais inseridos!")
    else:
        print("Tabela já tem dados.")


# GET — listar todos os livros
@app.route('/livros', methods=['GET'])
def get_livros():
    livros = Livro.query.all()
    return jsonify([l.to_dict() for l in livros])


# POST — criar livro
@app.route('/livros', methods=['POST'])
def create_livro():
    dados = request.json or {}

    novo = Livro(
        nome=dados.get("nome"),
        autor=dados.get("autor"),
        editora=dados.get("editora"),
        publicacao=dados.get("publicacao")
    )

    db.session.add(novo)
    db.session.commit()

    return jsonify(novo.to_dict()), 201


# GET — buscar por nome com ?nome=
@app.get("/livro")
def buscar_livro():
    nome = request.args.get("nome")
    if not nome:
        return jsonify({"erro": "Informe ?nome=algum_nome"}), 400

    livros = Livro.query.filter(Livro.nome.ilike(f"%{nome}%")).all()

    if not livros:
        return jsonify({"mensagem": "Nenhum livro encontrado"}), 404

    return jsonify([l.to_dict() for l in livros]), 200


#Buscar por Editora
@app.get("/livro/editora")
def buscar_por_editora():
    editora = request.args.get("editora")
    if not editora:
        return jsonify({"erro": "Informe a editora usando ?editora=nome"}), 400

    livros = Livro.query.filter(Livro.editora.ilike(f"%{editora}%")).all()

    if not livros:
        return jsonify({"mensagem": "Nenhum livro encontrado para essa editora"}), 404

    return jsonify([l.to_dict() for l in livros]), 200


# DELETE — deletar por id
@app.route('/livros/<int:id>', methods=['DELETE'])
def deletar_livro(id):
    livro = Livro.query.get(id)

    if not livro:
        return jsonify({"erro": "Livro não encontrado"}), 404

    db.session.delete(livro)
    db.session.commit()

    return jsonify({"mensagem": f"Livro '{livro.nome}' deletado"}), 200


if __name__ == "__main__":
    app.run(debug=True)
