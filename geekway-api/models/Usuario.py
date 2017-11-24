import sqlite3
from flask_restful import fields
import base64
from itsdangerous import (TimedJSONWebSignatureSerializer
as Serializer, BadSignature, SignatureExpired)

usuario_campos = {
    'id': fields.Integer,
    'nome': fields.String,
    'email': fields.String,
    'data_nasc': fields.String,
    'profissao': fields.String,
    'genero': fields.String,
    'cidade': fields.String,
    'estado': fields.String,
    'pais': fields.String
}

'''
    Classe Usuario.
'''

class Usuario():
    def __init__(self, nome, email, senha, data_nasc, profissao, genero, cidade, estado, pais, amigos, id=None, token=None):
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
        self.token = token

    def inserir(self):
        conn = sqlite3.connect('redesocial.db')
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tb_usuario (nome, email, senha, data_nasc, profissao, genero, cidade, estado, pais)
            VALUES (?,?,?,?,?,?,?,?,?)
            """, (self.nome, self.email, self.senha, self.data_nasc, self.profissao, self.genero, self.cidade, self.estado, self.pais))

        conn.commit()
        conn.close()

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

    # Lista todos os amigos
    def listarAmigos(self):
        conn = sqlite3.connect('redesocial.db')
        cursor = conn.cursor()
        cursor.execute("""
            SELECT usuario1_id, usuario2_id FROM tb_amizade WHERE usuario1_id = ? or usuario2_id = ?
        """, (self.id, self.id))

        idAmigos = []

        for users in cursor.fetchall():
            if (users[0] == self.id):
                idAmigos.append(users[1])
            else:
                idAmigos.append(users[0])

        amigos = []

        for id in idAmigos:
            amigos.append(Usuario.findUserById(id))

        return amigos

    @staticmethod
    def findUserById(id):
        users = Usuario.listar()
        for user in users:
            if user.id == id:
                return user
        return None

    @staticmethod
    def findUserByEmail(email):
        users = Usuario.listar()
        for user in users:
            if user.email == email:
                return user
        return None

    def verificar_senha(self, password):
        #pass_hash = base64.b64encode(password.encode('utf-8'))
        #if pass_hash.decode('utf-8') == self.senha:
        if password == self.senha:
            return True
        else:
            return False

    def generate_auth_token(self, expiration=None):
        s = Serializer('123456', expires_in=expiration)
        dumps = s.dumps({'id': self.id})

        self.token = dumps.decode('ascii')

    @staticmethod
    def verify_auth_token(token):
        s = Serializer('123456')
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None  # valid token, but expired
        except BadSignature:
            return None  # invalid token

        user = Usuario.findUserById(data['id'])

        return user