from config import Config
from flask import Flask
from .routes.usuario_route import bp_usuarios

def init_app():    
    app = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)
    app.register_blueprint(bp_usuarios)
    return app