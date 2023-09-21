from api import init_app
from flask import Flask, request, jsonify
from config import Config
from api.models.usuarios import Usuario  # Importa la clase Usuario desde el módulo models.usuario
from api.models.mensajes import Mensaje  # Importa la clase Mensaje desde el módulo models.mensaje
from api.models.canales import Canal  # Importa la clase Canal desde el módulo models.canal
from api.models.servidores import Servidor  # Importa la clase Servidor desde el módulo models.servidor

app = init_app()

if __name__ == "__main__":
    app.run(debug=True)