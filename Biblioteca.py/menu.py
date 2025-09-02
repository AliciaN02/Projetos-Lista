
while True:  # Loop infinito
    print("\n===== MENU =====")
    print("1. Listar usuários")
    print("2. Listar livros")
    print("3. Emprestar livros")
    print("4. Devolver livros")
    print("5. Listar livros emprestados")
    print("6. Sair")

    opcao = input("Informe a opção desejada: ")

    if opcao == "1": 
        print("\n--- Lista de usuários ---")
        for usuario in usuarios:
            print(f"Nome: {usuario.nome}, Matrícula: {usuario.getMatricula()}")

    elif opcao == "2": 
        print("\n--- Lista de livros ---")
        for livro in livros:
            print(f"Título: {livro.getTitulo()}, Autor: {livro.getAutor()}, ID: {livro.getID()}")

    elif opcao == "3": 
        print("\n--- Emprestar Livros ---")
        matricula = int(input("Digite a matrícula do usuário: ")) 
        id_livro = int(input("Digite o ID do livro: "))

        # Encontrar usuário
        usuario_encontrado = None 
        for usuario in usuarios: 
            if usuario.getMatricula() == matricula:
                usuario_encontrado = usuario 
                break

        # Encontrar livro
        livro_encontrado = None 
        for livro in livros: 
            if livro.getID() == id_livro:
                livro_encontrado = livro
                break

        # Tentar emprestar
        if usuario_encontrado and livro_encontrado:
            if usuario_encontrado.emprestaLivros(livro_encontrado):
                print(f"Livro '{livro_encontrado.getTitulo()}' emprestado para {usuario_encontrado.nome}!")
            else:
                print("Esse usuário já possui esse livro emprestado.")
        else:
            print("❌ Usuário ou livro não encontrado.")

    elif opcao == "4":
        print("\n--- Devolver livros ---")
        matricula = int(input("Digite a matrícula do usuário: ")) 
        id_livro = int(input("Digite o ID do livro: "))

        # Encontrar usuário
        usuario_encontrado = None
        for usuario in usuarios:
            if usuario.getMatricula() == matricula:
                usuario_encontrado = usuario
                break

        # Encontrar livro
        livro_encontrado = None
        for livro in livros:
            if livro.getID() == id_livro:
                livro_encontrado = livro
                break

        # Tentar devolver
        if usuario_encontrado and livro_encontrado:
            if usuario_encontrado.devolveLivros(livro_encontrado):
                print(f"Livro '{livro_encontrado.getTitulo()}' devolvido por {usuario_encontrado.nome}!")
            else:
                print("Esse usuário não possui esse livro emprestado.")
        else:
            print("❌ Usuário ou livro não encontrado.")

    elif opcao == "5":
        print("\n--- Livros emprestados ---")
        matricula = int(input("Digite a matrícula do usuário: "))

        usuario_encontrado = None
        for usuario in usuarios:
            if usuario.getMatricula() == matricula:
                usuario_encontrado = usuario
                break

        if usuario_encontrado:
            print(f"\nLivros emprestados por {usuario_encontrado.nome}:")
            usuario_encontrado.listaEmprestimos()
        else:
            print(" Usuário não encontrado.")

    elif opcao == "6":
        print("Saindo do sistema... Até logo!")
        break

    else: 
        print(" Opção inválida, tente novamente.")
