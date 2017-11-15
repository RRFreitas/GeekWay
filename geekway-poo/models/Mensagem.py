import sqlite3
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

    def inserir(self):
        conn = sqlite3.connect('redesocial.db')
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tb_mensagem (remetente_id, destinatario_id, mensagem, data_hora, visualizada)
            VALUES (?,?,?,?,?)
            """, (self.remetente.id, self.destinatario.id, self.mensagem, self.dataHora, self.visualizada))

        conn.commit()
        conn.close()

    def listar(self):
        mensagens = []
        conn = sqlite3.connect('redesocial.db')
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM tb_mensagem;
        """)
        for linha in cursor.fetchall():
            mensagem = linha[1]
            dataHora = linha[2]
            visualizada = linha[3]

            mensagem = Mensagem(mensagem, dataHora, visualizada)
            mensagens.append(mensagem)

        conn.close()

        return mensagens

    def deletar(self, id):
        conn = sqlite3.connect('redesocial.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tb_mensagem WHERE id = ?", (id,))
        conn.commit()
        conn.close()

    def atualizar(self, id, mensagem, dataHora, visualizada):
        conn = sqlite3.connect('redesocial.db')
        cursor = conn.cursor()
        cursor.execute("""
                          UPDATE tb_mensagem
                          SET mensagem = ?, dataHora = ?, visualizada = ?
                          WHERE id = ?;
                      """, (mensagem, dataHora, visualizada, id))
        conn.commit()
        conn.close