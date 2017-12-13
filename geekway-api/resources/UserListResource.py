from flask_restful import Resource, marshal_with
from flask import request
from models.Usuario import Usuario, usuario_campos
from database.UsuarioDAO import UsuarioDAO
from datetime import datetime

class UserListResource(Resource):

    # GET /users
    @marshal_with(usuario_campos)
    def get(self):
        return UsuarioDAO().listar()

    # POST /users
    def post(self):
        usuarioJson = request.json

        if(not UsuarioDAO().procurarUsuarioPorEmail(usuarioJson["email"]) is None):
            return "E-mail já existe", 409

        usuarioObj = Usuario(usuarioJson["nome"], usuarioJson["email"], usuarioJson["senha"], usuarioJson["data_nasc"], "", usuarioJson["genero"], "", "", "")
        usuarioObj.generate_auth_token()

        UsuarioDAO().insert(usuarioObj)

        return usuarioObj.token, 200