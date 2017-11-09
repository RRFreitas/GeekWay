import sqlite3

class Usuario():
    def __init__(self, nome, email, senha, data_nasc, profissao, genero, cidade, estado, pais, amigos):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.data_nasc = data_nasc
        self.profissao = profissao
        self.genero = genero
        self.cidade = cidade
        self.estado = estado
        self.pais = pais
        self.amigos = amigos

    def inserir(self):
        conn = sqlite3.connect('redesocial.db')
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tb_usuario (nome, email, senha, data_nasc, profissao, genero, cidade, estado, pais)
            VALUES (?,?,?,?,?,?,?,?,?)
            """, (self.nome, self.email, self.senha, self.data_nasc, self.profissao, self.genero, self.cidade, self.estado, self.pais))

        conn.commit()
        conn.close()

    def listar(self):
        usuarios = []
        conn = sqlite3.connect('redesocial.db')
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM tb_usuario;
        """)
        for linha in cursor.fetchall():
            nome = linha[1]
            email = linha[2]
            senha = linha[3]
            data_nasc = linha[4]
            profissao = linha[5]
            genero = linha[6]
            cidade = linha[7]
            estado = linha[8]
            pais = linha[9]

            usuario = Usuario(nome, email, senha, data_nasc, profissao, genero, cidade, estado, pais, [])
            usuarios.append(usuario)

        conn.close()

        return usuarios

    def deletar(self, id):
        conn = sqlite3.connect('redesocial.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tb_usuario WHERE id = ?", (id,))
        conn.commit()
        conn.close()

    def atualizar(self, id, nome, email, senha, data_nasc, profissao, genero, cidade, estado, pais):
        conn = sqlite3.connect('redesocial.db')
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE tb_usuario
            SET nome = ?, email = ?, senha = ?, data_nasc = ?, profissao = ?, genero = ?, cidade = ?, estado = ?, pais = ?
            WHERE id = ?;
        """, (nome, email, senha, data_nasc, profissao, genero, cidade, estado, pais, id))
        conn.commit()
        conn.close