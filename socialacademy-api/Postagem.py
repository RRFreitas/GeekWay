import sqlite3
import datetime

conn = sqlite3.connect('social_academy.db')
cursor = conn.cursor()

def inserirPostagem():
    id_usuario = int(input('ID do Usuário: '))
    mensagem = input('Mensagem: ')
    privacidade = input('Privacidade ')
    data_hora = str(datetime.datetime.now().time())
    curtidas = 0

    cursor.execute("""
    INSERT INTO tb_postagem (usuario_id, mensagem, privacidade, data_hora, curtidas)
    VALUES (?,?,?,?,?)
    """, (id_usuario, mensagem, privacidade, data_hora, curtidas))

    conn.commit()

    print('Dados inseridos com sucesso!')

def listarPostagem():
    cursor.execute("""
        SELECT * FROM tb_postagem;
    """)

    for linha in cursor.fetchall():
        print(linha)

#inserirPostagem()
listarPostagem()

conn.close()
