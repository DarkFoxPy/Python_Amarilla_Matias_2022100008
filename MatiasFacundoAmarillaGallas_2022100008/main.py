from flask import Flask, request, jsonify
from cliente import verificar_cliente

app = Flask(__name__)

@app.route('/cliente', methods=['POST'])
def cliente():
    data = request.get_json()
    if not data or 'ci' not in data:
        return jsonify({
            "accion": "Faltan parametros",
            "codRes": "ERROR",
            "menRes": "Error debe cargar la CI del clientes",
            "ci": None
        }), 400

    ci = data['ci']
    resultado = verificar_cliente(ci)
    return jsonify(resultado)

if __name__ == '__main__':
    app.run(host='localhost', debug = True, port = 5003)