from config import Config
from flask import Flask
from .routes.usuario_route import bp_usuarios
from .routes.servidor_route import bp_servidores
from .routes.canal_route import bp_canales
from .routes.mensaje_route import bp_mensajes



def init_app():    
    app = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)
    app.register_blueprint(bp_usuarios, url_prefix = "/usuarios")
    app.register_blueprint(bp_servidores, url_prefix="/servidores")
    app.register_blueprint(bp_canales, url_prefix="/canales")
    app.register_blueprint(bp_mensajes, url_prefix="/mensajes")

    return app