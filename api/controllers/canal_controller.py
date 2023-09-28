from flask import request
from ..models.canal_models import Canal

class CanalController:
    @classmethod
    def crear_canal(cls):
        data = request.json
        canal = Canal(**data)
        nombre_canal = data.get('nombre_canal')
        Canal.crear_canal(canal)
        return {'message': 'canal creado exitosamente'}, 200


    @classmethod
    def obtener_todos(cls):
        canales_obj = Canal.obtener_todos()
        canales = []
        for canal in canales_obj:
            canales.append(canal.serialize())
        return canales, 200

    