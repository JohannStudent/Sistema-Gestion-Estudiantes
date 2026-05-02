# database.py
# Configuración y gestión de conexión a MySQL

import mysql.connector

# ==============================
# CONFIGURACIÓN DE LA BASE DE DATOS
# ==============================

# Credenciales de conexión (ajustar según el entorno local)
HOST = "localhost"
USER = "root"
PASSWORD = "Joh102Cas397*"
DATABASE = "student_db" # Nombre de la base de datos

# ==============================
# FUNCIÓN: CREAR CONEXIÓN
# ==============================

def create_connection():
    """
    Establece y retorna una conexión activa a la base de datos MySQL.

    Retorna:
        connection (MySQLConnection): Objeto de conexión a la base de datos.
    """
    return mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

# ==============================
# FUNCIÓN: CREAR TABLA
# ==============================

def create_table():
    """
    Crea la tabla 'students' si no existe en la base de datos.

    Estructura de la tabla:
        - id: Identificador único (clave primaria, autoincremental)
        - name: Nombre del estudiante
        - age: Edad del estudiante
        - marks: Calificación o puntaje del estudiante

    Nota:
        Esta función garantiza que la tabla esté disponible antes
        de realizar operaciones CRUD.
    """
    conn = create_connection()
    cursor = conn.cursor()

    # Consulta SQL para crear la tabla si no existe
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            age INT NOT NULL,
            marks FLOAT NOT NULL
        )
    """)

    # Guardar cambios en la base de datos
    conn.commit()

    # Cerrar conexión para liberar recursos
    conn.close()