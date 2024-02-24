import mysql.connector
import process

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
        
def main():
    while True:
        conexion = get_connection()
        guardar_registro("jesus", "sajdjaf@gmail.com", "skafsalfa")
        
# Esto permitirá ejecutar el archivo como script de manera independiente para probar la conexión
if __name__ == "__main__":
    main()
    print("Nunca Imprimir")


