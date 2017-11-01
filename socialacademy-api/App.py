from models.Usuario import Usuario

def main():
    usuario = Usuario("Rennan", "rennan@gmail.com", "123", "01/11/2017", "Data Scientist", "Masculino", "Campina", "PB", "BR", [])
    #usuario.inserir()
    usuario.deletar(1)
    print(usuario.listar())

if __name__ == '__main__':
    main()
