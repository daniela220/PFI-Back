from ..database import DatabaseConnection


class Usuario:
    #(variable) _keys: list [str]
    _keys= ["usuario_id","nombre_usuario","contrasenia"]

    def __init__(self, usuario_id, nombre_usuario, contrasenia, imagen=None):
        self.usuario_id = usuario_id
        self.nombre_usuario = nombre_usuario
        self.contrasenia = contrasenia
        self.imagen = imagen

    
    def serialize(self):
        return {
            "usuario_id": self.usuario_id,
            "nombre_usuario": self.nombre_usuario,
            "contrasenia": self.contrasenia,
            "imagen": self.imagen
        }

    @classmethod
    def crear_usuario(cls, usuario):
        query = """INSERT INTO usuarios (nombre_usuario, contrasenia, imagen) VALUES (%(nombre_usuario)s, %(contrasenia)s, %(imagen)s)"""
        params = usuario.__dict__
        DatabaseConnection.execute_query(query, params)

    @classmethod
    def obtener_por_id(cls, usuario_id):
        query = """SELECT usuario_id, nombre_usuario, contrasenia, imagen FROM usuarios WHERE usuario_id = %(usuario_id)s"""
        params = {"usuario_id": usuario_id}
        result = DatabaseConnection.fetch_one(query, params)
        if result:
            return cls(**dict(zip(cls._keys, result)))
        else:
            return None

    @classmethod
    def obtener_todos(cls):
        query = (
            """SELECT usuario_id, nombre_usuario, contrasenia, imagen FROM usuarios"""
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
            if usuario_datos[key] is not None and key != "usuario_id":
                usuario_update.append(f"{key} = %({key})s")
        query += ", ".join(usuario_update)
        query += "WHERE user_id = %(usuario_id)s"
        DatabaseConnection.execute_query(query, usuario_datos)

    @classmethod
    def borrar_usuario(cls, usuario):
        query = "DELETE FROM tif_db.usuarios WHERE usuario_id = %(usuario_id)s"
        params = usuario.__dict__
        DatabaseConnection.execute_query(query, params)
