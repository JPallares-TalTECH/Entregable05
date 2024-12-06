CREATE TABLE Estudiantes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50),
    edad INT,
    ciudad VARCHAR(50)
);

-- Insertar datos básicos en la tabla
INSERT INTO Estudiantes (nombre, edad, ciudad) VALUES ('Veronica Berrio', 20, 'Barranquilla');
INSERT INTO Estudiantes (nombre, edad, ciudad) VALUES ('Humberto Covilla', 22, 'Santa Marta');
INSERT INTO Estudiantes (nombre, edad, ciudad) VALUES ('Manuel Romero', 24, 'Monteria');
INSERT INTO Estudiantes (nombre, edad, ciudad) VALUES ('Felipe Aguirre', 23, 'Barranquilla');
INSERT INTO Estudiantes (nombre, edad, ciudad) VALUES ('Yarelvis Arguelles', 22, 'Santa Marta');
INSERT INTO Estudiantes (nombre, edad, ciudad) VALUES ('Carmelo Ariza', 18, 'Monteria');
INSERT INTO Estudiantes (nombre, edad, ciudad) VALUES ('Oscar Ballesta', 26, 'Barranquilla');
INSERT INTO Estudiantes (nombre, edad, ciudad) VALUES ('Pedro Bayona', 22, 'Santa Marta');
INSERT INTO Estudiantes (nombre, edad, ciudad) VALUES ('Alejandra Bolaño', 16, 'Sincelejo');
INSERT INTO Estudiantes (nombre, edad, ciudad) VALUES ('Yuranis Blanco', 20, 'Barranquilla');
INSERT INTO Estudiantes (nombre, edad, ciudad) VALUES ('Jonatan Pallares', 47, 'Valledupar');
INSERT INTO Estudiantes (nombre, edad, ciudad) VALUES ('Li Aparicio', 18, 'Sincelejo');

-- Consultas básicas

-- Consultar todos los registros de la tabla
SELECT * FROM Estudiantes;

-- Filtrar estudiantes por ciudad
SELECT * FROM Estudiantes WHERE ciudad = 'Barranquilla';

-- Consultar estudiantes mayores de 20 años
SELECT * FROM Estudiantes WHERE edad > 20;