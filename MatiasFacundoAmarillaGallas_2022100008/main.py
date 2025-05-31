
from flask import Flask
from login import login

app = Flask(__name__)

##servicios rest
app.register_blueprint(login)

@app.route('/', methods=['GET'])
def hello():
    return 'Hola Mundo'

if __name__ == "__main__":
    app.run(host='localhost', debug=True, port=5003)
    app.run(debug=True)