import sqlite3
import datetime

conn = sqlite3.connect('social_academy.db')
cursor = conn.cursor()

def inserirGrupo():
    id_criador = input('ID do usuário criador: ')
    nome = input('Nome: ')
    data_criacao = str(datetime.datetime.now().time())
    descricao = input('Descrição: ')

    cursor.execute("""
    INSERT INTO tb_grupo (id_criador, nome, data_criacao, descricao)
    VALUES (?,?,?,?)
    """, (id_criador, nome, data_criacao, descricao))

    conn.commit()

    print('Dados inseridos com sucesso!')

def listarGrupos():
    cursor.execute("""
        SELECT * FROM tb_grupo;
    """)

    for linha in cursor.fetchall():
        print(linha)

inserirGrupo()
listarGrupos()

conn.close()
