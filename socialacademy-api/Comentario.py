import sqlite3
import datetime

conn = sqlite3.connect('social_academy.db')
cursor = conn.cursor()

def inserirComentario():
    id_postagem = int(input('ID da postagem: '))
    id_usuario = int(input('ID do Usuário: '))
    mensagem = input('Mensagem: ')
    data_hora = str(datetime.datetime.now().time())
    curtidas = 0

    cursor.execute("""
    INSERT INTO tb_comentario_postagem (postagem_id, usuario_id, mensagem, data_hora, curtidas)
    VALUES (?,?,?,?,?)
    """, (id_postagem, id_usuario, mensagem, data_hora, curtidas))

    conn.commit()

    print('Dados inseridos com sucesso!')

def listarComentarios():
    cursor.execute("""
        SELECT * FROM tb_comentario_postagem;
    """)

    for linha in cursor.fetchall():
        print(linha)

inserirComentario()
listarComentarios()

conn.close()
