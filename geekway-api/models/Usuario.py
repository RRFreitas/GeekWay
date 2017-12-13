from flask_restful import fields
import database.UsuarioDAO
from itsdangerous import (TimedJSONWebSignatureSerializer
as Serializer, BadSignature, SignatureExpired)

usuario_campos = {
    'id': fields.Integer,
    'nome': fields.String,
    'email': fields.String,
    'data_nasc': fields.String,
    'profissao': fields.String,
    'genero': fields.String,
    'cidade': fields.String,
    'estado': fields.String,
    'pais': fields.String
}

'''
    Classe Usuario.
'''
class Usuario():
    def __init__(self, nome, email, senha, data_nasc=None, profissao=None, genero=None, cidade=None, estado=None, pais=None, amigos=None, id=None):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.data_nasc = data_nasc
        self.profissao = profissao
        self.genero = genero
        self.cidade = cidade
        self.estado = estado
        self.pais = pais
        self.amigos = amigos
        self.id = id

    #Verifica se a senha informada está correta.
    def verificar_senha(self, password):
        if password == self.senha:
            return True
        else:
            return False

    def generate_auth_token(self, expiration=None):
        s = Serializer('123456', expires_in=expiration)
        dumps = s.dumps({'id': self.id})

        self.token = dumps.decode('ascii')

    @staticmethod
    def verify_auth_token(token):
        s = Serializer('123456')
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None  # valid token, but expired
        except BadSignature:
            return None  # invalid token

        user = database.UsuarioDAO.UsuarioDAO().procurarUsuarioPorId(data['id'])

        return user