import mysql.connector
from models.Comentario import Comentario
from database.ConfigDB import connectar

class ComentarioDAO():

    def inserirComentario(comentario: Comentario):
        idComentario = 0
        # Script de Inserção.
        query = "INSERT INTO tb_comentario(usuario_id, postagem_id, mensagem_id, data_hora, curtidas) " \
                "VALUES(%s, %s, %s, %s, %s)"
        # Valores.
        values = (comentario.usuario.id, comentario.postagem.id, comentario.mensagem.id, comentario.dataHora, comentario.curtidas)

        try:
            # Conexão com a base de dados.
            conn = connectar()
            # Preparando o cursor para a execução da consulta.
            cursor = conn.cursor()
            cursor.execute(query, values)

            if cursor.lastrowid:
                idComentario = cursor.lastrowid
            # Finalizando a persistência dos dados.
            conn.commit()
        except mysql.connector.Error as error:
            print(error)
        finally:
            cursor.close()
            conn.close()
        # Retornar id da rede social.
        return idComentario

    def deletar(self, id):
        conn = connectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tb_comentario WHERE id = ?", (id,))
        conn.commit()
        conn.close()

    def atualizar(self, id, mensagem, dataHora, curtidas):
        conn = connectar()
        cursor = conn.cursor()
        cursor.execute("""
                          UPDATE tb_comentario
                          SET mensagem = ?, dataHora = ?, curtidas = ?
                          WHERE id = ?;
                      """, (mensagem, dataHora, curtidas, id))
        conn.commit()
        conn.close

    def listar(self):
        comentarios = []
        conn = connectar()
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
