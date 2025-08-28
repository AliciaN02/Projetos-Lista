# Função principal do menu interativo
def menu():
    while True:  # Loop infinito, mantém o menu ativo até o usuário escolher sair
        print("\n=== Biblioteca ===")
        print("1. Listar usuários")             # Opção para mostrar todos os usuários
        print("2. Listar livros")               # Opção para mostrar todos os livros
        print("3. Emprestar livro")             # Opção para emprestar um livro a um usuário
        print("4. Devolver livro")              # Opção para devolver um livro emprestado
        print("5. Listar livros emprestados")   # Opção para mostrar todos os empréstimos
        print("6. Sugestão da IA")              # Opção para receber sugestões de livros pelo sistema de IA
        print("7. Sair")                        # Opção para encerrar o programa
        
        opcao = input("Escolha uma opção: ")  # Recebe a opção escolhida pelo usuário

        # Opção 1: Listar todos os usuários cadastrados
        if opcao == "1":
            for u in usuarios:  # Percorre a lista de usuários
                print(f"Nome: {u.nome}, Matrícula: {u.getMatricula()}")  # Exibe nome e matrícula
        
        # Opção 2: Listar todos os livros cadastrados
        elif opcao == "2":
            for l in livros:  # Percorre a lista de livros
                print(f"Título: {l.getTitulo()}, Autor: {l.getAutor()}, ID: {l.getID()}")  # Exibe informações do livro
        
        # Opção 3: Emprestar livro para um usuário
        elif opcao == "3":
            user_id = int(input("Informe a matrícula do usuário: "))  # Pede a matrícula do usuário
            livro_id = int(input("Informe o ID do livro: "))          # Pede o ID do livro
            # Busca o usuário e o livro na lista
            usuario = next((u for u in usuarios if u.getMatricula() == user_id), None)
            livro = next((l for l in livros if l.getID() == livro_id), None)

            if usuario and livro:  # Verifica se ambos existem
                if usuario.emprestaLivros(livro):  # Tenta realizar o empréstimo
                    print(f"{livro.getTitulo()} emprestado para {usuario.nome}")
                else:
                    print("Livro já está emprestado para este usuário.")
            else:
                print("Usuário ou livro não encontrado.")
        
        # Opção 4: Devolver livro emprestado
        elif opcao == "4":
            user_id = int(input("Informe a matrícula do usuário: "))  # Pede matrícula do usuário
            livro_id = int(input("Informe o ID do livro: "))          # Pede ID do livro
            # Busca o usuário e o livro na lista
            usuario = next((u for u in usuarios if u.getMatricula() == user_id), None)
            livro = next((l for l in livros if l.getID() == livro_id), None)

            if usuario and livro:  # Verifica se ambos existem
                if usuario.devolveLivros(livro):  # Tenta devolver o livro
                    print(f"{livro.getTitulo()} devolvido por {usuario.nome}")
                else:
                    print("Este usuário não possui este livro emprestado.")
            else:
                print("Usuário ou livro não encontrado.")
        
        # Opção 5: Listar livros emprestados por cada usuário
        elif opcao == "5":
            for u in usuarios:  # Percorre a lista de usuários
                print(f"\nUsuário: {u.nome} - Matrícula: {u.getMatricula()}")
                u.listaEmprestimos()  # Mostra os livros emprestados por esse usuário
        
        # Opção 6: Sugestão de livros pelo sistema de IA
        elif opcao == "6":
            user_id = int(input("Informe a matrícula do usuário para receber recomendações: "))
            usuario = next((u for u in usuarios if u.getMatricula() == user_id), None)
            if usuario:
                ia_recomendacao(usuario)  # Chama a função de IA para sugerir livros
            else:
                print("Usuário não encontrado.")
        
        # Opção 7: Sair do menu
        elif opcao == "7":
            print("Saindo do sistema...")
            break  # Encerra o loop e sai do menu
        
        # Caso o usuário digite uma opção inválida
