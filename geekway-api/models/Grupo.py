from flask_restful import fields
from models.Usuario import usuario_campos

grupo_campos = {
    'criador_id': fields.Integer(attribute="criador.id"),
    'dataCriacao': fields.DateTime,
    'descricao': fields.String,
    'participantes': fields.List(fields.Nested(usuario_campos))
}

'''
    Classe Grupo.
'''
class Grupo():
    def __init__(self, criador, nome, dataCriacao, descricao):
        self.criador = criador
        self.nome = nome
        self.dataCriacao = dataCriacao
        self.descricao = descricao