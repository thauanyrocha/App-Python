from src.app.server import app
from src.controllers.usuariosController import UsuarioController
from src.controllers.response import Resposta
from flask import request

#BEM VINDO


@app.route("/", methods=["GET"])
def index():
    return "Seja bem vindo(a)!!! "

# METODO GET USUARIO
@app.route("/usuario", methods=["GET"])
def get_usuario():
    dados = UsuarioController.get()
    return Resposta.newResponse(200, dados, "Sucesso")
# METODO GET USUARIO BY ID
@app.route("/usuario/<id>", methods=["GET"])
def get_usuario_id(id):
    dados = UsuarioController.get_id(id)
    return Resposta.newResponse(200, dados, "Sucesso")
# METODO POST USUARIO
@app.route("/usuario", methods=["POST"])
def create_usuario():
    body = request.get_json()
    dados = UsuarioController.create(body)
    return Resposta.newResponse(dados["status"], dados["conteudo"], dados["mensagem"])
# METODO PUT USUARIO
@app.route("/usuario/<id>", methods=["PUT"])
def update_usuario(id):
    body = request.get_json()
    dados = UsuarioController.update(id, body)
    return Resposta.newResponse(dados["status"], dados["conteudo"], dados["mensagem"])
# METODO DELETE USUARIO
@app.route("/usuario/<id>", methods=["DELETE"])
def delete_usuario(id):
    dados = UsuarioController.delete(id)
    return Resposta.newResponse(dados["status"], dados["conteudo"], dados["mensagem"])

#app.run()
