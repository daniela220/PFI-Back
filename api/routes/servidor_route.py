from flask import Blueprint
from ..controllers.servidor_controller import ServidorController

bp_servidores = Blueprint("servidores", __name__)
bp_servidores.route("/servidores/<int:usuario_id>", methods = ["GET"])(ServidorController.get_servidores_usuario)
