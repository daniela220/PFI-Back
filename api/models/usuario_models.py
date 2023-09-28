from ..database import DatabaseConnection


class Usuario:
    #(variable) _keys: list [str]
    _keys= ["usuario_id","nombre_usuario","contrasenia"]

    def __init__(self, usuario_id, nombre_usuario, contrasenia, imagen=None):
        self.usuario_id = usuario_id
        self.nombre_usuario = nombre_usuario
        self.contrasenia = contrasenia
        self.imagen = imagen

    """def __init__(self, **kwargs):
        self.usuario_id = kwargs.get("usuario_id")
        self.nombre_usuario = kwargs.get("nombre_usuario")
        self.contrasenia = kwargs.get("contrasenia")
        self.imagen = kwargs.get("imagen")"""
    
    def serialize(self):
        return {
            "usuario_id": self.usuario_id,
            "nombre_usuario": self.nombre_usuario,
            "contrasenia": self.contrasenia
        }

    @classmethod
    def crear_usuario(cls, usuario):
        query = """INSERT INTO usuarios (nombre_usuario, contrasenia) VALUES (%(nombre_usuario)s, %(contrasenia)s)"""
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
        usuario_updates = []
        for key in usuario_datos.keys():
            if usuario_datos[key] is not None and key != "usuario_id":
                usuario_updates.append(f"{key} = %({key})s")
        query += ", ".join(usuario_updates)
        query += " WHERE usuario_id = %(usuario_id)s"
        DatabaseConnection.execute_query(query, usuario_datos)

    @classmethod
    def borrar_usuario(cls, usuario):
        query = "DELETE FROM tif_db.usuarios WHERE usuario_id = %(usuario_id)s"
        params = usuario.__dict__
        DatabaseConnection.execute_query(query, params)


###############################
    @classmethod
    def get_servidores(cls, usuario):
        query = """
            SELECT nombre_servidor
            FROM servidores
            INNER JOIN usuario_servidor ON servidores.servidor_id = usuario_servidor.servidor_id
            INNER JOIN usuarios ON usuario_servidor.usuario_id = usuarios.usuario_id
            WHERE usuarios.usuario_id = %(usuario_id)s;
            """
        params = Usuario.__dict__
        results = DatabaseConnection.fetch_all(query, params)
        
        servidores = []
        from .servidor_models import Servidor

        for row in results:
            servidores.append(Servidor(**dict(zip(Servidor._keys, row))))
        return servidores
