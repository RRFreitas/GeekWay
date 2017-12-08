from models.Usuario import Usuario
from database.DAO import DAO

class UsuarioDAO(DAO):

    def __init__(self):
        super(UsuarioDAO, self).__init__()

    def insert(self, usuario: Usuario):
        # Script de Inserção.
        query = "INSERT INTO tb_usuario(nome, email, senha, data_nasc, profissao, genero, cidade, estado, pais) " \
                "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        # Valores.
        values = (usuario.nome, usuario.email, usuario.senha, usuario.data_nasc, usuario.profissao, usuario.genero, usuario.cidade, usuario.estado, usuario.pais)

        try:
            return super(UsuarioDAO, self).insert(query, values)
        except Exception as err:
            print("Erro no banco de dados!")
            print(err)
            return

    def delete(self, id):
        try:
            query = "DELETE FROM tb_usuario WHERE id = %s"
            values = (id,)
            self.execute(query, values)
            return True
        except Exception as err:
            print(err)
            return False

    def update(self, id, nome, email, senha, data_nasc, profissao, genero, cidade, estado, pais):
        try:
            query = "UPDATE tb_usuario " \
                    "SET nome = %s, email = %s, senha = %s, data_nasc = %s, profissao = %s, genero = %s, cidade = %s, estado = %s, pais = %s " \
                    "WHERE id = %s;"
            values = (nome, email, senha, data_nasc, profissao, genero, cidade, estado, pais, id)
            self.execute(query, values)
        except Exception as err:
            print(err)
            return False

    def listar(self):
        query = "SELECT * FROM tb_usuario;"
        results = self.get_rows(query)

        usuarios = []

        for row in results:
            id = row[0]
            nome = row[1]
            email = row[2]
            senha = row[3]
            data_nasc = row[4]
            profissao = row[5]
            genero = row[6]
            cidade = row[7]
            estado = row[8]
            pais = row[9]

            usuario = Usuario(nome, email, senha, data_nasc, profissao, genero, cidade, estado, pais, [], id)
            usuarios.append(usuario)

        return usuarios

    def aceitarAmizade(self, idSolicitante, idSolicitado):
        try:
            query = "UPDATE tb_solicitacao_amizade " \
                    "SET status = %s WHERE solicitante_id = %s and solicitado_id = %s;"
            values = ("ACEITA", idSolicitante, idSolicitado)
            self.execute(query, values)

            query = "INSERT INTO tb_amizade(usuario1_id, usuario2_id) " \
                    "VALUES(%s,%s);"
            values = (idSolicitante, idSolicitado)
            self.execute(query, values)

            return True
        except:
            return False

    def negarAmizade(self, idSolicitante, idSolicitado):
        try:
            query = "DELETE FROM tb_solicitacao_amizade " \
                    "WHERE solicitante_id = %s and solicitado_id = %s;"
            values = (idSolicitante, idSolicitado)
            self.execute(query, values)

            return True
        except:
            return False

    def solicitacaoAmizade(self, idSolicitante, idSolicitado):
        query = "SELECT status FROM tb_solicitacao_amizade WHERE (solicitante_id = %s and solicitado_id = %s) or (solicitado_id = %s and solicitante_id = %s)"
        values = (idSolicitante, idSolicitado, idSolicitante, idSolicitado)

        solicitacao = self.get_row(query, values)

        if(not(solicitacao is None) and len(solicitacao) > 0):
            if(solicitacao[0] == "PENDENTE"):
                return False

        query = "INSERT INTO tb_solicitacao_amizade (solicitante_id, solicitado_id, status) " \
                "VALUES(%s,%s,%s)"
        values = (idSolicitante, idSolicitado, "PENDENTE")
        self.execute(query, values)
        return True

    def listarAmigos(self, id):
        query = "SELECT usuario1_id, usuario2_id FROM tb_amizade WHERE usuario1_id = %s or usuario2_id = %s"
        values = (id, id)
        result = self.get_rows(query, values)

        idAmigos = []

        for user in result:
            if(user[0] == id):
                idAmigos.append(user[1])
            else:
                idAmigos.append(user[0])

        amigos = []

        for ida in idAmigos:
            amigos.append(self.procurarUsuarioPorId(ida))

        return amigos

    def listarSolicitacoes(self, id):
        query = "SELECT * FROM tb_solicitacao_amizade WHERE solicitado_id = %s"
        values = (id,)
        solicitacoes = self.get_rows(query, values)

        return solicitacoes

    def enviarMensagem(self, idRemetente, idDestinatario, mensagem):
        try:
            query = "INSERT INTO tb_mensagem_direta (remetente_id, destinatario_id, mensagem) " \
                    "VALUES (%s,%s,%s)"
            values = (idRemetente, idDestinatario, mensagem)
            self.execute(query, values)

            return True
        except:
            return False

    def listarMensagens(self, id):
        query = "SELECT * FROM tb_mensagem_direta WHERE remetente_id = %s or destinatario_id = %s ORDER BY id"
        values = (id, id)
        mensagens = self.get_rows(query, values)

        return mensagens

    def isFriend(self, id, idFriend):
        friendList = self.listarAmigos(id)

        for user in friendList:
            if (user.id == idFriend):
                return True

        return False

    def procurarUsuariosPorNome(self, nome):
        users = self.listar()
        users2 = []

        for user in users:
            if user.nome == nome:
                users2.append(user)

        return users2

    def procurarUsuarioPorId(self, id):
        users = self.listar()
        for user in users:
            if user.id == id:
                return user
        return None

    def procurarUsuarioPorEmail(self, email):
        users = self.listar()
        for user in users:
            if user.email == email:
                return user
        return None

    def verificar_login(self, login, password):
        user = self.procurarUsuarioPorEmail(login)

        if (user is None):
            return False
        if (user.verificar_senha(password)):
            return True
        return False

    def emailExists(self, email):
        query = "SELECT email FROM tb_usuario WHERE email = %s"
        values = (email,)

        if (self.get_row(query, values) is None):
            return False
        else:
            return True