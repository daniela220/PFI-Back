from ..models.auth.user_model import User
from flask import request, session

class UserController:

    user_name = ''

    @classmethod
    def login(cls):
        data = request.json
        user = User(
            nombre_usuario = data.get('nombre_usuario'),
            contrasenia = data.get('contrasenia')
        )        
        # print("Datos de inicio de sesion", data)
        cls.user_name = data.get('nombre_usuario')
        if User.is_registered(user):
            session['username'] = data.get('nombre_usuario')
            # print("Sesion claves: ", session.keys())
            # print("Sesión iniciada para:", session.get('username'))
            return {"message": "Sesion iniciada"}, 200
        else:
            return {"message": "Usuario o contraseña incorrectos"}, 401
    
    @classmethod
    def show_profile(cls):
        # username = session.get('nombre_usuario')
        # print("Sesion Claves: ", session.keys())
        username = cls.user_name
        print("variable ", username)
        # print("Usuario en sesion:", session.get("username"))
        if username is None:
            return {"message": "Usuario no encontrado"}, 404
        else:
            user = User.get(User(nombre_usuario = username))
            # return user.serialize(), 200
            return user, 200
    
    @classmethod
    def logout(cls):
        print("logout", session.keys())
        session.pop('username', None)
        cls.user_name = ''
        return {"message": "Sesion cerrada"}, 200