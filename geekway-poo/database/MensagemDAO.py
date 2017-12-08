from database.DAO import DAO
from database.UsuarioDAO import UsuarioDAO
from models.Mensagem import Mensagem

class MensagemDAO(DAO):

    def __init__(self):
        super(MensagemDAO, self).__init__()

    def insert(self, mensagem: Mensagem):
        # Script de Inserção.
        query = "INSERT INTO tb_mensagem_direta(remetente_id, destinatario_id, mensagem, data_hora, visualizada) " \
                "VALUES(%s, %s, %s, %s, %s)"
        # Valores.
        values = (mensagem.remetente.id, mensagem.destinatario.id, mensagem.mensagem, mensagem.dataHora, mensagem.visualizada)

        try:
            return super(MensagemDAO, self).insert(query, values)
        except Exception as err:
            print("Erro no banco de dados!")
            print(err)
            return

    def delete(self, id):
        query = "DELETE FROM tb_mensagem_direta WHERE id = %s"
        values = (id,)

        try:
            self.execute(query, values)
            return True
        except Exception as err:
            print(err)
            return False

    def update(self, id, mensagem, dataHora, visualizada):
        query = "UPDATE tb_mensagem_direta " \
                "SET mensagem = %s, data_hora = %s, visualizada = %s " \
                "WHERE id = %s"
        values = (mensagem, dataHora, visualizada, id)

        try:
            self.execute(query, values)
            return True
        except Exception as err:
            print(err)
            return False

    def listar(self):
        query = "SELECT * FROM tb_mensagem_direta;"
        result = self.get_rows(query)

        usuarioDAO = UsuarioDAO()

        mensagens = []

        for row in result:
            remetente = usuarioDAO.procurarUsuarioPorId(row[1])
            destinatario = usuarioDAO.procurarUsuarioPorId(row[2])
            mensagem = row[3]
            dataHora = row[4]
            visualizada = row[5]

            mensagem = Mensagem(remetente, destinatario, mensagem, dataHora, visualizada)
            mensagens.append(mensagem)

        return mensagens
