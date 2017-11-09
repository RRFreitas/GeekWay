from models.Usuario import Usuario

def main():
    usuario = Usuario("Rennan", "rennan@gmail.com", "123", "01/11/2017", "Data Scientist", "Masculino", "Campina", "PB", "BR", [])
    #usuario.inserir()
    #usuario.deletar(5)
    #print(usuario.listar()[0].nome)

   # usuario.atualizar(6, "Rennan2", "rennan@gmail.com", "123", "01/11/2017", "Data Scientist", "Masculino", "Campina", "PB", "BR")
    print(usuario.listar()[0].nome)

if __name__ == '__main__':
    main()
