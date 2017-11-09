import sqlite3

class Postagem():
    def __init__(self, mensagem, privacidade, dataHora, curtidas):
        self.mensagem = mensagem
        self.privacidade = privacidade
        self.dataHora = dataHora
        self.curtidas = curtidas

    def inserir(self):
        conn = sqlite3.connect('redesocial.db')
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tb_postagem (mensagem, privacidade, dataHora, curtidas)
            VALUES (?,?,?,?)
            """, (self.mensagem, self.privacidade, self.dataHora, self.curtidas))

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