import mysql.connector
from models.Postagem import Postagem
from database.ConfigDB import connectar

class PostagemDAO():

    def inserirPostagem(postagem: Postagem):
        idPostagem = 0
        # Script de Inserção.
        query = "INSERT INTO tb_postagem(usuario_id, mensagem, privacidade, dataHora, curtidas) " \
                "VALUES(%s, %s, %s, %s, %s)"
        # Valores.
        values = (postagem.usuario.id, postagem.mensagem, postagem.privacidade, postagem.data_Hora, postagem.curtidas )

        try:
            # Conexão com a base de dados.
            conn = connectar()
            # Preparando o cursor para a execução da consulta.
            cursor = conn.cursor()
            cursor.execute(query, values)

            if cursor.lastrowid:
                idPostagem = cursor.lastrowid
            # Finalizando a persistência dos dados.
            conn.commit()
        except mysql.connector.Error as error:
            print(error)
        finally:
            cursor.close()
            conn.close()
        # Retornar id da rede social.
        return idPostagem

    def deletar(id):
        conn = connectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tb_postagem WHERE id = ?", (id,))
        conn.commit()
        conn.close()

    def atualizar(self, id, mensagem, privacidade, dataHora, curtidas):
        conn = connectar()
        cursor = conn.cursor()
        cursor.execute("""
                  UPDATE postagem
                  SET mensagem = ?, privacidade = ?, dataHora = ?, curtidas = ?
                  WHERE id = ?;
              """, (mensagem, privacidade, dataHora, curtidas, id))
        conn.commit()
        conn.close

    def listar(self):
        postagens = []
        conn = connectar()
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
