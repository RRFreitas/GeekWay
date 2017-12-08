from models.Postagem import Postagem
from database.DAO import DAO
from database.UsuarioDAO import UsuarioDAO

class PostagemDAO(DAO):

    def __init__(self):
        super(PostagemDAO, self).__init__()

    def insert(self, postagem: Postagem):
        # Script de Inserção.
        query = "INSERT INTO tb_postagem(usuario_id, mensagem, privacidade, dataHora, curtidas) " \
                "VALUES(%s, %s, %s, %s, %s)"
        # Valores.
        values = (postagem.usuario.id, postagem.mensagem, postagem.privacidade, postagem.data_Hora, postagem.curtidas )

        try:
            return super(PostagemDAO, self).insert(query, values)
        except Exception as err:
            print("Erro no banco de dados!")
            print(err)
            return

    def delete(self, id):
        query = "DELETE FROM tb_postagem WHERE id = %s"
        values = (id,)

        try:
            self.execute(query, values)
            return True
        except Exception as err:
            print(err)
            return False

    def update(self, id, mensagem, privacidade, dataHora, curtidas):
        query = "UPDATE postagem " \
                "SET mensagem = %s, privacidade = %s, dataHora = %s, curtidas = %s" \
                "WHERE id = %s;"
        values = (mensagem, privacidade, dataHora, curtidas, id)

        try:
            self.execute(query, values)
            return True
        except Exception as err:
            print(err)
            return False

    def procurarPostagemPorId(self, id):
        posts = self.listar()
        for post in posts:
            if post.id == id:
                return post
        return None

    def listar(self):
        query = "SELECT * FROM tb_postagem;"
        result = self.get_rows(query)

        usuarioDAO = UsuarioDAO()

        postagens = []

        for row in result:
            usuario = usuarioDAO.procurarUsuarioPorId(row[1])
            mensagem = row[2]
            privacidade = row[3]
            dataHora = row[4]
            curtidas = row[5]

            postagem = Postagem(usuario, mensagem, privacidade, dataHora, curtidas)
            postagens.append(postagem)

        return postagens
