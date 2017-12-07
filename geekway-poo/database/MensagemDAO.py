import mysql.connector
from models.Mensagem import Mensagem
from database.ConfigDB import connectar

class MensagemDAO():

    def inserirMensagem(mensagem: Mensagem):
        idMensagem = 0
        # Script de Inserção.
        query = "INSERT INTO tb_mensagem_direta(remetente_id, destinatario_id, mensagem, dataHora, visualizada) " \
                "VALUES(%s, %s, %s, %s, %s)"
        # Valores.
        values = (mensagem.remetente.id, mensagem.destinatario.id, mensagem.mensagem, mensagem.dataHora, mensagem.visualizada)

        try:
            # Conexão com a base de dados.
            conn = connectar()
            # Preparando o cursor para a execução da consulta.
            cursor = conn.cursor()
            cursor.execute(query, values)

            if cursor.lastrowid:
                idMensagem = cursor.lastrowid
            # Finalizando a persistência dos dados.
            conn.commit()
        except mysql.connector.Error as error:
            print(error)
        finally:
            cursor.close()
            conn.close()
        # Retornar id da rede social.
        return idMensagem

    def deletar(self, id):
        conn = connectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tb_mensagem WHERE id = ?", (id,))
        conn.commit()
        conn.close()

    def atualizar(self, id, mensagem, dataHora, visualizada):
        conn = connectar()
        cursor = conn.cursor()
        cursor.execute("""
                          UPDATE tb_mensagem
                          SET mensagem = ?, dataHora = ?, visualizada = ?
                          WHERE id = ?;
                      """, (mensagem, dataHora, visualizada, id))
        conn.commit()
        conn.close

    def listar(self):
        mensagens = []
        conn = connectar()
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
