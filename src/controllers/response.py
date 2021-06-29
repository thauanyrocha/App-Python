from flask import Response 
import json

class Resposta():
    def newResponse(status, conteudo, mensagem=False):
        body = {}
        body["dados"] = conteudo

        if(mensagem):
            body["mensagem"] = mensagem

        return Response(json.dumps(body), status = status, mimetype="application/json")