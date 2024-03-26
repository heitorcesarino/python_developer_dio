from flask import Flask, request
from flask_restful import Resource, Api
import json

#definindo app e api
app = Flask(__name__)
api = Api(app)

#lista de desenvolvedores
desenvolvedores = [
    {
        "id": "0",
        "nome": "heitor",
        "habilidades":['Python', 'flask'] 
    },
    {
        "id": "1",
        "nome": "athos",
        "habilidades":['delphi', 'django'] 
    }
]

# devolve um desenvolvedor pelo id, tambem altera e deleta um desenvolvedor
class Desenvolvedor(Resource):

    #get desenvolvedor
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            error_message = "Desenvolvedor do id {} não existe".format(id)
            response = {"status": "erro", "mensagem": error_message}
        except Exception:
            error_message = 'erro desconhecido. Procure o adm da api'
            response = {"status": "erro", "mensagem": error_message}
        return response
    
    #altera desenvolvedor
    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    #deleta desenvolvedor
    def delete(self, id):
        desenvolvedores.pop(id)
        return {"status":"sucesso", "mensagem": "registro excluido"}


#lista de todos os desenvolvedores e permite registrar um novo desenvolvedor
class ListaDesenvolvedores(Resource):
    
    #pega todos os desenvolvedores
    def get(self): 
        return desenvolvedores

    #adiciona um novo desenvolvedor
    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados["id"] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]


#rotas da api
api.add_resource(Desenvolvedor, "/dev/<int:id>/")
api.add_resource(ListaDesenvolvedores, "/dev/")


#permitir que somente o main rode esse codigo
if __name__ == "__main__":
    app.run(debug=True)