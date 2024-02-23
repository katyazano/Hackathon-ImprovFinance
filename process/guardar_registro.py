# guardar_registro.py
import mysql.connector
from data.conexion import get_connection  

def guardar_registro(usuario, correo, contraseña):
    try:
        # Obtener conexión a la base de datos
        conexion = get_connection()

        if conexion.is_connected():
            cursor = conexion.cursor()

            # Insertar datos en la base de datos
            sql = "INSERT INTO usuarios (usuario, correo, contraseña) VALUES (%s, %s, %s)"
            valores = (usuario, correo, contraseña)
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

if __name__ == "__main__":
    # Obtener datos del formulario
    import cgi
    form = cgi.FieldStorage()

    usuario = form.getvalue("usuario")
    correo = form.getvalue("correo")
    contraseña = form.getvalue("contraseña")

    # Procesar y guardar el registro
    guardar_registro(usuario, correo, contraseña)
