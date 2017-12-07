import mysql.connector
from models.Grupo import Grupo
from database.ConfigDB import connectar

class GrupoDAO():

    def inserirGrupo(grupo: Grupo):
        idGrupo= 0
        # Script de Inserção.
        query = "INSERT INTO tb_grupo(criador_id, data_criacao, descricao) " \
                "VALUES(%s, %s, %s)"
        # Valores.
        values = (grupo.criador.id, grupo.dataCriacao, grupo.descricao)

        try:
            # Conexão com a base de dados.
            conn = connectar()
            # Preparando o cursor para a execução da consulta.
            cursor = conn.cursor()
            cursor.execute(query, values)

            if cursor.lastrowid:
                idGrupo = cursor.lastrowid
            # Finalizando a persistência dos dados.
            conn.commit()
        except mysql.connector.Error as error:
            print(error)
        finally:
            cursor.close()
            conn.close()
        # Retornar id da rede social.
        return idGrupo

    def deletar(self, id):
        conn = connectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tb_grupo WHERE id = ?", (id,))
        conn.commit()
        conn.close()

    def atualizar(self, criador, dataCriacao, descricao):
        conn = connectar()
        cursor = conn.cursor()
        cursor.execute("""
                          UPDATE tb_grupo
                          SET criador = ?, dataCriacao = ?, descricao = ?
                          WHERE id = ?;
                      """, (criador, dataCriacao, descricao, id))
        conn.commit()
        conn.close

    def listar(self):
        grupos = []
        conn = connectar()
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
