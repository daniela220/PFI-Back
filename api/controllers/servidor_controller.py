from flask import request, jsonify
from ..models.servidor_model import Servidor

class ServidorController:
    @classmethod
    def get_servidores_usuario(cls, usuario_id):
        servidores = Servidor.obtener_servidores_por_id_usuario(usuario_id)
        if not servidores:
            return jsonify({"message": "No perteneces a ningún servidor"}), 404        
        servidores_json = [servidor.serialize() for servidor in servidores]
        return jsonify(servidores_json), 200
