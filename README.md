# 📦 Sistema de Gestión de Inventario (Python + MySQL)

## 🚀 Descripción del Proyecto

Este proyecto consiste en el desarrollo de un **Sistema de Gestión de Inventario** implementado en **Python** con integración a **MySQL**, el cual permite realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) sobre los registros de productos.

El sistema simula un entorno real de desarrollo backend, aplicando buenas prácticas de programación, arquitectura modular y conexión segura a bases de datos relacionales.

---

## 👨‍🎓 Información del Estudiante

- **Nombre:** Johann Casallas  
- **Institución:** Corporación Unificada de Educación Superior CUN  
- **Carrera:** Ingeniería de Sistemas  
- **Asignatura:** Administración de Bases de Datos  
- **Código / Grupo:** 51167 / Segundo Bloque / 26P01  
- **Fecha:** mayo de 2026  

---

## 🎯 Funcionalidades Principales

- ✅ Registrar nuevos productos  
- ✅ Consultar todos los productos (ordenados)  
- ✅ Buscar productos por ID  
- ✅ Actualizar información de productos  
- ✅ Eliminar productos  
- ✅ Conexión a base de datos MySQL  
- ✅ Código modular y estructurado  
- ✅ Uso de consultas parametrizadas (seguridad contra SQL Injection)  

---

## 🛠 Tecnologías Utilizadas

| Tecnología | Uso |
|------------|------|
| **Python 3** | Lógica del sistema |
| **MySQL** | Gestión de base de datos |
| **mysql-connector-python** | Conexión entre Python y MySQL |

---

## 📂 Estructura del Proyecto

- `database.py` → Configuración de conexión y creación de tablas  
- `models.py` → Definición del modelo de datos  
- `student_manager.py` → Operaciones CRUD  
- `main.py` → Interfaz de usuario por consola  
- `requirements.txt` → Dependencias del proyecto  
- `README.md` → Documentación  

---

## ⚙️ Instrucciones de Instalación

### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/suma-sree/student-management-system-python-mysql.git
cd student-management-system-python-mysql
```

### 2️⃣ Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3️⃣ Configurar la base de datos MySQL

Asegúrese de tener MySQL instalado y en ejecución.

Ingresar a MySQL:
```bash
mysql -u root -p
```

Crear la base de datos:
```sql
CREATE DATABASE student_db;
```

### 4️⃣ Configurar credenciales

Editar el archivo `database.py` con sus datos:

```python
HOST = "localhost"
USER = "root"
PASSWORD = "tu_contraseña"
DATABASE = "student_db"
```

### 5️⃣ Ejecutar el sistema
```bash
python gui.py
```

---

## 🧠 Conceptos Aplicados

- ✅ Arquitectura modular (separación por capas)  
- ✅ Diseño de bases de datos relacionales  
- ✅ Programación orientada a objetos (POO)  
- ✅ Consultas SQL seguras (parametrizadas)  
- ✅ Manejo de errores y validación de datos  
- ✅ Desarrollo de sistemas backend escalables  

---

## 📌 Observaciones

Este proyecto fue desarrollado como parte de la asignatura **Administración de Bases de Datos**, con el objetivo de aplicar conocimientos en diseño, implementación y gestión de sistemas de información basados en bases de datos relacionales.

---

## 🎬 Video demostrativo
[Enlace a YouTube o Drive]
