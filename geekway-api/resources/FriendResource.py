from flask_restful import Resource, marshal_with
from flask import request
from models.Usuario import Usuario, usuario_campos

class FriendResource(Resource):

    # GET /friends/<id>
    @marshal_with(usuario_campos)
    def get(self, id):
        user = Usuario.findUserById(id)

        if(user is None):
            if(Usuario.findUserById(Usuario.verify_auth_token(id)) is None):
                return 404

        return user.listarAmigos()