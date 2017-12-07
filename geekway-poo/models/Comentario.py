'''
    Classe Comentario.
'''

class Comentario():
    def __init__(self, usuario, postagem, mensagem, dataHora, curtidas):
        self.usuario = usuario
        self.postagem = postagem
        self.mensagem = mensagem
        self.dataHora = dataHora
        self.curtidas = curtidas
