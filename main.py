# main.py
# Interfaz de usuario por consola para la gestión del sistema

from product_manager import StudentManager
from database import create_table

def main():
    """
    Función principal que ejecuta el sistema de gestión.

    - Inicializa la base de datos
    - Muestra un menú interactivo en consola
    - Permite ejecutar operaciones CRUD sobre estudiantes
    """
    
    # Asegurar que la tabla exista antes de operar
    create_table()

    # Instancia del gestor de estudiantes
    manager = StudentManager()

    while True:
        # ==============================
        # MENÚ PRINCIPAL
        # ==============================
        print("\n========== Student Management System ==========")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student by ID")
        print("4. Update Student Details")
        print("5. Delete Student")
        print("6. Exit")

        # Captura de opción del usuario
        choice = input("Enter your choice (1-6): ").strip()

        try:
            # ==============================
            # OPCIÓN 1: AGREGAR ESTUDIANTE
            # ==============================
            if choice == "1":
                name = input("Enter student name: ").strip()
                age = int(input("Enter student age: "))
                marks = float(input("Enter student marks: "))

                manager.add_student(name, age, marks)

            # ==============================
            # OPCIÓN 2: MOSTRAR TODOS
            # ==============================
            elif choice == "2":
                manager.display_all_students()

            # ==============================
            # OPCIÓN 3: BUSCAR POR ID
            # ==============================
            elif choice == "3":
                student_id = int(input("Enter student ID to search: "))
                manager.search_student(student_id)

            # ==============================
            # OPCIÓN 4: ACTUALIZAR
            # ==============================
            elif choice == "4":
                student_id = int(input("Enter student ID to update: "))
                name = input("Enter new name: ").strip()
                age = int(input("Enter new age: "))
                marks = float(input("Enter new marks: "))

                manager.update_student(student_id, name, age, marks)

            # ==============================
            # OPCIÓN 5: ELIMINAR
            # ==============================
            elif choice == "5":
                student_id = int(input("Enter student ID to delete: "))
                manager.delete_student(student_id)

            # ==============================
            # OPCIÓN 6: SALIR
            # ==============================
            elif choice == "6":
                print("\nThank you for using Student Management System. Goodbye!")
                break

            # ==============================
            # OPCIÓN INVÁLIDA
            # ==============================
            else:
                print("Invalid choice. Please select a valid option.")

        # ==============================
        # MANEJO DE ERRORES
        # ==============================
        except ValueError:
            print("Invalid input! Please enter correct numbers.")

# Punto de entrada del programa
if __name__ == "__main__":
    main()