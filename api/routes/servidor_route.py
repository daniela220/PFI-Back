from flask import Blueprint
from ..controllers.servidor_controller import ServidorController

bp_servidores = Blueprint("servidores", __name__)
bp_servidores.route("<int:servidor_id>/canales", methods = ["GET"])(ServidorController.obtener_canales_de_servidor)
bp_servidores.route("/", methods=["GET"])(ServidorController.obtener_todos)
bp_servidores.route("/<int:servidor_id>", methods=["GET"])(ServidorController.obtener_uno)
bp_servidores.route("/", methods = ["POST"])(ServidorController.crear_nuevo)


############

