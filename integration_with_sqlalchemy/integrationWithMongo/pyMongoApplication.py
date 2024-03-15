import pymongo as pyM
import datetime
import pprint

# criando client
client = pyM.MongoClient('mongodb+srv://heitorcesarino:vkMqqY3uWAxP76Cs@cluster0.ktltw0y.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')

#criando db e collection
db = client.test
collection = db.test_collection
#printando collection
print(db.test_collection)

# definição de informações para compor o documento
post = {
    "author": "sauron",
    "text": "my first mongodb application based on python",
    "tags": ["mongodb", "python3", "pymongo"],
    "date": datetime.datetime.now()
}

#preparando para submeter as informações
posts = db.posts
post_id = posts.insert_one(post).inserted_id
print(post_id)

#utilizando pprint para trazer a estrutura melhor formatada
pprint.pprint(db.posts.find_one())

#criando dois documentos em um mesmo post
#bulk inserts
new_posts = [
    {
        "author": "morgoth",
        "text": "my first mongodb application based on python das trevas",
        "tags": ["post", "bulk", "pymongo"],
        "date": datetime.datetime.now()
    },
    {
        "author": "ungolianth",
        "text": "my first mongodb application based on python da fome",
        "title": "Uma historia de morrer de fome, literalmente",
        "tags": ["post", "bulk", "pymongo"],
        "date": datetime.datetime.now()
    }
]

result = posts.insert_many(new_posts).inserted_ids
pprint.pprint(db.posts.find_one({"author": "ungolianth"}))

print("\ndocumentos dentro da coleção posts")
for post in posts.find():
    pprint.pprint(post)