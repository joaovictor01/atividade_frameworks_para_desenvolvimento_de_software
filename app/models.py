import datetime
from app.extensions import db


class Usuario(db.Model):
    __tablename__ = "usuario"
    id = db.Column("id", db.Integer, primary_key=True)
    nome = db.Column("nome", db.String(100), nullable=False)
    email = db.Column("email", db.String(100), nullable=False)
    senha = db.Column("senha", db.String(100), nullable=False)
    endereco = db.Column("endereco", db.String(100), nullable=False)

    def __init__(self, nome, email, senha, endereco):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.endereco = endereco


class Categoria(db.Model):
    __tablename__ = "categoria"
    id = db.Column("id", db.Integer, primary_key=True)
    nome = db.Column("nome", db.String(100), nullable=False)
    descricao = db.Column("descricao", db.String(100), nullable=False)

    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao


class Anuncio(db.Model):
    __tablename__ = "anuncio"
    id = db.Column("id", db.Integer, primary_key=True)
    titulo = db.Column("titulo", db.String(256))
    descricao = db.Column("descricao", db.String(256))
    quantidade = db.Column("quantidade", db.Integer)
    preco = db.Column("preco", db.Float)
    categoria_id = db.Column("categoria_id", db.Integer, db.ForeignKey("categoria.id"))
    usuario_id = db.Column("usuario_id", db.Integer, db.ForeignKey("usuario.id"))
    data_criacao = db.Column(
        "data_criacao", db.DateTime, default=datetime.utcnow(), nullable=False
    )

    def __init__(
        self,
        titulo,
        descricao,
        quantidade,
        preco,
        categoria_id,
        usuario_id,
        data_criacao=None,
    ):
        self.titulo = titulo
        self.descricao = descricao
        self.quantidade = quantidade
        self.preco = preco
        self.categoria_id = categoria_id
        self.usuario_id = usuario_id
        if data_criacao:
            self.data_criacao = data_criacao
