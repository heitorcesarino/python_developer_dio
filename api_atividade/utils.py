from models import Pessoas

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


#permite que somente a main chame as funções
if __name__ == "__main__":
    #insere_pessoas()
    #altera_pessoa()
    exclue_pessoa()
    consulta_pessoas()
    
    