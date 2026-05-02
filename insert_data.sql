-- =========================================
-- USAR BASE DE DATOS
-- =========================================

USE student_db;

-- =========================================
-- INSERTAR DATOS DE PRUEBA
-- =========================================

INSERT INTO students (name, age, marks) VALUES
('Juan Perez', 20, 4.5),
('Maria Gomez', 22, 4.8),
('Carlos Lopez', 19, 3.9),
('Ana Torres', 21, 4.2),
('Luis Ramirez', 23, 3.7),
('Sofia Martinez', 20, 4.9),
('Pedro Castillo', 24, 3.5),
('Laura Diaz', 22, 4.6),
('Diego Herrera', 21, 3.8),
('Valentina Rojas', 19, 4.7);

-- =========================================
-- CONSULTA DE VERIFICACIÓN
-- =========================================

SELECT * FROM students;
