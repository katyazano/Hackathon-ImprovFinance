from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/post_example', methods=['POST'])
def post_example():
    if request.method == 'POST':
        data = request.json
        #usuario = data["usuario"]
        #correo = data["correo"]
        #contrasena = data["contraseña"]
        print(data)
        #print (usuario)
        #print (correo)
        #print(contrasena)
        return 'Hello, World!'
    else:
        return 'Método no permitido', 405

@app.route('/get_example', methods=['GET'])
def get_example():
    return 'Hello, World! (GET method)'

if __name__ == '__main__':
    app.run(debug=True)