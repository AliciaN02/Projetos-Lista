# Função principal do menu interativo
def menu():
    while True:  # Loop infinito, o menu fica ativo até o usuário escolher sair
        print("\n=== Biblioteca ===")
        print("1. Listar usuários")
        print("2. Listar livros")
        print("3. Emprestar livro")
        print("4. Devolver livro")
        print("5. Listar livros emprestados")
        print("6. Sair")
        
        opcao = input("Escolha uma opção: ")  # Recebe a opção do usuário

        # Opção 1: Listar todos os usuários
        if opcao == "1":
            print("\n--- Usuários ---")
            for u in usuarios:  # Percorre a lista de usuários
                print(f"Nome: {u.nome}, Matrícula: {u.getMatricula()}")  # Exibe nome e matrícula
        
        # Opção 2: Listar todos os livros
        elif opcao == "2":
            print("\n--- Livros ---")
            for l in livros:  # Percorre a lista de livros
                print(f"Título: {l.getTitulo()}, Autor: {l.getAutor()}, ID: {l.getID()}")  # Exibe informações do livro
        
        # Opção 3: Emprestar livro
        elif opcao == "3":
            user_id = int(input("Informe a matrícula do usuário: "))  # Pede a matrícula do usuário
            livro_id = int(input("Informe o ID do livro: "))  # Pede o ID do livro
