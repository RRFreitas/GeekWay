import sqlite3
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
    def __init__(self, criador, dataCriacao, descricao, participantes):
        self.criador = criador
        self.dataCriacao = dataCriacao
        self.descricao = descricao
        self.participantes = participantes

    def inserir(self):
        conn = sqlite3.connect('redesocial.db')
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tb_grupo (criador, data_criacao, descricao)
            VALUES (?,?,?)
            """, (self.criador, self.dataCriacao, self.descricao))

        conn.commit()
        conn.close()

    def listar(self):
        grupos = []
        conn = sqlite3.connect('redesocial.db')
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM tb_grupo;
        """)
        for linha in cursor.fetchall():
            criador = linha[1]
            dataCriacao = linha[2]
            descricao  = linha[3]

            grupo = Grupo(criador, dataCriacao, descricao)
            grupos.append(grupo)

        conn.close()

        return grupos

    def deletar(self, id):
        conn = sqlite3.connect('redesocial.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tb_grupo WHERE id = ?", (id,))
        conn.commit()
        conn.close()

    def atualizar(self, criador, dataCriacao, descricao):
        conn = sqlite3.connect('redesocial.db')
        cursor = conn.cursor()
        cursor.execute("""
                          UPDATE tb_grupo
                          SET criador = ?, dataCriacao = ?, descricao = ?
                          WHERE id = ?;
                      """, (criador, dataCriacao, descricao, id))
        conn.commit()
        conn.close