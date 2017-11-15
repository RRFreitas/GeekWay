from CreateDB import criarBanco
from models.Usuario import Usuario

def menuUsuario(usuario):
    limparTela()
    print("Bem vindo, " + usuario.nome + "!")

    op = 100

    while op > 0:
        try:
            op = int(input("Digite uma opção: \n"
                           "1 - Adicionar amigo\n"
                           "2 - Listar amigos\n"
                           "3 - Solicitações de amizade\n"
                           "4 - Enviar mensagem para amigo\n"
                           "5 - Listar mensagens\n"
                           "0 - Logout\n"))
        except:
            print("Essa não é uma opção válida...\n\n\n")
            continue

        #Opção de logout, quando usada quebra o laço, saindo do menu de usuário e voltando para menu principal.
        if(op == 0):
            break

        #Opção de adicionar amigo, pede o nome da pessoa, procura todos os usuários com esse nome e lista com seu respectivo id,
        #verifica se nenhum usuário foi encontrado
        #se só 1 usuário for encontrado, ele já enviar a solicitação
        #se mais de 1 usuário for encontrado, pede para especificar o id do usuário e em seguida envia solicitação
        elif(op == 1):
            nome = input("Digite o nome da pessoa: ")
            users = Usuario.findUsersByName(nome)

            if len(users) == 0:
                limparTela()
                print("Nenhum usuário com esse nome foi encontrado.")
                continue
            elif len(users) == 1:
                if(usuario.isFriend(users[0].id)):
                    limparTela()
                    print(users[0].nome + " já é seu amigo!")
                    continue

                usuario.solicitacaoAmizade(users[0].id)
                limparTela()
                print("Solicitação de amizade enviada!\n\n")
            else:
                for user in users:
                    print(user.id + " - " + user.nome)

                id = int(input("Digite o ID da pessoa que eseja adicionar: "))

                if(Usuario.findUserById(id) is None):
                    print("Usuário com esse ID não encontrado.\n\n")
                    continue
                else:
                    if (usuario.isFriend(id)):
                        print(Usuario.findUserById(id).nome + " já é seu amigo!")
                        continue
                    usuario.solicitacaoAmizade(id)
                    print("Solicitação de amizade enviada!\n\n")

        #Opção que lista todos os amigos do usuário
        elif(op == 2):
            limparTela()
            for user in usuario.listarAmigos():
                print(user.nome)

        #Opção que lista todas as solicitações de amizade pendentes
        elif(op == 3):
            if(len(usuario.listarSolicitacoes()) == 0):
                print("Nenhuma solicitação pendente!")

            for solicitacao in usuario.listarSolicitacoes():
                if(not solicitacao[1] is None):
                    print(Usuario.findUserById(solicitacao[1]).nome + " - " + solicitacao[3])

                    if(solicitacao[3] == "PENDENTE"):
                        op1 = input("Desenha aceitar esta solicitação? (s/n) ")

                        if(op1.lower().startswith("s")):
                            usuario.aceitarAmizade(solicitacao[1])
                            limparTela()
                            print("Amizade aceita!")

        #Lista os amigos com seus respectivos ids, e em seguida pede o id do usuário a enviar a mensagem, e depois a mensagem
        #Obs: No momento, o usuário pode enviar mensagem para um id que não é seu amigo. (A consertar)
        elif(op == 4):
            for user in usuario.listarAmigos():
                print(str(user.id) + " - " + str(user.nome))

            id = int(input("Digite o id do amigo que deseja enviar mensagem: "))
            user = Usuario.findUserById(id)

            if user is None:
                print("Usuário inválido")
                continue

            msg = input("Digite a mensagem que deseja enviar: ")

            usuario.enviarMensagem(id, msg)
            limparTela()
            print("Mensagem privada enviada com sucesso!")

        #Lista todas as mensagens enviadas e recebidas.
        elif(op == 5):
            msgs = usuario.listarMensagens()
            limparTela()

            for msg in msgs:
                print(Usuario.findUserById(msg[2]).nome + " para " + Usuario.findUserById(msg[1]).nome + ": " + msg[3])

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

            if(Usuario.verificar_login(email, senha)):
                limparTela()
                print("Logado com sucesso!\n\n\n")

                usuario = Usuario.findUserByEmail(email)
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

                if(Usuario.emailExists(email)):
                    print("Este email já existe, cadastre outro.\n")
                    continue
                else:
                    break

            senha = input("Digite sua senha: ")
            user = None

            try:
                user = Usuario(nome, email, senha)
                user.inserir()
            except:
                print("Erro!")
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