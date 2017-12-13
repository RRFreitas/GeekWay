from models.Grupo import Grupo
from database.DAO import DAO
from database.UsuarioDAO import UsuarioDAO

class GrupoDAO(DAO):

    def __init__(self):
        super(GrupoDAO, self).__init__()

    def insert(self, grupo: Grupo):
        # Script de Inserção.
        query = "INSERT INTO tb_grupo(criador_id, nome, data_criacao, descricao) " \
                "VALUES(%s, %s, %s, %s)"
        # Valores.
        values = (grupo.criador.id, grupo.nome, grupo.dataCriacao, grupo.descricao)

        try:
            return super(GrupoDAO, self).insert(query, values)
        except Exception as err:
            print("Erro no banco de dados!")
            print(err)
            return

    def delete(self, id):
        query = "DELETE FROM tb_grupo WHERE id = %s"
        values = (id,)

        try:
            self.execute(query, values)
            return True
        except Exception as err:
            print(err)
            return False

    def update(self, criador, nome, dataCriacao, descricao):
        query = "UPDATE tb_grupo " \
                "SET criador = %s, nome = %s, data_criacao = %s, descricao = %s " \
                "WHERE id = %s;"
        values = (criador, nome, dataCriacao, descricao, id)
        try:
            self.execute(query, values)
            return True
        except Exception as err:
            print(err)
            return False

    def listar(self):
        query = "SELECT * FROM tb_grupo;"
        result = self.get_rows(query)

        usuarioDAO = UsuarioDAO()

        grupos = []

        for row in result:
            criador = usuarioDAO.procurarUsuarioPorId(row[1])
            nome = row[2]
            dataCriacao = row[3]
            descricao  = row[4]

            grupo = Grupo(criador, nome, dataCriacao, descricao)
            grupos.append(grupo)

        return grupos
