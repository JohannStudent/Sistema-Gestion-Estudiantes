-- =========================================
-- CREACIÓN DE BASE DE DATOS
-- =========================================

CREATE DATABASE IF NOT EXISTS student_db;

-- Usar la base de datos
USE student_db;

-- =========================================
-- CREACIÓN DE TABLA
-- =========================================

CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    marks FLOAT NOT NULL
);

-- =========================================
-- VERIFICACIÓN
-- =========================================

SHOW TABLES;
