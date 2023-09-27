from flask import request, jsonify
from api.models.usuario_model import Usuario
import uuid

class UsuarioController:
    @classmethod
    def get_usuarios(cls):
        usuarios = []
        for usuario in Usuario.obtener_todos():
            usuarios.append(usuario.serialize())
        return usuarios, 200

    @classmethod
    def get_usuario(cls, id_usuario):
        usuario = Usuario.obtener_por_id(id_usuario)
        if usuario:
            usuario.serialize(), 200

    @classmethod
    def crear(cls):
        data = request.json
        nuevo_user_id = str(uuid.uuid4())
        data["usuario_id"] = nuevo_user_id
        nuevo_usuario = Usuario(**data)
        Usuario.crear_usuario(nuevo_usuario)
        return jsonify({"message": "Usuario creado exitosamente"}), 201
        
    @classmethod
    def update(cls):
        pass

    @classmethod
    def delete(cls):
        pass

    @classmethod
    def get_servidores(cls):
        pass
    
    @classmethod
    def get_next_user_id(cls):
        # Incrementa el último user_id y lo devuelve como un número entero
        cls.last_user_id += 1
        return cls.last_user_id