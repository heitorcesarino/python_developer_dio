from flask import Flask

app = Flask(__name__)

@app.route("/<number>", methods=['GET', 'POST'])
def hello(number):
    return 'hello world. {}'.format(number)

if __name__ == "__main__":
    app.run(debug=True)