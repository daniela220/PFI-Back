from api import init_app
from flask import Flask, request
from flask_cors import CORS


app = init_app()
cors = CORS(app, resources={r"/*":{"origins": "http://127.0.0.1:5500"}})

if __name__ == "__main__":
    app.run(debug=True)

# Hoola Soy German