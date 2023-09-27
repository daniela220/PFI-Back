from ..models.auth.user_model import User
from flask import request, session

class UserController:

    @classmethod
    def login(cls):
        data = request.json
        user = User(
            nombre_usuario = data.get('nombre_usuario'),
            contrasenia = data.get('contrasenia')
        )        
        print("Datos de inicio de sesion", data)
        if User.is_registered(user):
            session['username'] = data.get('nombre_usuario')
            print("Sesión iniciada para:", session.get('username'))
            return {"message": "Sesion iniciada"}, 200
        else:
            return {"message": "Usuario o contraseña incorrectos"}, 401
    
    """ @classmethod
    def show_profile(cls):
        username = session.get('username')
        user = User.get(User(username = username))
        if user is None:
            return {"message": "Usuario no encontrado"}, 404
        else:
            return {
                "user_id": user.user_id,
                "username": user.username,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "date_of_birth": user.date_of_birth,
                "phone_number": user.phone_number,
                "creation_date": user.creation_date,
                "last_login": user.last_login,
                "status_id": user.status_id,
                "role_id": user.role_id
            }, 200 """

    @classmethod
    def show_profile(cls):
        # username = session.get('nombre_usuario')
        username = session.get('username')
        print("Usuario en sesion:", session)
        if username is None:
            return {"message": "Usuario no encontrado"}, 404
        else:
            user = User.get(User(nombre_usuario = username))
            return user.serialize(), 200
    
    @classmethod
    def logout(cls):
        session.pop('username', None)
        return {"message": "Sesion cerrada"}, 200