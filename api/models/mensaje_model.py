from ..database import DatabaseConnection

class Mensaje:
    def __init__(self, id_mensaje, contenido, fecha_envio, id_canal, id_usuario):
        self.id_mensaje = id_mensaje
        self.contenido = contenido
        self.fecha_envio = fecha_envio
        self.id_canal = id_canal
        self.id_usuario = id_usuario

    @classmethod
    def crear_mensaje(cls, contenido, id_usuario, id_canal):
        query = """INSERT INTO mensajes (contenido, id_usuario, id_canal) VALUES (%(contenido)s, %(id_usuario)s %(id_canal)s)"""
        params = {
            "contenido": contenido,
            "id_usuario": id_usuario,
            "id_canal": id_canal
        }
        DatabaseConnection.execute_query(query, params)

    @classmethod
    def obtener_mensajes_por_canal(cls, id_canal):
        query = """SELECT FROM mensajes WHERE id_canal = %(id_canal)s"""
        params = {
            "id_canal" : id_canal
        }
        resultados = DatabaseConnection.fetch_all(query,params)
        mensajes = []
        for resultado in resultados:
            mensaje = cls(**dict(zip(cls._keys, resultado)))
            mensajes.append(mensaje)
        return mensaje
        
    @classmethod
    def editar_mensaje(cls, id_mensaje, nuevo_contenido):
        query = """UPDATE mensajes SET contenido = %(nuevo_contenido)s WHERE id_mensaje = %(id_mensaje)s"""
        params = {
            "nuevo_contenido": nuevo_contenido,
            "id_mensaje": id_mensaje
        }
        DatabaseConnection.execute_query(query, params) 

    def eliminar_mensaje(cls, id_mensaje):
        query = """DELETE FROM mensajes WHERE id_mensaje = %(id_mensaje)s"""
        params = {
            "id_mensaje": id_mensaje
        }
        DatabaseConnection.execute_query(query, params)

    