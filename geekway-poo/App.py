from CreateDB import criarBanco
from models.Usuario import Usuario
from database.UsuarioDAO import UsuarioDAO

usuarioDAO = UsuarioDAO()

def menuUsuario(usuario):
    limparTela()
    print("Bem vindo, " + usuario.nome + "!")

    op = 100

    while op > 0:
        try:
            op = int(input("Digite uma opção: \n"
                           "1 - Ver meu perfil\n"
                           "2 - Adicionar amigo\n"
                           "3 - Listar amigos\n"
                           "4 - Solicitações de amizade\n"
                           "5 - Enviar mensagem para amigo\n"
                           "6 - Listar mensagens\n"
                           "0 - Logout\n"))
        except:
            print("Essa não é uma opção válida...\n\n\n")
            continue

        #Opção de logout, quando usada quebra o laço, saindo do menu de usuário e voltando para menu principal.
        if(op == 0):
            break

        elif(op == 1):
            limparTela()

            print("===========================")
            print("Nome:", usuario.nome)
            print("Data de nascimento:", usuario.data_nasc)
            print("Profissão:", usuario.profissao)
            print("Gênero:", usuario.genero)
            print("Cidade:", usuario.cidade)
            print("Estado:", usuario.estado)
            print("País:", usuario.pais)
            print("===========================\n")

        #Opção de adicionar amigo, pede o nome da pessoa, procura todos os usuários com esse nome e lista com seu respectivo id,
        #verifica se nenhum usuário foi encontrado
        #se só 1 usuário for encontrado, ele já enviar a solicitação
        #se mais de 1 usuário for encontrado, pede para especificar o id do usuário e em seguida envia solicitação
        elif(op == 2):
            nome = input("Digite o nome da pessoa: ")
            users = usuarioDAO.procurarUsuariosPorNome(nome)

            if len(users) == 0:
                limparTela()
                print("Nenhum usuário com esse nome foi encontrado.")
                continue
            elif len(users) == 1:
                if(usuarioDAO.isFriend(usuario.id, users[0].id)):
                    limparTela()
                    print(users[0].nome + " já é seu amigo!")
                    continue

                limparTela()

                if(usuarioDAO.solicitacaoAmizade(usuario.id, users[0].id)):
                    print("Solicitação de amizade enviada!\n\n")
                else:
                    print("Houve um problema... Não já existe uma solicitação pendente?\n\n")
            else:
                for user in users:
                    print(user.id + " - " + user.nome)

                id = int(input("Digite o ID da pessoa que deseja adicionar: "))

                if(usuarioDAO.procurarUsuarioPorId(id) is None):
                    print("Usuário com esse ID não encontrado.\n\n")
                    continue
                else:
                    if (usuario.isFriend(id)):
                        print(usuarioDAO.procurarUsuarioPorId(id).nome + " já é seu amigo!")
                        continue

                    if(usuario.solicitacaoAmizade(id)):
                        print("Solicitação de amizade enviada!\n\n")
                    else:
                        print("Houve um problema... Não já existe uma solicitação pendente?\n\n")

        #Opção que lista todos os amigos do usuário
        elif(op == 3):
            limparTela()
            for user in usuarioDAO.listarAmigos(usuario.id):
                print(user.nome)

        #Opção que lista todas as solicitações de amizade pendentes
        elif(op == 4):
            if(len(usuarioDAO.listarSolicitacoes(usuario.id)) == 0):
                limparTela()
                print("Nenhuma solicitação pendente!")

            for solicitacao in usuarioDAO.listarSolicitacoes(usuario.id):
                if(not solicitacao[1] is None):
                    print(usuarioDAO.procurarUsuarioPorId(solicitacao[1]).nome + " - " + solicitacao[3])

                    if(solicitacao[3] == "PENDENTE"):
                        op1 = input("Desenha aceitar esta solicitação? (s/n) ")

                        if(op1.lower().startswith("s")):
                            usuarioDAO.aceitarAmizade(solicitacao[1], usuario.id)
                            limparTela()
                            print("Amizade aceita!")
                        elif(op1.lower().startswith("n")):
                            usuarioDAO.negarAmizade(solicitacao[1], usuario.id)
                            limparTela()
                            print("Amizade negada!")

        #Lista os amigos com seus respectivos ids, e em seguida pede o id do usuário a enviar a mensagem, e depois a mensagem
        #Obs: No momento, o usuário pode enviar mensagem para um id que não é seu amigo. (A consertar)
        elif(op == 5):
            for user in usuarioDAO.listarAmigos(usuario.id):
                print(str(user.id) + " - " + str(user.nome))

            id = int(input("Digite o id do amigo que deseja enviar mensagem: "))
            user = usuarioDAO.procurarUsuarioPorId(id)

            if user is None:
                print("Usuário inválido")
                continue

            msg = input("Digite a mensagem que deseja enviar: ")

            usuarioDAO.enviarMensagem(usuario.id, id, msg)
            limparTela()
            print("Mensagem privada enviada com sucesso!")

        #Lista todas as mensagens enviadas e recebidas.
        elif(op == 6):
            msgs = usuarioDAO.listarMensagens(usuario.id)
            limparTela()

            for msg in msgs:
                print(usuarioDAO.procurarUsuarioPorId(msg[2]).nome + " para " + usuarioDAO.procurarUsuarioPorId(msg[1]).nome + ": " + msg[3])

def limparTela():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

def menu():
    op = 100

    while op > 0:
        try:
            op = int(input("Digite uma opção: \n"
                           "1 - Login\n"
                           "2 - Registrar\n"
                           "0 - Sair\n"))
        except:
            limparTela()
            print("Essa não é uma opção válida...\n\n\n")
            continue

        #Quebra o laço e finaliza o programa
        if(op == 0):
            print("Volte sempre...")
            return

        #Pede email e senha e em seguida verifica se existe no banco
        #se for autenticado, vai para o menu de usuário
        elif(op == 1):
            email = input("Digite seu email: ")
            senha = input("Digite sua senha: ")

            if(usuarioDAO.verificar_login(email, senha)):
                limparTela()
                print("Logado com sucesso!\n\n\n")

                usuario = usuarioDAO.procurarUsuarioPorEmail(email)
                menuUsuario(usuario)
            else:
                limparTela()
                print("Login inválido.\n\n\n")
                continue

        #Pede informações de cadastro e verifica se email já existe.
        #se cadastrar, redireciona para menu de usuário
        elif(op == 2):
            nome = input("Digite seu nome: ")
            email = None

            while True:
                email = input("Digite seu email: ")

                if(usuarioDAO.emailExists(email)):
                    print("Este email já existe, cadastre outro.\n")
                    continue
                else:
                    break

            senha = input("Digite sua senha: ")
            user = None

            try:
                user = Usuario(nome, email, senha)
                usuarioDAO.inserirUsuario(user)
            except:
                limparTela()
                print("Oops! Houve algum problema... Talvez você tenha passado dos limites :P")
                continue

            limparTela()
            print("Cadastrado com sucesso!\n\n\n")

            menuUsuario(user)

        limparTela()

def main():
    #Função para criar o banco com todas as tabelas.
    criarBanco()

    #Menu principal
    menu()

if __name__ == '__main__':
    main()