import sqlite3

'''
    Classe Usuario.
'''

class Usuario():
    def __init__(self, nome, email, senha, data_nasc=None, profissao=None, genero=None, cidade=None, estado=None, pais=None, amigos=None, id=None):
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
        self.id = id

    def inserir(self):
        conn = sqlite3.connect('redesocial.db')
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tb_usuario (nome, email, senha, data_nasc, profissao, genero, cidade, estado, pais)
            VALUES (?,?,?,?,?,?,?,?,?)
            """, (self.nome, self.email, self.senha, self.data_nasc, self.profissao, self.genero, self.cidade, self.estado, self.pais))

        conn.commit()
        conn.close()

    #Lista todos os usuários
    @staticmethod
    def listar():
        usuarios = []
        conn = sqlite3.connect('redesocial.db')
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM tb_usuario;
        """)
        for linha in cursor.fetchall():
            id = linha[0]
            nome = linha[1]
            email = linha[2]
            senha = linha[3]
            data_nasc = linha[4]
            profissao = linha[5]
            genero = linha[6]
            cidade = linha[7]
            estado = linha[8]
            pais = linha[9]

            usuario = Usuario(nome, email, senha, data_nasc, profissao, genero, cidade, estado, pais, [], id)
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

    #Verifica se a senha informada está correta.
    def verificar_senha(self, password):
        if password == self.senha:
            return True
        else:
            return False

    #Aceita solicitação de amizade e registra no banco.
    def aceitarAmizade(self, id):
        conn = sqlite3.connect("redesocial.db")
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE tb_solicitacao_amizade
            SET status = ? WHERE solicitante_id = ? and solicitado_id = ?;
        """, ("ACEITA", id, self.id))

        cursor.execute("""
            INSERT INTO tb_amizade(usuario1_id, usuario2_id)
            VALUES(?,?);
        """, (id, self.id))

        conn.commit()
        conn.close()

    #Envia solicitação de amizade para um usuário, registrando no banco.
    def solicitacaoAmizade(self, id):
        conn = sqlite3.connect('redesocial.db')
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tb_solicitacao_amizade (solicitante_id, solicitado_id, status)
            VALUES(?,?,?)
        """, (self.id, id, "PENDENTE"))

        conn.commit()
        conn.close()

    #Lista toos os amigos
    def listarAmigos(self):
        conn = sqlite3.connect('redesocial.db')
        cursor = conn.cursor()
        cursor.execute("""
            SELECT usuario1_id, usuario2_id FROM tb_amizade WHERE usuario1_id = ? or usuario2_id = ?
        """, (self.id, self.id))

        idAmigos = []

        for users in cursor.fetchall():
            if(users[0] == self.id):
                idAmigos.append(users[1])
            else:
                idAmigos.append(users[0])

        amigos = []

        for id in idAmigos:
            amigos.append(Usuario.findUserById(id))

        return amigos

    #Lista todas as solicitações, estando pendente ou não.
    def listarSolicitacoes(self):
        conn = sqlite3.connect('redesocial.db')
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM tb_solicitacao_amizade WHERE solicitado_id = ?
        """, (self.id,))

        return cursor.fetchall()

    #Envia mensagem para um usuário, registrando no banco.
    def enviarMensagem(self, id, mensagem):
        conn = sqlite3.connect('redesocial.db')
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tb_mensagem_direta (remetente_id, destinatario_id, mensagem)
            VALUES (?,?,?)
        """, (self.id, id, mensagem))
        conn.commit()
        conn.close()

    #Lista mensagens enviadas e recebidas
    def listarMensagens(self):
        conn = sqlite3.connect('redesocial.db')
        cursor = conn.cursor()
        cursor.execute("""
                    SELECT * FROM tb_mensagem_direta WHERE remetente_id = ? or destinatario_id = ? ORDER BY id
                """, (self.id, self.id))

        return cursor.fetchall()

    #Verifica se um determinado usuário com id passado por parâmetro é amigo
    def isFriend(self, id):
        friendList = self.listarAmigos()

        for user in friendList:
            if(user.id == id):
                return True

        return False

    #Encontra lista de usuários que possuem determinado nome passado por parâmetro.
    @staticmethod
    def findUsersByName(nome):
        users = Usuario.listar()
        users2 = []

        for user in users:
            if user.nome == nome:
                users2.append(user)

        return users2

    #Encontra usuário que possui id passado por parâmtro
    @staticmethod
    def findUserById(id):
        users = Usuario.listar()
        for user in users:
            if user.id == id:
                return user
        return None

    #Encontra usuário que possui email passado por parâmetro
    @staticmethod
    def findUserByEmail(email):
        users = Usuario.listar()
        for user in users:
            if user.email == email:
                return user
        return None

    #Verifica email e senha
    @staticmethod
    def verificar_login(login, password):
        user = Usuario.findUserByEmail(login)

        if(user is None):
            return False
        if(user.verificar_senha(password)):
            return True
        return False

    #Verifica se determinado email passado por parâmetro é de algum usuário.
    @staticmethod
    def emailExists(email):
        conn = sqlite3.connect("redesocial.db")
        cursor = conn.cursor()

        cursor.execute("""
            SELECT email FROM tb_usuario WHERE email = ?
        """, (email,))

        if(cursor.fetchone() is None):
            return False
        else:
            return True