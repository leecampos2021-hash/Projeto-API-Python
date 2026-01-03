from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Livro(db.Model):
    __tablename__ = "livros"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String, nullable=False)
    autor = db.Column(db.String, nullable=False)
    editora = db.Column(db.String, nullable=False)
    publicacao = db.Column(db.Integer)

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "autor": self.autor,
            "editora": self.editora,
            "publicacao": self.publicacao
        }

