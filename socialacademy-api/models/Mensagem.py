import sqlite3

class Mensagem():
    def __init__(self, mensagem, dataHora, visualizada):
        self.mensagem = mensagem
        self.dataHora = dataHora
        self.visualizada = visualizada

    def inserir(self):
        conn = sqlite3.connect('redesocial.db')
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tb_mensagem (mensagem, dataHora, visualizada)
            VALUES (?,?,?)
            """, (self.mensagem, self.dataHora, self.visualizada))

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
        cursor.execute("""
        DELETE FROM tb_mensagem WHERE 'id' = id;
        """)
        conn.commit()
        conn.close()

    def atualizar(self, nmensagem, dataHora, vizualizada):
        pass