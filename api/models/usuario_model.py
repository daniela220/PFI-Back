from ..database import DatabaseConnection


class Usuario:
    #(variable) _keys: list [str]
    _keys= ["id_usuario","nombre_usuario","contrasenia"]

    def __init__(self, id_usuario, nombre_usuario, contrasenia, imagen=None):
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario
        self.contrasenia = contrasenia
        self.imagen = imagen

    
    def serialize(self):
        return {
            "id_usuario": self.id_usuario,
            "nombre_usuario": self.nombre_usuario,
            "contrasenia": self.contrasenia
        }

    @classmethod
    def crear_usuario(cls, usuario):
        query = """INSERT INTO usuarios (id_usuario, nombre_usuario, contrasenia) VALUES (%(id_usuario)s, %(nombre_usuario)s, %(contrasenia)s"""
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
        query = (
            """SELECT id_usuario, nombre_usuario, contrasenia, imagen FROM usuarios"""
        )
        results = DatabaseConnection.fetch_all(query)
        usuarios = []
        for row in results:
            usuarios.append(cls(*row))
        return usuarios

    @classmethod
    def actualizar_usuario(cls, usuario):
        query = "UPDATE tif_db.usuarios SET"
        usuario_datos = usuario.__dict__
        usuario_update = []
        for key in usuario_datos.keys():
            if usuario_datos[key] is not None and key != "id_usuario":
                usuario_update.append(f"{key} = %({key})s")
        query += ", ".join(usuario_update)
        query += "WHERE user_id = %(id_usuario)s"
        DatabaseConnection.execute_query(query, usuario_datos)

    @classmethod
    def borrar_usuario(cls, usuario):
        query = "DELETE FROM tif_db.usuarios WHERE id_usuario = %(id_usuario)s"
        params = usuario.__dict__
        DatabaseConnection.execute_query(query, params)
