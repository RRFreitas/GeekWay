from flask_restful import Resource, marshal_with
from flask import request
from models.Usuario import Usuario, usuario_campos
from database.UsuarioDAO import UsuarioDAO

class UserResource(Resource):

    # GET /user/<id>
    @marshal_with(usuario_campos)
    def get(self, id):
        user = UsuarioDAO().procurarUsuarioPorId(id)

        if(user is None):
            user = Usuario.verify_auth_token(id)
            if(user is None):
                return "Usuário não encontrado.", 404

        return user, 200