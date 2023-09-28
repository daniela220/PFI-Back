from flask import request, jsonify
from ..models.mensaje_models import Mensaje

class MensajeController:

    @classmethod
    def crear_mensaje(self, canal_id):
        """Publica un mensaje en el chat"""
        data = request.json
        chat = Mensaje(**data)

        chat.canal_id = canal_id
        
        Mensaje.crear_mensaje(chat)
        return {"message": "Mensaje publicado exitosamente"}

    @classmethod
    def obtener_mensajes_canal(cls, canal_id):
        mensaje_obj = Mensaje.obtener_mensajes_por_canal(canal_id)
        mensajes = []
        for mensaje in mensaje_obj:
            mensajes.append(mensaje.serialize())
        return mensajes, 200

    @classmethod
    def obtener_mensajes_ordenados(cls):
        mensajes = Mensaje.obtener_mensajes_ordenados()

        if not mensajes:
            return jsonify({"message": "No se encontraron mensajes"}), 404

        mensajes_json = [mensaje.serialize() for mensaje in mensajes]
        return jsonify(mensajes_json), 200
