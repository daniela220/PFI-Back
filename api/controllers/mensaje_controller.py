from flask import request, jsonify
from ..models.mensaje_model import Mensaje
import uuid
from datetime import date

class MensajeController:

    @classmethod
    def crear_mensaje(self, canal_id):
        """Crea y publica un mensaje en el chat del canal especificado."""
        data = request.json

        id_mensaje = str(uuid.uuid4())
        data["id_mensaje"] = id_mensaje

        fecha = date.today()
        data["fecha_envio"] = str(fecha)

        chat = Mensaje(**data)
        chat.canal_id = canal_id
        print("<<<<<<<<<<<<<<<<<<<<<<", chat)

        try:
            Mensaje.crear_mensaje(chat)
            return jsonify({"message": "Mensaje publicado exitosamente"}), 201
        except Exception:
            return jsonify({"message:" "Error al crear el usuario"}), 500

    @classmethod
    def obtener_mensajes_canal(cls, canal_id):
        """Obtiene todos los mensajes publicados en un canal especificado y los serializa."""
        mensaje_obj = Mensaje.obtener_mensajes_por_canal(canal_id)
        mensajes = []
        for mensaje in mensaje_obj:
            mensajes.append(mensaje.serialize())
        return mensajes, 200

    @classmethod
    def obtener_mensajes_ordenados(cls):
        """Obtiene todos los mensajes y los devuelve en orden."""
        mensajes = Mensaje.obtener_mensajes_ordenados()

        if not mensajes:
            return jsonify({"message": "No se encontraron mensajes"}), 404

        mensajes_json = [mensaje.serialize() for mensaje in mensajes]
        return jsonify(mensajes_json), 200