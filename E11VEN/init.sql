-- Eliminar la tabla si existe
DROP TABLE IF EXISTS mytable;

-- Crear la tabla
CREATE TABLE mytable (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    edad INTEGER,
    email VARCHAR(100)
);

-- Insertar datos de ejemplo
INSERT INTO mytable (nombre, edad, email) VALUES 
    ('Jhoan Gruezo', 20, 'jg@gmail.com');