from flask import Blueprint
from ..controllers.mensaje_controller import MensajeController


bp_mensajes = Blueprint("mensajes",__name__)
bp_mensajes.route("/<int:canal_id>/canal", methods = ["GET"])(MensajeController.obtener_mensajes_canal)
bp_mensajes.route("/ordenar", methods = ["GET"])(MensajeController.obtener_mensajes_ordenados)
bp_mensajes.route("/", methods = ["POST"])(MensajeController.crear_mensaje)

