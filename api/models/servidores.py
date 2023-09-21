from ..database import DatabaseConnection

class Servidor:
    def __init__(self, id_servidor, nombre_servidor, descripcion, id_usuario):
        self.id_servidor = id_servidor
        self.nombre_servidor = nombre_servidor
        self.descripcion = descripcion
        self.id_usuario = id_usuario



    @classmethod
    def crear_servidor(cls, servidor):
        query = """INSERT INTO servidores (nombre_servidor, descripcion, id_usuario) VALUES (%(nombre_servidor)s, %(descripcion)s, %(id_usuario)s)"""
        params = servidor.__dict__
        DatabaseConnection.execute_query(query,params)


    @classmethod
    def borrar_servidor(cls,id_servidor):
        query = """
            DELETE FROM servidores
            WHERE id_servidor = %(id_servidor)s
        """
        params = {"id_servidor": id_servidor}
        DatabaseConnection.execute_query(query, params)

    
    @classmethod
    def obtener_servidores_del_usuario(cls, id_usuario):
        query = """
            SELECT id_servidor, nombre, descripcion, id_usuario
            FROM servidores
            WHERE id_usuario = %(id_usuario)s
        """
        params = {"id_usuario": id_usuario}
        results = DatabaseConnection.fetch_all(query, params)
        
        servidores = []

        for row in results:
            servidor = cls(**dict(zip(cls._keys, row)))
            servidores.append(servidor)

        if not servidores:
            return ["No perteneces a ningún servidor"]
        
        return servidores

    @classmethod
    def obtener_canales(cls, id_servidor):
        query = """
                SELECT id_canal, nombre_canal FROM canales WHERE id_servidor = %(id_servidor)s 
                """
        
        params = {
            "id_servidor" : id_servidor
        }
        results = DatabaseConnection.fetch_all(query, params)
        
        canales = []
        for row in results:
            canal = {"id_canal": row[0], "nombre_canal" : row[1]}
            canales.append(canal)
        return canales

        
        