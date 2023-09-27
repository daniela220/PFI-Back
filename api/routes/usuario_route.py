from flask import Blueprint, request, jsonify
from ..controllers.usuario_controller import UsuarioController

bp_usuarios = Blueprint("users",__name__)
@bp_usuarios.before_request
def set_json_content_type():
    print('works')
    if request.method == "POST" and request.headers["Content-Type"] != "application/json":
        print('if', request.content_type) 
        return jsonify({"error": "Unsupported Media Type"}), 415
    
bp_usuarios.route("/", methods = ["GET"])(UsuarioController.get_usuarios)
bp_usuarios.route("/usuario/<int:id_usuario>", methods = ["GET"])(UsuarioController.get_usuario)
bp_usuarios.route("/crear", methods = ["POST"])(UsuarioController.crear)
bp_usuarios.route("/<int:user_id>", methods=["PUT"])(UsuarioController.update)
bp_usuarios.route("/<int:user_id>/servers", methods = ["GET"])(UsuarioController.get_servidores)