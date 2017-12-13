from flask_restful import fields

postagem_campos = {
    'id': fields.Integer,
    'usuario_id': fields.Integer(attribute="usuario.id"),
    'mensagem': fields.String,
    'privacidade': fields.String,
    'dataHora': fields.DateTime,
    'curtidas': fields.Integer
}

'''
    Classe Postagem.
'''
class Postagem():
    def __init__(self, usuario, mensagem, privacidade, dataHora, curtidas, id=0):
        self.usuario = usuario
        self.mensagem = mensagem
        self.privacidade = privacidade
        self.dataHora = dataHora
        self.curtidas = curtidas
        self.id = id
