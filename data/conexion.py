import mysql.connector

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

# Esto permitirá ejecutar el archivo como script de manera independiente para probar la conexión
if __name__ == "__main__":
    conexion = get_connection()
    print("Conexión de prueba exitosa.")


