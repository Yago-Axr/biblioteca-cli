Livros = []

while True:
    Titulo = "BIBLIOTECA"
    Linha = "=" * 50
    print(Linha)
    print(Titulo.center(50))
    print(Linha)


    print("1 - Cadastrar Livro")
    print("2 - Listar Livro")
    print("3 - Buscar Livro")
    print("4 - Emprestar Livro")
    print("5 - Devolver Livro")
    print("6 - Remover Livro")
    print("7 - Sair")

    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        Id = int(input("Qual o ID do Livro: "))
        titulo = input("Qual o título do Livro: ")
        autor = input("Qual o autor do Livro: ")
        ano = int(input("Qual o ano do Livro: "))

        livro = {
            "ID" : Id

        }
    elif opcao == 7:
        print("Encerrando o programa")
        break
    else:
        print("Opção Inválida!")
    