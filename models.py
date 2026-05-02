# models.py
# Definición del modelo de datos para el sistema

class Student:
    """
    Clase que representa un estudiante dentro del sistema.

    Esta clase funciona como un modelo de datos (objeto) que
    encapsula la información de un registro en la base de datos.

    Atributos:
        student_id (int): Identificador único del estudiante.
        name (str): Nombre del estudiante.
        age (int): Edad del estudiante.
        marks (float): Calificación o puntaje del estudiante.
    """

    def __init__(self, student_id, name, age, marks):
        """
        Constructor de la clase Student.

        Parámetros:
            student_id (int): ID único del estudiante.
            name (str): Nombre del estudiante.
            age (int): Edad del estudiante.
            marks (float): Calificación del estudiante.
        """
        self.student_id = student_id
        self.name = name
        self.age = age
        self.marks = marks

    def __str__(self):
        """
        Representación en texto del objeto Student.

        Retorna:
            str: Información formateada del estudiante.
        """
        return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Marks: {self.marks}"