import sqlite3
import datetime

conn = sqlite3.connect('social_academy.db')
cursor = conn.cursor()

def inserirMensagem():
    remetente_id = int(input('ID do Remetente: '))
    destinatario_id = int(input('ID do Destinatário: '))
    mensagem = input('Mensagem: ')
    data_hora = str(datetime.datetime.now().time())
    visualizada = False

    cursor.execute("""
    INSERT INTO tb_mensagem_direta (remetente_id, destinatario_id, mensagem, data_hora, visualizada)
    VALUES (?,?,?,?,?)
    """, (remetente_id, destinatario_id, mensagem, data_hora, visualizada))

    conn.commit()

    print('Dados inseridos com sucesso!')

def listarMensagens():
    cursor.execute("""
        SELECT * FROM tb_mensagem_direta;
    """)

    for linha in cursor.fetchall():
        print(linha)

inserirMensagem()
listarMensagens()

conn.close()
