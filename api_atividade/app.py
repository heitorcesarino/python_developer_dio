from flask import Flask, request
from flask_restful import Resource, Api
from models import Pessoas, Atividades, Usuarios
from flask_httpauth import HTTPBasicAuth

#autenticação, inicializando api
auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)

# USUARIOS = {
#     'heitor': '554',
#      'ana':'665'
# }

# @auth.verify_password
# def verificacao(login, senha):
#     if not (login, senha):
#         return False
#     return USUARIOS.get(login) == senha

# executa a verificação para ter acesso aos dados.
@auth.verify_password
def verificacao(login, senha):
    if not (login, senha):
        return False
    return Usuarios.query.filter_by(login=login, senha=senha).first()


# classe pessoa que ira trazer dados do banco de dados relacionados a pessoa
class Pessoa(Resource):
    @auth.login_required
    def get(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        try:
            response ={
                'nome': pessoa.nome,
                'idade': pessoa.idade,
                'id': pessoa.id
        }
        except AttributeError:
            response  = {
                'status': 'error',
                'mensagem': 'pessoa nao encontrada'
            }
        return response

    def put(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        dados = request.json
        if 'nome' in dados:
            pessoa.nome = dados['nome']
        if 'idade' in dados:
            pessoa.idade = dados['idade']
        pessoa.save()
        response = {
            'id':pessoa.id,
            'nome': pessoa.nome,
            'idade': pessoa.idade
        }
        return response
    
    def delete(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        mensagem = "pessoa {} excluida com sucesso".format(pessoa.nome)
        pessoa.delete()
        return {'status':"sucesso", "mensagem": mensagem}
    

# classe atividade que ira trazer dados da tabela de pessoas
class ListaPessoas(Resource):
    @auth.login_required
    def get(self):
        pessoas = Pessoas.query.all()
        response = [{"id":i.id, 'nome':i.nome, 'idade':i.idade} for i in pessoas]
        return response
    
    def post(self):
        dados = request.json
        pessoa = Pessoas(nome=dados['nome'], idade=dados['idade'])
        pessoa.save()
        response = {
            'id': pessoa.id,
            'nome': pessoa.nome,
            'idade':pessoa.idade
        }
        return response


# classe listaatividades que ira trazer os dados da tabela de atividades
class ListaAtividades(Resource):
    def get(self):
        atividades = Atividades.query.all()
        response = [{'id':i.id, 'nome':i.nome, 'pessoa':i.pessoa.nome} for i in atividades]
        return response
    
    
    def post(self):
        dados = request.json
        pessoa = Pessoas.query.filter_by(nome=dados['pessoa']).first()
        atividade = Atividades(nome=dados['nome'], pessoa=pessoa)
        atividade.save()
        response ={
                'pessoa': atividade.pessoa.nome,
                'nome': atividade.nome,
                'id': atividade.id
        }
        return response

#adicionando rotas/resources
api.add_resource(Pessoa, "/pessoa/<string:nome>/")
api.add_resource(ListaPessoas, "/pessoa/")
api.add_resource(ListaAtividades, "/atividades/")

# 
if __name__ =="__main__":
    app.run(debug=True)