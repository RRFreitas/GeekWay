'''
    Classe Postagem.
'''
class Postagem():
    def __init__(self, usuario, mensagem, privacidade, dataHora, curtidas, id=0):
        self.usuario = usuario
        self.mensagem = mensagem
        self.privacidade = privacidade
        self.dataHora = dataHora
        self.curtidas = curtidas
        self.id = id
