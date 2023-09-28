from flask import request, jsonify
from ..models.usuario_models import Usuario
import uuid

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
        print(id_usuario, "Hola este es el comentario -------------------------------------------")
        # if usuario:
        #     usuario.serialize(), 200
        return usuario.serialize(), 200


    @classmethod
    def crear(cls):
        data = request.json
        
        if "nombre_usuario" not in data or "contrasenia" not in data:
            return jsonify({"message:" "Faltan usuario o contraseña"}), 400
        
        nuevo_user_id = str(uuid.uuid4())
        data["usuario_id"] = nuevo_user_id
        print(data)
        nuevo_usuario = Usuario(**data)
        try:
            Usuario.crear_usuario(nuevo_usuario)
            return jsonify({"message": "Usuario creado exitosamente"}), 201
        except Exception:
            return jsonify({"message:" "Error al crear el usuario"}), 500
        
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
        

    ######################
    @classmethod
    def get_servidores(cls, usuario_id):
        """Obtiene los servidores asociados a un usuario y los devuelve como JSON."""
        usuario=Usuario(usuario_id=usuario_id)
        servidores = []
        for servidor in Usuario.get_servidores(usuario_id):
            print(servidor)
            servidores.append(servidor.serialize())
        return servidores, 200
    

