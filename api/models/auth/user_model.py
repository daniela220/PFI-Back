from ...database import DatabaseConnection
from .user_role_model import UserRoleModel
from .user_status_model import UserStatusModel
from PIL import Image
from io import BytesIO

class User:

    def __init__(self, **kwargs):
        self.usuario_id = kwargs.get('usuario_id')
        self.nombre_usuario = kwargs.get('nombre_usuario')
        self.contrasenia = kwargs.get('contrasenia')
        self.imagen = kwargs.get('imagen')
        #self.imagen = Image.open(BytesIO('imagen'))
        self.status_id = kwargs.get('status_id')
        self.role_id = kwargs.get('role_id')
    
    def serialize(self):
        return {
            "usuario_id": self.usuario_id,
            "nombre_usuario": self.nombre_usuario,
            "contrasenia": self.contrasenia,
            "imagen": self.imagen,
            "status": UserStatusModel.get(UserStatusModel(status_id = self.status_id)),
            "role": UserRoleModel.get(UserRoleModel(role_id = self.role_id))
        }

    @classmethod
    def is_registered(cls, user):
        query = """SELECT usuario_id FROM usuarios 
        WHERE nombre_usuario = %(nombre_usuario)s and contrasenia = %(contrasenia)s"""
        params = user.__dict__
        print("-------------------------------------",query, "      ", params, "-------------------------------------")
        result = DatabaseConnection.fetch_one(query, params=params)
        if result is not None:
            return True
        return False
    
    @classmethod
    def get(cls, user):
        query = """SELECT * FROM usuarios 
        WHERE nombre_usuario = %(nombre_usuario)s"""
        params = user.__dict__
        result = DatabaseConnection.fetch_one(query, params=params)
        if result is not None:
            return cls(
                usuario_id = result[0],
                nombre_usuario = result[1],
                contrasenia = result[2],
                imagen = result[3],
                status_id = result[4],
                role_id = result[5]
            )
        return None