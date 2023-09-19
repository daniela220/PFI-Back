from ..database import DatabaseConnection

class Usuario:
    def __init__(self, id_usuario, nombre_usuario, contrasenia, imagen = None):
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario
        self.contrasenia = contrasenia
        self.imagen = imagen

   
    @classmethod
    def crear_usuario(cls, usuario):
        query = """INSERT INTO usuarios (id_usuario, nombre_usuario, contrasenia, imagen) VALUES (%(id_usuario)s, %(nombre_usuario)s, %(contrasenia)s, %(imagen)s)"""
        params = usuario.__dict__
        DatabaseConnection.execute_query(query, params)


    @classmethod
    def obtener_por_id(cls, id_usuario):
        query = """SELECT id_usuario, nombre_usuario, contrasenia, imagen FROM usuarios WHERE id_usuario = %(id_usuario)s"""
        params = {"id_usuario": id_usuario}
        result = DatabaseConnection.fetch_one(query, params)
        if result:
            return cls(**dict(zip(cls._keys, result)))
        else:
            return None

    @classmethod
    def obtener_todos(cls):
        query = """SELECT id_usuario, nombre_usuario, contrasenia, imagen FROM usuarios"""
        results = DatabaseConnection.fetch_all(query)
        usuarios = []
        for row in results:
            usuarios.append(cls(*row)) 
        return usuarios

    def actualizar_usuario(self):
        pass

    def borrar_usuario(self):
        pass

    