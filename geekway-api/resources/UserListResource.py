from flask_restful import Resource, marshal_with
from flask import request
from sqlalchemy import exc
from models.Usuario import Usuario, usuario_campos

class UserListResource(Resource):

    # GET /users
    @marshal_with(usuario_campos)
    def get(self):
        return Usuario.listar()

    # POST /users
    def post(self):
        usuarioJson = request.json

        if(not Usuario.findUserByEmail(usuarioJson["email"]) is None):
            return "E-mail já existe", 409

        usuarioObj = Usuario(usuarioJson["nome"], usuarioJson["email"], usuarioJson["senha"], usuarioJson["data_nasc"], "", usuarioJson["genero"], "", "", "", [])
        usuarioObj.inserir()
        usuarioObj.generate_auth_token()
        return usuarioObj.token, 200