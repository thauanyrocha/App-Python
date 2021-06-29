from src.model.usuarios import Usuario
from src.app.server import db

class UsuarioController():

    def get():
        usuario = Usuario.query.all()
        dados = [ Usuario.to_json() for Usuario in usuario]
        return dados
    
    def get_id(id):
        usuario = Usuario.query.filter_by(id=id).first()
        dados = usuario.to_json()
        return dados

    def create(body):
        try:
            usuario = Usuario(
                nome=body["nome"], 
                email=body["email"]
            )
            db.session.add(usuario)
            db.session.commit()
            return {
                "status": 201,
                "conteudo": {},
                "mensagem": "Sucesso"
            }
        except Exception as e:
            return {
                "status": 400,
                "conteudo": {},
                "mensagem": "Erro"
            }  

    def update(id, body):
        usuario = Usuario.query.filter_by(id=id).first()
        try:
            usuario.nome = body["nome"]
            usuario.email = body["email"]
            db.session.commit()
            return {
                "status": 201,
                "conteudo": {},
                "mensagem": "Sucesso"
            }
        except Exception as e:
            return {
                "status": 400,
                "conteudo": {},
                "mensagem": "Erro"
            }
    
    def delete(id):
        usuario = Usuario.query.filter_by(id=id).first()
        try:
            db.session.delete(usuario)
            db.session.commit()
            return {
                "status": 201,
                "conteudo": {},
                "mensagem": "Sucesso"
            }
        except Exception as e:
            return {
                "status": 400,
                "conteudo": {},
                "mensagem": "Erro"
            }
