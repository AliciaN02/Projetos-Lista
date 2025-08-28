# Função simples de IA para recomendar livros
def ia_recomendacao(usuario):
    print(f"\n[IA] Olá {usuario.nome}, aqui estão algumas sugestões de livros:")
    # Sugere livros que o usuário ainda não pegou
    sugestoes = [l for l in livros if l not in usuario._Usuarios__emprestimos]
    if sugestoes:
        for l in sugestoes:
            print(f"- {l.getTitulo()} por {l.getAutor()}")
    else:
        print("Você já pegou todos os livros disponíveis!")
