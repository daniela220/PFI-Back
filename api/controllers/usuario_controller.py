from flask import request, jsonify
from ..models.usuario_models import Usuario
from ..models.servidor_models import Servidor


class UsuarioController:
    @classmethod
    def get_usuarios(cls):
        """Obtiene todos los usuarios y los devuelve en una lista serializada."""
        usuarios = []
        for usuario in Usuario.obtener_todos():
            usuarios.append(usuario.serialize())
        return usuarios, 200

    @classmethod
    def get_usuario(cls, id_usuario):
        """Obtiene un usuario a traves del id_usuario y lo devuelve en una lista serializada."""
        usuario = Usuario.obtener_por_id(id_usuario)
        if usuario:
            usuario.serialize(), 200

    @classmethod
    def crear(cls):
        """Crea un nuevo usuario utilizando los datos proporcionados en la solicitud JSON."""

        data = request.json
        nuevo_usuario = Usuario(
            usuario_id=data.get("usuario_id"),
            nombre_usuario=data.get("nombre_usuario"),
            contrasenia = data.get("contrasenia")
            )
        Usuario.crear_usuario(nuevo_usuario)
        return jsonify({"message": "Usuario creado exitosamente"}), 201
        
    @classmethod
    def update(cls, usuario_id):
        """Actualiza un usuario existente con los datos proporcionados en la solicitud JSON."""
        try:
            data = request.json
            usuario_actualizado = Usuario(usuario_id, **data)
            Usuario.actualizar_usuario(usuario_actualizado)
            return jsonify({"message": "Usuario actualizado exitosamente"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500    

    @classmethod
    def delete(cls, usuario_id):
        """Elimina un usuario por su ID."""
        usuario = Usuario.obtener_por_id(usuario_id)
        
        if usuario:
            Usuario.borrar_usuario(usuario)
            return jsonify({"message": "Usuario eliminado exitosamente"}), 200
        else:
            return jsonify({"message": "Usuario no encontrado"}), 404
        

    @classmethod
    def get_servidores(cls, usuario_id):
        """Obtiene los servidores asociados a un usuario y los devuelve como JSON."""
        usuario = Usuario.obtener_por_id(usuario_id)
        servidores = Usuario.get_servidores(usuario)
        return servidores, 200

    

