from flask_restful import Resource, marshal_with
from flask import request
from models.Usuario import Usuario, usuario_campos

class LoginResource(Resource):

    # POST /login
    def post(self):
        dados = request.json
        try:
            usuario = Usuario.findUserByEmail(dados['email'])
            if usuario is None:
                return "Usuário não encontrado.", 404
            else:
                if usuario.verificar_senha(dados['senha']) == False:
                    return "Senha incorreta.", 404
                else:
                    usuario.generate_auth_token()

        except:
            return "", 500

        return usuario.token, 200