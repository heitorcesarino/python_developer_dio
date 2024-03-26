from flask import Flask, jsonify, request
import json

app = Flask(__name__)

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
@app.route("/dev/<int:id>/", methods=['GET', "PUT", "DELETE"])
def desenvolvedor(id):
    if request.method == "GET":
        try:
            response = desenvolvedores[id]
        except IndexError:
            error_message = "Desenvolvedor do id {} não existe".format(id)
            response = {"status": "erro", "mensagem": error_message}
        except Exception:
            error_message = 'erro desconhecido. Procure o adm da api'
            response = {"status": "erro", "mensagem": error_message}
        return jsonify(response)
    
    elif request.method == "PUT":
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify({"status":"sucesso", "mensagem": "registro alterado"})
    
    elif request.method == "DELETE":
        desenvolvedores.pop(id)
        return jsonify({"status":"sucesso", "mensagem": "registro excluido"})


#lista de todos os desenvolvedores e permite registrar um novo desenvolvedor
@app.route("/dev/", methods=["POST", "GET"])
def lista_desenvolvedores():
    if request.method == "POST":
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados["id"] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
    elif request.method == "GET":
        return jsonify(desenvolvedores)


if __name__ == "__main__":
    app.run()

