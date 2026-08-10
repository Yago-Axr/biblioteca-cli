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
    print("\n")
    print(Linha)
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        id_livro = int(input("Informe o ID do livro: "))
        titulo = input("Informe o Título do livro: ")
        autor = input("Informe o nome do autor: ")
        ano = int(input("Informe o ano do livro: "))
        print("\n")
        Cadastro = {
            "id": id_livro,
            "titulo": titulo,
            "autor": autor,
            "ano": ano,
            "disponivel": True
        }
        print("Livro cadastrado com sucesso!!")
        Livros.append(Cadastro)

    elif opcao == 2:
        if not Livros:
            print("Nenhum Livro cadastrado.")
        else:
            for livro in Livros:
                print(f"ID: {livro['id']}")
                print(f"Título: {livro['titulo']}")
                print(f"Autor: {livro['autor']}")
                print(f"Ano: {livro['ano']}")
                print("Disponível: ", end="")
                if livro['disponivel']:
                    print("Sim")
                else:
                    print("Não")
                print("-" * 50)
    elif opcao == 3:
        buscador = int(input("Qual o ID do livro: "))
        encontrado = False
        for livro in Livros:
            if buscador == livro['id']:
                 encontrado = True
                 print(f"ID: {livro['id']}")
                 print(f"Título: {livro['titulo']}")
                 print(f"Autor: {livro['autor']}")
                 print(f"Ano: {livro['ano']}")
                 print("Disponível: ", end="")
                 if livro['disponivel']:
                    print("Sim")
                 else:
                    print("Não")
                 print("-" * 50)
                 break
        if not encontrado:
            print("ID não encontrado")
    elif opcao == 4:
        pedir_id = int(input("Informe o ID do livro: "))
        emprestado = False
        for livro in Livros:
            if pedir_id == livro['id']:
                emprestado = True
                print(f"ID: {livro['id']} encontrado")
                if livro['disponivel']:
                    print("Livro disponivel.")
                else:
                    print("Livro emprestado")
                break
        if not emprestado:
            print("Não encontrado.")


                     
    elif opcao == 7:
        print("Encerrando o programa")
        break
    else:
        print("Opção Inválida!")
    