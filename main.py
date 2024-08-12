from flask import Flask, make_response
from markupsafe import escape
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/cad/usuario")
def usuario():
    return render_template("usuario.html")


@app.route("/cad/cad_user", methods=["POST"])
def cad_user():
    return request.form

@app.route("/cad/anuncios")
def anuncio():
    pass

@app.route("/anuncios/pergunta")
def pergunta():
    pass

@app.route("/anuncios/compra")
def compra():
    pass

@app.route("anuncios/favoritos")
def favoritos():
    pass

@app.route("/config/categoria")
def categoria():
    return render_template("categoria;hyml")


@app.route("/relatorios/vendas")
def relatorio_vendas():
    return render_template("relatorio_vendas.html")

@app.route("/relatorios/compras")
def relatorio_compras():
    return render_template("relatorio_compras.html")