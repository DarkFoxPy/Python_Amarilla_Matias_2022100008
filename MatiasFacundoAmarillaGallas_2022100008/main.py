from flask import Flask, request, jsonify
import cliente

app = Flask(__name__)

@app.route('/cliente', methods=['POST'])
def cliente_lookup():
    try:
        data = request.get_json()
        ci = data.get('ci')
        
        if not ci:
            return jsonify({
                "accion": "Error",
                "codRes": "ERROR",
                "menRes": "Cédula no proporcionada",
                "ci": ""
            }), 400

      
        result = cliente.check_client(ci)
        
        if result:
            return jsonify({
                "accion": "Success",
                "codRes": "SIN_ERROR",
                "menRes": "OK",
                "ci": ci
            }), 200
        else:
            return jsonify({
                "accion": "Cliente no está en el sistema",
                "codRes": "ERROR",
                "menRes": "Error cliente",
                "ci": ci
            }), 404

    except Exception as e:
        return jsonify({
            "accion": "Error",
            "codRes": "ERROR",
            "menRes": str(e),
            "ci": ci if 'ci' in locals() else ""
        }), 500

if __name__ == '__main__':
    app.run(host='localhost', port=5003, debug=True)