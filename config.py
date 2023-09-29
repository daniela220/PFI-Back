class Config:
    SERVER_NAME = "127.0.0.1:5000"
    DEBUG = True
    APP_NAME = 'Aplicación de Mensajería'
    DESCRIPTION = """Se proporciona una API REST que permite
    a la interfaz de usuario interactuar con la base de datos y 
    acceder a las funcionalidades de la aplicación."""
    DEVELOPERS = [
        {'nombre': 'Germán', 'apellido': 'Aguirre'},
        {'nombre':'Daniela', 'apellido':'Farfán'},
        {'nombre':'Fabricio', 'apellido':'Garcia'}
    ]
    VERSION = '1.0.0'

    TEMPLATE_FOLDER = "templates/"
    STATIC_FOLDER = "static/"