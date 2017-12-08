from models.Comentario import Comentario
from database.DAO import DAO
from database.UsuarioDAO import UsuarioDAO
from database.PostagemDAO import PostagemDAO

class ComentarioDAO(DAO):

    def __init__(self):
        super(ComentarioDAO, self).__init__()

    def insert(self, comentario: Comentario):
        # Script de Inserção.
        query = "INSERT INTO tb_comentario_postagem(usuario_id, postagem_id, mensagem_id, data_hora, curtidas) " \
                "VALUES(%s, %s, %s, %s, %s)"
        # Valores.
        values = (comentario.usuario.id, comentario.postagem.id, comentario.mensagem.id, comentario.dataHora, comentario.curtidas)

        try:
            return super(ComentarioDAO, self).insert(query, values)
        except Exception as err:
            print("Erro no banco de dados!")
            print(err)
            return

    def delete(self, id):
        query = "DELETE FROM tb_comentario_postagem WHERE id = %s"
        values = (id,)

        try:
            self.execute(query, values)
            return True
        except Exception as err:
            print(err)
            return False

    def update(self, id, mensagem, dataHora, curtidas):
        query = "UPDATE tb_comentario_postagem " \
                "SET mensagem = %s, data_hora = %s, curtidas = %s" \
                "WHERE id = %s;"
        values = (mensagem, dataHora, curtidas, id)

        try:
            self.execute(query, values)
            return True
        except Exception as err:
            print(err)
            return False

    def listar(self):
        query = "SELECT * FROM tb_comentario_postagem;"
        result = self.get_rows(query)

        usuarioDAO = UsuarioDAO()
        postagemDAO = PostagemDAO()

        comentarios = []

        for row in result():
            usuario = usuarioDAO.procurarUsuarioPorId(row[1])
            postagem = postagemDAO.procurarPostagemPorId(row[0])
            mensagem = row[2]
            dataHora = row[3]
            curtidas = row[4]

            comentario = Comentario(usuario, postagem, mensagem, dataHora, curtidas)
            comentarios.append(comentario)

        return comentarios
