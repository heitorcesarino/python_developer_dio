from models import Pessoas
from models import Usuarios

#insere dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='heitor', idade=24)
    print(pessoa)
    pessoa.save()


#consulta dados da tabela pessoa
def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    #pessoa = Pessoas.query.filter_by(nome='heitor').first()
    #print(pessoa.idade)


#altera dados da tabela pessoa
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='heitor').first()
    pessoa.idade = 21
    pessoa.save()


#exclui dados da tabela pessoa
def exclue_pessoa():
    pessoa = Pessoas.query.filter_by(nome='heitor').first()
    pessoa.delete()


def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)

#permite que somente a main chame as funções
if __name__ == "__main__":
    insere_usuario('heitor', 'jahg')
    insere_usuario('ana', '1234')
    consulta_todos_usuarios()
    #insere_pessoas()
    #altera_pessoa()
    #exclue_pessoa()
    #consulta_pessoas()
    
    