from flask_restful import fields

mensagem_campos = {
    'remetente_id': fields.Integer(attribute="remetente.id"),
    'destinatario_id': fields.Integer(attribute="destinatario.id"),
    'mensagem': fields.String,
    'dataHora': fields.DateTime,
    'visualizada': fields.Boolean
}

'''
    Classe Mensagem.
'''
class Mensagem():
    def __init__(self, remetente, destinatario, mensagem, dataHora, visualizada):
        self.remetente = remetente
        self.destinatario = destinatario
        self.mensagem = mensagem
        self.dataHora = dataHora
        self.visualizada = visualizada
