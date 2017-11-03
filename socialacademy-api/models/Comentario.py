import sqlite3

class Comentario():
    def __init__(self, mensagem, dataHora, curtidas):
        self.mensagem = mensagem
        self.dataHora = dataHora
        self.curtidas = curtidas

    def inserir(self):
        conn = sqlite3.connect('redesocial.db')
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tb_comentario (mensagem, dataHora, curtidas)
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
        cursor.execute("""
        DELETE FROM tb_comentario WHERE 'id' = id;
        """)
        conn.commit()
        conn.close()

    def atualizar(self, mensagem, dataHora, curtidas):
        pass