from api import init_app
from flask import Flask, request, jsonify
from config import Config
from api.models.usuarios import Usuario  
from api.models.mensajes import Mensaje  
from api.models.canales import Canal  
from api.models.servidores import Servidor 

app = init_app()

if __name__ == "__main__":
    app.run(debug=True)

# Hoola Soy German