from flask import request, jsonify
from ..models.usuario_models import Usuario

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
        nuevo_usuario = Usuario(
            nombre_usuario=data.get("nombre_usuario"),
            contrasenia = data.get("contrasenia")
            )
        Usuario.crear_usuario(nuevo_usuario)
        return jsonify({"message": "Usuario creado exitosamente"}), 201
        
    @classmethod
    def update(cls, usuario_id):
        try:
            data = request.json
            usuario_actualizado = Usuario(usuario_id, **data)
            Usuario.actualizar_usuario(usuario_actualizado)
            return jsonify({"message": "Usuario actualizado exitosamente"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500    

    @classmethod
    def delete(cls, usuario_id):
        usuario = Usuario.obtener_por_id(usuario_id)
        
        if usuario:
            Usuario.borrar_usuario(usuario)
            return jsonify({"message": "Usuario eliminado exitosamente"}), 200
        else:
            return jsonify({"message": "Usuario no encontrado"}), 404
        

    ######################
    @classmethod
    def get_servidores(cls, usuario_id):
        usuario=Usuario(usuario_id=usuario_id)
        servidores = []
        for servidor in Usuario.get_servidores(usuario_id):
            print(servidor)
            servidores.append(servidor.serialize())
        return servidores, 200
    

