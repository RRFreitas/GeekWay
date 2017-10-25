import sqlite3

conn = sqlite3.connect('social_academy.db')
cursor = conn.cursor()



def inserirUsuario():
    nome = input('Nome: ')
    email = input('E-mail: ')
    senha = input('Senha: ')
    data_nasc = input('Data de nacimento: ')
    profissao = input('Profissão: ')
    genero = input('Gênero: ')
    cidade= input('Cidade: ')
    estado = input('Estado: ')
    pais = input('pais: ')


    cursor.execute("""
    INSERT INTO tb_usuario (nome, email, senha, data_nasc, profissao, genero, cidade, estado, pais)
    VALUES (?,?,?,?,?,?,?,?,?)
    """, (nome, email, senha, data_nasc, profissao, genero, cidade, estado, pais))

    conn.commit()

    print('Dados inseridos com sucesso!')

def listarUsuario():
    cursor.execute("""
        SELECT * FROM tb_usuario;
    """)

    for linha in cursor.fetchall():
        print(linha)

#inserirUsuario()
listarUsuario()

conn.close()
