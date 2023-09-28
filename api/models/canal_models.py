from ..database import DatabaseConnection
class Canal:
    def __init__(self, canal_id, nombre_canal, descripcion, servidor_id):
        self.canal_id = canal_id
        self.nombre_canal = nombre_canal
        self.descripcion = descripcion
        self.servidor_id = servidor_id


    def serialize(self):
        return {
            "canal_id": self.canal_id,
            "nombre_canal": self.nombre_canal,
            "descripcion": self.descripcion,
            "servidor_id":self.servidor_id
        }


    @classmethod 
    def crear_canal(cls, canal):
        """Crea un nuevo canal en la base de datos utilizando los datos proporcionados en el objeto canal."""

        query = """INSERT INTO canales (nombre_canal, descripcion, servidor_id) VALUES (%(nombre_canal)s,%(descripcion)s, %(servidor_id)s)"""
        params = canal.__dict__
        DatabaseConnection.execute_query(query, params)

    @classmethod
    def obtener_todos(cls):
        """Obtiene todos los canales almacenados en la base de datos y los devuelve como una lista de objetos Canal"""
        query ="""SELECT * FROM canales"""
        results = DatabaseConnection.fetch_all(query)
        servidores = []
        for row in results:
            servidores.append(cls(*row))
        return servidores

