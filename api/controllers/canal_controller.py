from flask import request
from ..models.canal_model import Canal

class CanalController:
    @classmethod
    def crear_canal(cls):
        """ Crea un nuevo canal utilizando los datos proporcionados en la solicitud JSON"""
        data = request.json
        canal = Canal(**data)
        nombre_canal = data.get('nombre_canal')
        Canal.crear_canal(canal)
        return {'message': 'canal creado exitosamente'}, 200


    @classmethod
    def obtener_todos(cls):
        """Obtiene todos los canales y los serializa en una lista de diccionarios."""
        canales_obj = Canal.obtener_todos()
        canales = []
        for canal in canales_obj:
            canales.append(canal.serialize())
        return canales, 200

    