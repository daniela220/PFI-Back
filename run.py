from api import init_app
from flask import Flask, request

app = init_app()

if __name__ == "__main__":
    app.run(debug=True)

# Hoola Soy German