from ..database import DatabaseConnection
class Canal:
    def __init__(self, id_canal, nombre_canal, descripcion, id_servidor):
        self.id_canal = id_canal
        self.nombre_canal = nombre_canal
        self.descripcion = descripcion
        self.id_servidor = id_servidor

    @classmethod 
    def crear_canal(cls, canal):
        query = """INSERT INTO canales (nombre_canal, descripcion, id_servidor) VALUES (%(id_canal)s, %(nombre_canal)s, %(id_servidor)s)"""
        params = canal.__dict__
        DatabaseConnection.execute_query(query, params)

    @classmethod
    def obtener_canales_servidor(cls, id_servidor):
        query = """
            SELECT id_canal, nombre_canal
            FROM canales
            WHERE id_servidor = %(id_servidor)s
        """
        params = {"id_servidor": id_servidor}
        results = DatabaseConnection.fetch_all(query, params)

        canales = []
        for row in results:
            canal = {"id_canal": row[0], "nombre_canal": row[1]}
            canales.append(canal)

        return canales