import tkinter as tk
from tkinter import ttk, messagebox
from product_manager import StudentManager

manager = StudentManager()

# ---------------- FUNCIONES ---------------- #

def cargar_datos():
    for item in tree.get_children():
        tree.delete(item)

    conn = manager.display_all_students()  # no sirve porque imprime
    # entonces usamos SQL directo o adaptamos (más abajo te explico mejor)

    # 🔥 solución rápida: consulta directa
    import mysql.connector
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Joh102Cas397*",
        database="student_db"
    )
    cursor = conexion.cursor()
    cursor.execute("SELECT id, name, age FROM students")

    for fila in cursor.fetchall():
        tree.insert("", "end", values=fila)

    conexion.close()


def agregar():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    notas = entry_notas.get()

    if not nombre or not edad or not notas:
        messagebox.showwarning("Error", "Completa todos los campos")
        return

    manager.add_student(nombre, int(edad), float(notas))
    cargar_datos()


def eliminar():
    seleccionado = tree.selection()

    if not seleccionado:
        messagebox.showwarning("Error", "Selecciona un estudiante")
        return

    item = tree.item(seleccionado)
    student_id = item["values"][0]

    manager.delete_student(student_id)
    cargar_datos()


def seleccionar_fila(event):
    seleccionado = tree.selection()
    if seleccionado:
        item = tree.item(seleccionado)
        valores = item["values"]

        entry_nombre.delete(0, tk.END)
        entry_nombre.insert(0, valores[1])

        entry_edad.delete(0, tk.END)
        entry_edad.insert(0, valores[2])


# ---------------- INTERFAZ ---------------- #

root = tk.Tk()
root.title("Sistema de Estudiantes")
root.geometry("700x500")

# FORMULARIO
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Nombre").grid(row=0, column=0)
entry_nombre = tk.Entry(frame)
entry_nombre.grid(row=0, column=1)

tk.Label(frame, text="Edad").grid(row=1, column=0)
entry_edad = tk.Entry(frame)
entry_edad.grid(row=1, column=1)

tk.Label(frame, text="Notas").grid(row=2, column=0)
entry_notas = tk.Entry(frame)
entry_notas.grid(row=2, column=1)

# BOTONES
tk.Button(frame, text="Agregar", command=agregar).grid(row=3, column=0, pady=5)
tk.Button(frame, text="Eliminar", command=eliminar).grid(row=3, column=1)

# TABLA
tree = ttk.Treeview(root, columns=("ID", "Nombre", "Edad"), show="headings")

tree.heading("ID", text="ID")
tree.heading("Nombre", text="Nombre")
tree.heading("Edad", text="Edad")

tree.pack(fill="both", expand=True)

tree.bind("<<TreeviewSelect>>", seleccionar_fila)

# CARGAR DATOS
cargar_datos()

root.mainloop()