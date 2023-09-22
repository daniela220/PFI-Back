from flask import request, jsonify
from ..models.usuario_model import Usuario

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
    
        

