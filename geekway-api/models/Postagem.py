import sqlite3
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

    def inserir(self):
        conn = sqlite3.connect('redesocial.db')
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tb_postagem (usuario_id, mensagem, privacidade, data_hora, curtidas)
            VALUES (?,?,?,?,?)
            """, (self.usuario.id, self.mensagem, self.privacidade, self.dataHora, self.curtidas))

        conn.commit()
        conn.close()

    def listar(self):
        postagens = []
        conn = sqlite3.connect('redesocial.db')
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM tb_postagem;
        """)
        for linha in cursor.fetchall():
            mensagem = linha[1]
            privacidade = linha[2]
            dataHora = linha[3]
            curtidas = linha[4]

            postagem = Postagem(mensagem, privacidade, dataHora, curtidas)
            postagens.append(postagem)

        conn.close()

        return postagens

    def deletar(self, id):
        conn = sqlite3.connect('redesocial.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tb_postagem WHERE id = ?", (id,))
        conn.commit()
        conn.close()

    def atualizar(self, id, mensagem, privacidade, dataHora, curtidas):
        conn = sqlite3.connect('redesocial.db')
        cursor = conn.cursor()
        cursor.execute("""
                  UPDATE postagem
                  SET mensagem = ?, privacidade = ?, dataHora = ?, curtidas = ?
                  WHERE id = ?;
              """, (mensagem, privacidade, dataHora, curtidas, id))
        conn.commit()
        conn.close