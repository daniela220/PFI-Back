from ..database import DatabaseConnection

class Servidor:
    _keys= ["servidor_id","nombre_servidor","descripcion","usuario_id", "imagen"]

    def __init__(self, servidor_id, nombre_servidor, descripcion, imagen):
        """Inicializa una instancia de la clase Servidor con los atributos proporcionados."""
        self.servidor_id = servidor_id
        self.nombre_servidor = nombre_servidor
        self.descripcion = descripcion
        self.imagen = imagen

    def serialize(self):
        """Serializa los datos del servidor en un diccionario."""
        return {
                "servidor_id": self.servidor_id,
                "nombre_servidor": self.nombre_servidor,
                "descripcion": self.descripcion,
                "imagen": self.imagen
            }


    @classmethod
    def crear_servidor(cls, servidor):
        """Crea un nuevo servidor en la base de datos con los datos proporcionados."""
        query = """INSERT INTO servidores (nombre_servidor, descripcion) VALUES (%(nombre_servidor)s, %(descripcion)s)"""
        params = servidor.__dict__
        DatabaseConnection.execute_query(query,params)

    @classmethod
    def obtener_todos(cls):
        """Obtiene todos los servidores almacenados en la base de datos y los devuelve como una lista de objetos Servidor."""
        query = (
            """SELECT * FROM servidores"""
        )
        results = DatabaseConnection.fetch_all(query)
        servidores = []
        for row in results:
            servidores.append(cls(*row))
        return servidores
    
    @classmethod
    def obtener_uno(cls, servidor_id):
        """Obtiene un servidor por su ID y lo devuelve como un objeto Servidor."""
        query = (
            "SELECT * FROM servidores WHERE servidor_id = %(servidor_id)s" 
        )
        params = {"servidor_id" : servidor_id}
        result = DatabaseConnection.fetch_one(query, params)
        if result:
            return cls(**dict(zip(cls._keys, result)))
        else:
            return None


    @classmethod
    def borrar_servidor(cls,usuario_id):
        """Borra un servidor de la base de datos."""
        query = """
            DELETE FROM servidores
            WHERE usuario_id = %(usuario_id)s
        """
        params = {"usuario_id": usuario_id}
        DatabaseConnection.execute_query(query, params)
    
    @classmethod
    def obtener_canales(cls, servidor_id):
        """Obtiene los canales asociados a un servidor y los devuelve como una lista de diccionarios."""

        query = """
                SELECT canal_id, nombre_canal FROM canales WHERE servidor_id = %(servidor_id)s 
                """
        
        params = {
            "servidor_id" : servidor_id
        }
        results = DatabaseConnection.fetch_all(query, params)
        
        canales = []
        print("--------------", results)
        for row in results:
            canal = {"canal_id": row[0], "nombre_canal" : row[1]}
            canales.append(canal)
        return canales
    


    ##############################
    @classmethod
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
    
        