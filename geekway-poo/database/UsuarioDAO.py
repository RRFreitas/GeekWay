import mysql.connector
from models.Usuario import Usuario
from database.ConfigDB import connectar
import psycopg2

class UsuarioDAO():

    def inserirUsuario(self, usuario: Usuario):
        idUsuario = 0
        # Script de Inserção.
        query = "INSERT INTO tb_usuario(nome, email, senha, data_nasc, profissao, genero, cidade, estado, pais) " \
                "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        # Valores.
        values = (usuario.nome, usuario.email, usuario.senha, usuario.data_nasc, usuario.profissao, usuario.genero, usuario.cidade, usuario.estado, usuario.pais)

        try:
            # Conexão com a base de dados.
            conn = connectar()
            # Preparando o cursor para a execução da consulta.
            cursor = conn.cursor()
            cursor.execute(query, values)

            if cursor.lastrowid:
                idUsuario = cursor.lastrowid
            # Finalizando a persistência dos dados.
            conn.commit()
        except mysql.connector.Error as error:
            print(error)
        finally:
            cursor.close()
            conn.close()
        # Retornar id da rede social.
        return idUsuario

    def deletarUsuario(self, id):
        conn = connectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tb_usuario WHERE id = ?", (id,))
        conn.commit()
        conn.close()

    def atualizarUsuario(self, id, nome, email, senha, data_nasc, profissao, genero, cidade, estado, pais):
        conn = connectar()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE tb_usuario
            SET nome = ?, email = ?, senha = ?, data_nasc = ?, profissao = ?, genero = ?, cidade = ?, estado = ?, pais = ?
            WHERE id = ?;
        """, (nome, email, senha, data_nasc, profissao, genero, cidade, estado, pais, id))
        conn.commit()
        conn.close

    def listarUsuarios(self):
        usuarios = []
        conn = connectar()
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

    def aceitarAmizade(self, idSolicitante, idSolicitado):
        conn = connectar()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE tb_solicitacao_amizade
            SET status = %s WHERE solicitante_id = %s and solicitado_id = %s;
        """, ("ACEITA", idSolicitante, idSolicitado))

        cursor.execute("""
            INSERT INTO tb_amizade(usuario1_id, usuario2_id)
            VALUES(%s,%s);
        """, (idSolicitante, idSolicitado))

        conn.commit()
        conn.close()

    def negarAmizade(self, idSolicitante, idSolicitado):
        conn = connectar()
        cursor = conn.cursor()
        cursor.execute("""
            DELETE FROM tb_solicitacao_amizade
            WHERE solicitante_id = %s and solicitado_id = %s;
        """, (idSolicitante, idSolicitado))

        conn.commit()
        conn.close()

    def solicitacaoAmizade(self, idSolicitante, idSolicitado):
        conn = connectar()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT status FROM tb_solicitacao_amizade WHERE (solicitante_id = %s and solicitado_id = %s) or (solicitado_id = %s and solicitante_id = %s)
        """, (idSolicitante, idSolicitado, idSolicitante, idSolicitado))

        solicitacao = cursor.fetchone()

        if(not(solicitacao is None) and len(solicitacao) > 0):
            if(solicitacao[0] == "PENDENTE"):
                conn.close()
                return False

        cursor.execute("""
            INSERT INTO tb_solicitacao_amizade (solicitante_id, solicitado_id, status)
            VALUES(%s,%s,%s)
        """, (idSolicitante, idSolicitado, "PENDENTE"))

        conn.commit()
        conn.close()
        return True

    def listarAmigos(self, id):
        conn = connectar()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT usuario1_id, usuario2_id FROM tb_amizade WHERE usuario1_id = %s or usuario2_id = %s
        """, (id, id))

        idAmigos = []

        for users in cursor.fetchall():
            if(users[0] == id):
                idAmigos.append(users[1])
            else:
                idAmigos.append(users[0])

        amigos = []

        for ida in idAmigos:
            amigos.append(self.procurarUsuarioPorId(ida))

        conn.close()

        return amigos

    def listarSolicitacoes(self, id):
        conn = connectar()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM tb_solicitacao_amizade WHERE solicitado_id = %s
        """, (id,))

        solicitacoes = cursor.fetchall()

        conn.close()

        return solicitacoes

    def enviarMensagem(self, idRemetente, idDestinatario, mensagem):
        conn = connectar()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tb_mensagem_direta (remetente_id, destinatario_id, mensagem)
            VALUES (%s,%s,%s)
        """, (idRemetente, idDestinatario, mensagem))
        conn.commit()
        conn.close()

    def listarMensagens(self, id):
        conn = connectar()
        cursor = conn.cursor()
        cursor.execute("""
                    SELECT * FROM tb_mensagem_direta WHERE remetente_id = %s or destinatario_id = %s ORDER BY id
                """, (id, id))

        mensagens = cursor.fetchall()

        conn.close()
        return mensagens

    def isFriend(self, id, idFriend):
        friendList = self.listarAmigos(id)

        for user in friendList:
            if (user.id == idFriend):
                return True

        return False

    def procurarUsuariosPorNome(self, nome):
        users = self.listarUsuarios()
        users2 = []

        for user in users:
            if user.nome == nome:
                users2.append(user)

        return users2

    def procurarUsuarioPorId(self, id):
        users = self.listarUsuarios()
        for user in users:
            if user.id == id:
                return user
        return None

    def procurarUsuarioPorEmail(self, email):
        users = self.listarUsuarios()
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
        conn = connectar()
        cursor = conn.cursor()

        cursor.execute("""
               SELECT email FROM tb_usuario WHERE email = %s
           """, (email,))

        if (cursor.fetchone() is None):
            conn.close()
            return False
        else:
            conn.close()
            return True