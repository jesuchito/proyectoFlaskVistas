-- Creación de la tabla "contenidos"
CREATE TABLE vistas (
    id_vista SERIAL PRIMARY KEY,             -- Código identificativo de cada vista, con autoincremento
    nombre_vista VARCHAR(255) NOT NULL,      -- Nombre de la vista
    contenidos_ids INTEGER[]                 -- Listado de identificadores de contenidos, almacenado como un array de enteros
);

-- Inserción de datos en la tabla "Vistas"

-- Vista: Recomendado para ti
INSERT INTO vistas (nombre_vista, contenidos_ids)
VALUES 
('Recomendado para ti', ARRAY[1, 2, 3, 4, 5, 6, 9, 11]);

-- Vista: Películas
INSERT INTO vistas (nombre_vista, contenidos_ids)
VALUES 
('Películas', ARRAY[2, 3, 6]);

-- Vista: Series
INSERT INTO vistas (nombre_vista, contenidos_ids)
VALUES 
('Series', ARRAY[1, 7, 9]);

-- Vista: Documentales
INSERT INTO vistas (nombre_vista, contenidos_ids)
VALUES 
('Documentales', ARRAY[4, 8, 11]);

-- Vista: Horror y Thriller
INSERT INTO vistas (nombre_vista, contenidos_ids)
VALUES 
('Horror y Thriller', ARRAY[6, 7, 9]);

-- Vista:  
INSERT INTO vistas (nombre_vista, contenidos_ids)
VALUES 
('Favoritos', ARRAY[ ]::INTEGER[]);