from flask import redirect, url_for
from flask import render_template
from flask import request
from . import create_app
from models import Usuario, Categoria, Anuncio
from extensions import db

app = create_app()


@app.errorhandler(404)
def paginanaoencontrada(error):
    return render_template("pagnaoencontrada.html")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/cad/usuario")
def usuario():
    return render_template(
        "usuario.html", usuarios=Usuario.query.all(), titulo="Usuario"
    )


@app.route("/usuario/criar", methods=["POST"])
def criarusuario():
    usuario = Usuario(
        request.form.get("username"),
        request.form.get("email"),
        request.form.get("password"),
        request.form.get("address"),
    )
    db.session.add(usuario)
    db.session.commit()
    return redirect(url_for("usuario"))


@app.route("/usuario/detalhar/<int:id>")
def buscarusuario(id):
    usuario = Usuario.query.get(id)
    return usuario.nome


@app.route("/usuario/editar/<int:id>", methods=["GET", "POST"])
def editarusuario(id):
    usuario = Usuario.query.get(id)
    if request.method == "POST":
        usuario.nome = request.form.get("username")
        usuario.email = request.form.get("email")
        usuario.senha = request.form.get("password")
        usuario.end = request.form.get("address")
        db.session.add(usuario)
        db.session.commit()
        return redirect(url_for("usuario"))

    return render_template("editar_usuario.html", usuario=usuario, titulo="Usuario")


@app.route("/usuario/deletar/<int:id>")
def deletarusuario(id):
    usuario = Usuario.query.get(id)
    db.session.delete(usuario)
    db.session.commit()
    return redirect(url_for("usuario"))


@app.route("/cad/anuncio")
def anuncio():
    return render_template(
        "anuncio.html",
        anuncios=Anuncio.query.all(),
        categorias=Categoria.query.all(),
        titulo="Anuncio",
    )


@app.route("/anuncio/criar", methods=["POST"])
def criaranuncio():
    anuncio = Anuncio(
        request.form.get("titulo"),
        request.form.get("descricao"),
        request.form.get("quantidade"),
        request.form.get("preco"),
        request.form.get("categoria"),
        request.form.get("usuario"),
    )
    db.session.add(anuncio)
    db.session.commit()
    return redirect(url_for("anuncio"))


@app.route("/anuncios/pergunta")
def pergunta():
    return render_template("pergunta.html")


@app.route("/anuncios/compra")
def compra():
    print("anuncio comprado")
    return ""


@app.route("/anuncio/favoritos")
def favoritos():
    print("favorito inserido")
    return "<h4>Comprado</h4>"


@app.route("/config/categoria")
def categoria():
    return render_template(
        "categoria.html", categorias=Categoria.query.all(), titulo="Categoria"
    )


@app.route("/categoria/criar", methods=["POST"])
def criar_categoria():
    categoria = Categoria(request.form.get("nome"), request.form.get("desc"))
    db.session.add(categoria)
    db.session.commit()
    return redirect(url_for("categoria"))


@app.route("/relatorios/vendas")
def relatorio_vendas():
    return render_template("relatorio_vendas.html")


@app.route("/relatorios/compras")
def relatorio_compras():
    return render_template("relatorio_compras.html")
