from flask import Blueprint
from ..controllers.canal_controller import CanalController

bp_canales = Blueprint("canales",__name__)
bp_canales.route("/", methods = ["GET"])(CanalController.obtener_todos)
bp_canales.route("/", methods = ["POST"])(CanalController.crear_canal)

