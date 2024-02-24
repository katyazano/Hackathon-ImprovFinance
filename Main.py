from flask import Flask, Response, request, redirect, url_for, render_template
import bcrypt
import mysql.connector
import cgi
import MySQLdb
import os

app = Flask(__name__)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    print('hola mundo')
    if request.method == 'POST':
        data = request
        print(data)
        #usuario = request.form['usuario']
        #correo = request.form['correo']
        #contraseña = request.form['contraseña']
        #guardar_registro(usuario, correo, contraseña)
        return Response('ok', status=200)    
    return Response('ok', status=200)    


        
#def main():
 #   while True:
  #      conexion = get_connection()




#@app.route('/', methods=['GET', 'POST'])
#def login():
 #   print("Content-type: text/html\n")
  #  if request.method == 'POST':
   #     if 'login' in request.form:
    #        return render_template('login.html')
    #return render_template('register.html')

#@app.route('/static/<style.css>')
#def static_file(path):
  #  cache_timeout = 3600  # Cache timeout in seconds (1 hour)
   # root_dir = os.path.abspath(os.path.dirname(__file__))
    #return send_from_directory(os.path.join(root_dir, 'static'), path, cache_timeout=cache_timeout)

