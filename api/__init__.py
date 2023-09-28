from config import Config
from flask import Flask
from .routes.usuario_route import bp_usuarios
from .routes.auth import auth_bp
from flask_session import Session


def init_app():    
    app = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)
    app.config['SECRET_KEY'] = 'my precious'
    app.config["SESSION_PERMANENT"] = False
    app.config['SESSION_TYPE'] = 'filesystem'
    Session(app)
    app.register_blueprint(bp_usuarios)
    app.register_blueprint(auth_bp, url_prefix = '/auth')
    return app