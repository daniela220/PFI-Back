from flask import Blueprint
from ..controllers.usuario_controller import UsuarioController

bp_usuarios = Blueprint("usuarios",__name__)
bp_usuarios.route("/", methods = ["GET"])(UsuarioController.get_usuarios)
bp_usuarios.route("/<int:usuario_id>", methods = ["GET"])(UsuarioController.get_usuario)
bp_usuarios.route("/", methods = ["POST"])(UsuarioController.crear)
bp_usuarios.route("/<int:usuario_id>", methods=["PUT"])(UsuarioController.update)
bp_usuarios.route('/<int:usuario_id>', methods=['DELETE'])(UsuarioController.delete)
bp_usuarios.route('/<int:usuario_id>/servidores', methods = ["GET"])(UsuarioController.get_servidores)