from ..database import DatabaseConnection

class Mensaje:
    _keys= ["id_mensaje","contenido","fecha_envio","canal_id","usuario_id"]

    def __init__(self, id_mensaje, contenido, fecha_envio, canal_id, usuario_id):
        self.id_mensaje = id_mensaje
        self.contenido = contenido
        self.fecha_envio = fecha_envio
        self.canal_id = canal_id
        self.usuario_id = usuario_id

    def serialize(self):
        """Serializa los datos del mensaje en un diccionario."""
        return {
            "usuario_id": self.usuario_id,
            "id_mensaje": self.id_mensaje,
            "contenido": self.contenido,
            "fecha_envio":self.fecha_envio,
            "canal_id":self.canal_id,
            "usuario_id": self.usuario_id
        }


    @classmethod
    def crear_mensaje(cls, contenido, usuario_id, canal_id):
        """Crea un nuevo mensaje con los datos proporcionados."""
        query = """INSERT INTO mensajes (contenido, usuario_id, canal_id) VALUES (%(contenido)s, %(usuario_id)s %(canal_id)s)"""
        params = {
            "contenido": contenido,
            "usuario_id": usuario_id,
            "canal_id": canal_id
        }
        DatabaseConnection.execute_query(query, params)

    @classmethod
    def obtener_mensajes_por_canal(cls, canal_id):
        """Obtiene todos los mensajes de un canal específico y los devuelve como una lista."""
        query = """SELECT * FROM mensajes WHERE canal_id = %(canal_id)s"""
        params = {
            "canal_id" : canal_id
        }
        resultados = DatabaseConnection.fetch_all(query,params)
        mensajes = []
        for resultado in resultados:
            mensaje = cls(**dict(zip(cls._keys, resultado)))
            mensajes.append(mensaje)
        return mensajes
        
    @classmethod
    def editar_mensaje(cls, id_mensaje, nuevo_contenido):
        """Edita el contenido de un mensaje existente."""
        query = """UPDATE mensajes SET contenido = %(nuevo_contenido)s WHERE id_mensaje = %(id_mensaje)s"""
        params = {
            "nuevo_contenido": nuevo_contenido,
            "id_mensaje": id_mensaje
        }
        DatabaseConnection.execute_query(query, params) 

    def eliminar_mensaje(cls, id_mensaje):
        """Elimina un mensaje existente de la base de datos."""
        query = """DELETE FROM mensajes WHERE id_mensaje = %(id_mensaje)s"""
        params = {
            "id_mensaje": id_mensaje
        }
        DatabaseConnection.execute_query(query, params)


    @classmethod
    def obtener_mensajes_ordenados(cls):
        """Obtiene todos los mensajes de la base de datos y los devuelve en orden ascendente de fecha y hora de envío."""
        query = """
            SELECT id_mensaje, contenido, fecha_envio, canal_id, usuario_id
            FROM mensajes
            ORDER BY fecha_envio ASC; """
        
        results = DatabaseConnection.fetch_all(query)

        mensajes = []
        for row in results:
            mensaje = cls(**dict(zip(cls._keys, row)))
            mensajes.append(mensaje)

        return mensajes
