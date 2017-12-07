import sqlite3
from flask_restful import fields

'''
    Classe Grupo.
'''
class Grupo():
    def __init__(self, criador, dataCriacao, descricao, participantes):
        self.criador = criador
        self.dataCriacao = dataCriacao
        self.descricao = descricao
        self.participantes = participantes
