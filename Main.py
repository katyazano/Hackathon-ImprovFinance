from flask import Flask, request, redirect, url_for, render_template
import bcrypt
import mysql.connector
import cgi
import MySQLdb
import os

app = Flask(__name__)

# Configuración de la conexión a la base de datos
config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'users',
    'raise_on_warnings': True
}

conexion = None

def get_connection():
    global conexion
    if conexion is None or not conexion.is_connected():
        try:
            # Establecer la conexión si no existe o está cerrada
            conexion = mysql.connector.connect(**config)
        except mysql.connector.Error as e:
            print(f'Error al conectar a la base de datos: {e}')
            raise
    return conexion

def guardar_registro(usuario, correo, contraseña):
    try:
        # Obtener conexión a la base de datos
        conexion = get_connection()

        if conexion.is_connected():
            cursor = conexion.cursor()

            hashed_password = bcrypt.hashpw(contraseña.encode('utf-8'), bcrypt.gensalt())

            # Insertar datos en la base de datos
            sql = "INSERT INTO usuarios (usuario, correo, contraseña) VALUES (%s, %s, %s)"
            valores = (usuario, correo, hashed_password)
            cursor.execute(sql, valores)

            # Confirmar la operación y cerrar cursor
            conexion.commit()
            cursor.close()
            print("Registro guardado exitosamente.")
    except mysql.connector.Error as e:
        print(f'Error al guardar el registro en la base de datos: {e}')
    finally:
        # Cerrar la conexión
        if 'conexion' in locals() and conexion.is_connected():
            conexion.close()
        
def main():
    while True:
        conexion = get_connection()

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        usuario = request.form['usuario']
        correo = request.form['correo']
        contraseña = request.form['contraseña']
        guardar_registro(usuario, correo, contraseña)
    return render_template('register.html')


def guardar_login():
    try:
        # Connect to MySQL database
        db = MySQLdb.connect(host="localhost", user="root", passwd="", db="users")
        cursor = db.cursor()

        # Check if the request method is POST
        if os.environ['REQUEST_METHOD'] == 'POST':
            # Get form data
            form = cgi.FieldStorage()
            usuario = form.getvalue('usuario')
            contraseña = form.getvalue('contraseña')

            # Retrieve hashed password from database based on username
            cursor.execute("SELECT contraseña FROM usuarios WHERE usuario = %s", (usuario,))
            row = cursor.fetchone()

            if row:
                hashed_password = row[0]

                # Check if the entered password matches the hashed password
                if bcrypt.checkpw(contraseña.encode('utf-8'), hashed_password.encode('utf-8')):
                    # Password is correct
                    print("<h1>Inicio de sesión exitoso</h1>")
                    print("<p>Bienvenido, {}!</p>".format(usuario))
                else:
                    # Password is incorrect
                    print("<h1>Error:</h1>")
                    print("<p>Contraseña incorrecta.</p>")
            else:
                # User not found
                print("<h1>Error:</h1>")
                print("<p>Usuario no encontrado.</p>")
        else:
            # Handle other HTTP methods (e.g., GET)
            print("<h1>Error:</h1>")
            print("<p>Método HTTP no permitido.</p>")

    except Exception as e:
        print("<h1>Error:</h1>")
        print("<p>", e, "</p>")

    finally:
        # Close database connection
        if 'db' in locals() and db is not None:
            db.close()

def login():
    print("Content-type: text/html\n")
    if request.method == 'POST':
        usuario = request.form['usuario']
        contraseña = request.form['contraseña']
        guardar_login(usuario, contraseña)
        return render_template('login.html')

# Esto permitirá ejecutar el archivo como script de manera independiente para probar la conexión
if __name__ == "__main__":
    app.run(debug=True)