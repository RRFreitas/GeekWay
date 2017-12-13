'''
    Classe Mensagem.
'''
class Mensagem():
    def __init__(self, remetente, destinatario, mensagem, dataHora, visualizada):
        self.remetente = remetente
        self.destinatario = destinatario
        self.mensagem = mensagem
        self.dataHora = dataHora
        self.visualizada = visualizada
