from flask import request, jsonify
from ..models.servidor_model import Servidor

class ServidorController:
    @classmethod
    def crear_nuevo(self):
        """Crea un nuevo servidor utilizando los datos proporcionados en la solicitud JSON."""
        data = request.json
        servidor = Servidor(**data)

        nombre_servidor = data.get('nombre_servidor')

        Servidor.crear_servidor(servidor)
        return {'message': 'servidor creado exitosamente'}, 200
    
    @classmethod
    def obtener_todos(self):
        """Devuelve todos los servidores"""
        servidores_obj = Servidor.obtener_todos()
        servidores = []
        for servidor in servidores_obj:
            servidores.append(servidor.serialize())
        return servidores, 200
    

    @classmethod
    def obtener_uno(self, servidor_id):
        """Devuelve un servidor"""
        resultado = Servidor.obtener_uno(servidor_id)
        if resultado is not None:
            return resultado.serialize(), 200
    
    @classmethod
    def obtener_canales_de_servidor(cls, servidor_id):
        """Obtiene los canales asociados a un servidor y los devuelve como JSON."""
        canales = Servidor.obtener_canales(servidor_id)
        if not canales:
            return jsonify({"message": "No se encontraron canales para este servidor"}), 404
        return jsonify(canales), 200
    


    @classmethod
    def obtener_servidores_por_usuario(self, nombre_usuario):
        """Obtiene los servidores asociados a un usuario y los devuelve como JSON."""
        # nombre_usuario = Usuario(nombre_usuario=nombre_usuario)
        resultado = Servidor.obtener_servidor_por_usuario(nombre_usuario=nombre_usuario)
        servidores = []
        if len(resultado) > 0:
            for servidor in resultado:
                servidores.append(servidor.serialize())
            return servidores, 200        
    