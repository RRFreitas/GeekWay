import sqlite3

class Grupo():
    def __init__(self, criador, dataCriacao, descricao):
        self.criador = criador
        self.dataCriacao = dataCriacao
        self.descricao = descricao

    def inserir(self):
        conn = sqlite3.connect('redesocial.db')
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tb_grupo (criador, dataCriacao, descricao)
            VALUES (?,?,?)
            """, (self.criador, self.dataCriacao, self.descricao))

        conn.commit()
        conn.close()

    def listar(self):
        grupos = []
        conn = sqlite3.connect('redesocial.db')
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

    def deletar(self, id):
        conn = sqlite3.connect('redesocial.db')
        cursor = conn.cursor()
        cursor.execute("""
        DELETE FROM tb_grupo WHERE 'id' = id;
        """)
        conn.commit()
        conn.close()

    def atualizar(self, criador, dataCriacao, descricao):
        pass