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

    #Verifica se a senha informada está correta.
    def verificar_senha(self, password):
        if password == self.senha:
            return True
        else:
            return False