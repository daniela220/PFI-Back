from ..database import DatabaseConnection

class Servidor:
    def __init__(self, servidor_id, nombre_servidor, descripcion, usuario_id):
        self.servidor_id = servidor_id
        self.nombre_servidor = nombre_servidor
        self.descripcion = descripcion
        self.usuario_id = usuario_id

    def serialize(self):
        return {
                "servidor_id": self.servidor_id,
                "nombre_servidor": self.nombre_servidor,
                "descripcion": self.descripcion,
                "usuario_id":self.usuario_id
            }


    @classmethod
    def crear_servidor(cls, servidor):
        query = """INSERT INTO servidores (nombre_servidor, descripcion, usuario_id) VALUES (%(nombre_servidor)s, %(descripcion)s, %(usuario_id)s)"""
        params = servidor.__dict__
        DatabaseConnection.execute_query(query,params)


    @classmethod
    def borrar_servidor(cls,usuario_id):
        query = """
            DELETE FROM servidores
            WHERE usuario_id = %(usuario_id)s
        """
        params = {"usuario_id": usuario_id}
        DatabaseConnection.execute_query(query, params)

    
    def obtener_servidores_por_id_usuario(cls, usuario_id):
        query = """
            SELECT nombre_servidor
            FROM servidores
            INNER JOIN usuario_servidor ON servidores.servidor_id = usuario_servidor.servidor_id
            INNER JOIN usuarios ON usuario_servidor.usuario_id = usuarios.usuario_id
            WHERE usuarios.usuario_id = %(usuario_id)s;
            """
        params = {"usuario_id": usuario_id}
        results = DatabaseConnection.fetch_all(query, params)
        
        servidores = []

        for row in results:
            servidor = cls(**dict(zip(cls._keys, row)))
            servidores.append(servidor)

        if not servidores:
            return ["No perteneces a ningún servidor"]
        
        return servidores
    


    @classmethod
    def obtener_canales(cls, servidor_id):
        query = """
                SELECT id_canal, nombre_canal FROM canales WHERE servidor_id = %(servidor_id)s 
                """
        
        params = {
            "servidor_id" : servidor_id
        }
        results = DatabaseConnection.fetch_all(query, params)
        
        canales = []
        for row in results:
            canal = {"id_canal": row[0], "nombre_canal" : row[1]}
            canales.append(canal)
        return canales

        
        