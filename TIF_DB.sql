CREATE DATABASE IF NOT EXISTS TIF_DB;
USE TIF_DB;

CREATE TABLE usuarios (
  usuario_id INT AUTO_INCREMENT PRIMARY KEY,
  nombre_usuario VARCHAR(50) NOT NULL,
  contrasenia VARCHAR(255) NOT NULL,
  imagen VARCHAR(255) NOT NULL
);

CREATE TABLE servidores (
  servidor_id INT AUTO_INCREMENT PRIMARY KEY,
  nombre_servidor VARCHAR(255) NOT NULL,
  descripcion TEXT
);

CREATE TABLE canales (
  canal_id INT AUTO_INCREMENT PRIMARY KEY,
  nombre_canal VARCHAR(50) NOT NULL,
  descripcion TEXT,
  servidor_id INT NOT NULL,
  FOREIGN KEY (servidor_id) REFERENCES servidores(servidor_id)
);

CREATE TABLE usuario_servidor (
  id INT AUTO_INCREMENT PRIMARY KEY,
  servidor_id INT NOT NULL,
  usuario_id INT NOT NULL,
  FOREIGN KEY (servidor_id) REFERENCES servidores(servidor_id),
  FOREIGN KEY (usuario_id) REFERENCES usuarios(usuario_id)
);

CREATE TABLE mensajes (
  id_mensaje INT AUTO_INCREMENT PRIMARY KEY,
  contenido TEXT NOT NULL,
  fecha_envio TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  canal_id INT NOT NULL,
  usuario_id INT NOT NULL,
  FOREIGN KEY (canal_id) REFERENCES canales(canal_id),
  FOREIGN KEY (usuario_id) REFERENCES usuarios(usuario_id)
);
