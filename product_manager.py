# student_manager.py
# Gestión de operaciones CRUD sobre la base de datos MySQL

from database import create_connection
from models import Student

class StudentManager:
    """
    Clase encargada de gestionar las operaciones CRUD (Crear, Leer,
    Actualizar y Eliminar) para los registros de estudiantes en la base de datos.
    """

    def add_student(self, name, age, marks):
        """
        Inserta un nuevo estudiante en la base de datos.

        Parámetros:
            name (str): Nombre del estudiante.
            age (int): Edad del estudiante.
            marks (float): Calificación del estudiante.
        """
        conn = create_connection()
        cursor = conn.cursor()

        sql = "INSERT INTO students (name, age, marks) VALUES (%s, %s, %s)"
        cursor.execute(sql, (name, age, marks))

        conn.commit()
        print(f"\nStudent '{name}' added successfully!")

        conn.close()

    def display_all_students(self):
        """
        Recupera y muestra todos los estudiantes almacenados en la base de datos,
        ordenados alfabéticamente por nombre.
        """
        conn = create_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM students ORDER BY name ASC")
        rows = cursor.fetchall()

        conn.close()

        # Validar si existen registros
        if not rows:
            print("\nNo student records found.")
            return

        print("\nList of Students (sorted by name):")

        # Convertir cada fila en objeto Student y mostrarlo
        for row in rows:
            student = Student(*row)
            print(student)

    def search_student(self, student_id):
        """
        Busca un estudiante por su ID.

        Parámetros:
            student_id (int): Identificador del estudiante.
        """
        conn = create_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM students WHERE id = %s", (student_id,))
        row = cursor.fetchone()

        conn.close()

        if row:
            student = Student(*row)
            print("\nStudent found:")
            print(student)
        else:
            print("\nStudent not found.")

    def update_student(self, student_id, name, age, marks):
        """
        Actualiza la información de un estudiante existente.

        Parámetros:
            student_id (int): ID del estudiante a actualizar.
            name (str): Nuevo nombre.
            age (int): Nueva edad.
            marks (float): Nueva calificación.
        """
        conn = create_connection()
        cursor = conn.cursor()

        # Verificar si el estudiante existe antes de actualizar
        cursor.execute("SELECT * FROM students WHERE id = %s", (student_id,))
        row = cursor.fetchone()

        if not row:
            print("\nStudent not found.")
            conn.close()
            return

        sql = "UPDATE students SET name = %s, age = %s, marks = %s WHERE id = %s"
        cursor.execute(sql, (name, age, marks, student_id))

        conn.commit()
        print(f"\nStudent with ID {student_id} updated successfully!")

        conn.close()

    def delete_student(self, student_id):
        """
        Elimina un estudiante de la base de datos.

        Parámetros:
            student_id (int): ID del estudiante a eliminar.
        """
        conn = create_connection()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
        conn.commit()

        # Verificar si se eliminó algún registro
        if cursor.rowcount > 0:
            print(f"\nStudent with ID {student_id} deleted successfully.")
        else:
            print("\nStudent not found.")

        conn.close()