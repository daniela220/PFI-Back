from flask import Blueprint
from ..controllers.usuario_controller import UsuarioController

bp_usuarios = Blueprint("users",__name__)
bp_usuarios.route("/", methods = ["GET"])(UsuarioController.get_usuarios)
bp_usuarios.route("/usuario/<int:id_usuario>", methods = ["GET"])(UsuarioController.get_usuario)
bp_usuarios.route("/", methods = ["POST"])(UsuarioController.crear)
bp_usuarios.route("/<int:user_id>", methods=["PUT"])(UsuarioController.update)
bp_usuarios.route('/<int:user_id>/servers', methods = ["GET"])(UsuarioController.get_servidores)