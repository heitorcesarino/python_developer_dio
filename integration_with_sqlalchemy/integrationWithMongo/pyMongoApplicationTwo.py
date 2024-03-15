import pymongo as pyM
import datetime
import pprint

# criando client
client = pyM.MongoClient('mongodb+srv://heitorcesarino:vkMqqY3uWAxP76Cs@cluster0.ktltw0y.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
#setando db
db = client.test
#criando posts
posts = db.posts
#selecionando todos os posts da minha coleção
print("\ndocumentos dentro da coleção posts")
for post in posts.find():
    pprint.pprint(post)

# contando quantidade de registros em documentos, e filtrando
print(posts.count_documents({"author":"morgoth"}))
print(posts.count_documents({"tags":"pymongo"}))

# trazendo uma instancia do documento, e filtrando
pprint.pprint(posts.find_one({"tags":"pymongo"}))

# recuperando todos os documentos de forma ordenada
print("\n recuperando documentos de forma ordenada")
for post in posts.find({}).sort("date"):
    pprint.pprint(post)

#criando index para o banco de dados de documentos 
result = db.profiles.create_index([('author', pyM.ASCENDING )], unique=True)
print(sorted(list(db.profiles.index_information())))

#Criando dados para nova collection
user_profile_user = [
    {'user_id': 211, 'name': 'luke'},
    {'user_id': 212, 'name': 'joao'}
]

#criando nova collection e inserindo dados
result = db.profile_user.insert_many(user_profile_user)

#trazendo todas as collections
print("\nTodas as coleções disponiveis no mongodb")
collections = db.list_collection_names()
for collection in collections:
        print(collection)

#print(posts.delete_one({"author":"morgoth"}))
        
client.drop_database("test")
print(db.list_collection_names())