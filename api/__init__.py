from config import Config
from flask import Flask
from .routes.usuario_route import bp_usuarios
from .routes.servidor_route import bp_servidores
from .routes.canal_route import bp_canales
from .routes.mensaje_route import bp_mensajes


from .routes.auth import auth_bp
from flask_session import Session


def init_app():    
    app = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)
    app.register_blueprint(bp_usuarios)
    return app