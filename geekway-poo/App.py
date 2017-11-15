from CreateDB import criarBanco
from models.Usuario import Usuario

def menuUsuario(usuario):
    print("\n\n\n\n\n\n\n\n")
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

        if(op == 0):
            break
        elif(op == 1):
            nome = input("Digite o nome da pessoa: ")
            users = Usuario.findUsersByName(nome)

            if len(users) == 0:
                print("Nenhum usuário com esse nome foi encontrado.")
                continue
            elif len(users) == 1:
                usuario.solicitacaoAmizade(users[0].id)
                print("Solicitação de amizade enviada!\n\n")
            else:
                for user in users:
                    print(user.id + " - " + user.nome)

                id = int(input("Digite o ID da pessoa que eseja adicionar: "))

                if(Usuario.findUserById(id) is None):
                    print("Usuário com esse ID não encontrado.\n\n")
                    continue
                else:
                    usuario.solicitacaoAmizade(id)
                    print("Solicitação de amizade enviada!\n\n")
        elif(op == 2):
            for user in usuario.listarAmigos():
                print(user.nome)
        elif(op == 3):

            for solicitacao in usuario.listarSolicitacoes():
                if(not solicitacao[1] is None):
                    print(Usuario.findUserById(solicitacao[1]).nome + " - " + solicitacao[3])

                    if(solicitacao[3] == "PENDENTE"):
                        op1 = input("Desenha aceitar esta solicitação? (s/n) ")

                        if(op1.lower().startswith("s")):
                            usuario.aceitarAmizade(solicitacao[1])
                            print("\n\n\n\nAmizade aceita!")
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
            print("\n\n\n\nMensagem privada enviada com sucesso!")

        elif(op == 5):
            msgs = usuario.listarMensagens()
            print("\n\n\n\n")

            for msg in msgs:
                print(Usuario.findUserById(msg[2]).nome + " para " + Usuario.findUserById(msg[1]).nome + ": " + msg[3])

def menu():
    op = 100

    while op > 0:
        try:
            op = int(input("Digite uma opção: \n"
                           "1 - Login\n"
                           "2 - Registrar\n"
                           "0 - Sair\n"))
        except:
            print("Essa não é uma opção válida...\n\n\n")
            continue

        if(op == 0):
            print("Volte sempre...")
            return
        elif(op == 1):
            email = input("Digite seu email: ")
            senha = input("Digite sua senha: ")

            if(Usuario.verificar_login(email, senha)):
                print("Logado com sucesso!\n\n\n")

                usuario = Usuario.findUserByEmail(email)
                menuUsuario(usuario)
            else:
                print("Login inválido.\n\n\n")
                continue
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

            print("Cadastrado com sucesso!\n\n\n")

            menuUsuario(user)

def main():
    criarBanco()
    menu()

if __name__ == '__main__':
    main()