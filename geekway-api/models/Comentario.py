from flask_restful import fields

comentario_campos = {
    'usuario_id': fields.Integer(attribute="usuario.id"),
    'postagem_id': fields.Integer(attribute="postagem.id"),
    'mensagem': fields.String,
    'dataHora': fields.DateTime,
    'curtidas': fields.Integer
}

'''
    Classe Comentario.
'''

class Comentario():
    def __init__(self, usuario, postagem, mensagem, dataHora, curtidas):
        self.usuario = usuario
        self.postagem = postagem
        self.mensagem = mensagem
        self.dataHora = dataHora
        self.curtidas = curtidas
