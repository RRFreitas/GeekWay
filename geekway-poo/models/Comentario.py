import sqlite3
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

    def inserir(self):
        conn = sqlite3.connect('redesocial.db')
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tb_comentario (mensagem, data_hora, curtidas)
            VALUES (?,?,?)
            """, (self.mensagem, self.dataHora, self.curtidas))

        conn.commit()
        conn.close()

    def listar(self):
        comentarios = []
        conn = sqlite3.connect('redesocial.db')
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM tb_comentario;
        """)
        for linha in cursor.fetchall():
            mensagem = linha[1]
            dataHora = linha[2]
            curtidas = linha[3]

            comentario = Comentario(mensagem, dataHora, curtidas)
            comentarios.append(comentario)

        conn.close()

        return comentarios

    def deletar(self, id):
        conn = sqlite3.connect('redesocial.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tb_comentario WHERE id = ?", (id,))
        conn.commit()
        conn.close()

    def atualizar(self, mensagem, dataHora, curtidas):
        conn = sqlite3.connect('redesocial.db')
        cursor = conn.cursor()
        cursor.execute("""
                          UPDATE tb_comentario
                          SET mensagem = ?, dataHora = ?, curtidas = ?
                          WHERE id = ?;
                      """, (mensagem, dataHora, curtidas, id))
        conn.commit()
        conn.close