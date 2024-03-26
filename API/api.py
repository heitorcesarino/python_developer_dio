from flask import Flask, jsonify, request
import json

app = Flask(__name__)


@app.route('/<int:id>')
def pessoas(id):
    soma = 1 + id
    return jsonify({'id': soma, 'nome': 'rafael', 'profissao': 'Desenvolvedor'})

# maneira nem tão legal de fazer
# @app.route('/soma/<int:Valor1>/<int:Valor2>')
# def soma(Valor1, Valor2):
#      return jsonify({'soma':  Valor1 + Valor2})

#maneira legal de se fazer
@app.route('/soma', methods=['POST', 'GET'])
def soma():
    if request.method == 'POST':
        dados = json.loads(request.data)
        total = sum(dados['valores'])
    elif request.method == 'GET':
        total = 10 + 10
    return jsonify({'soma': total})


if __name__ == "__main__":
    app.run(debug=True)