class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []  # composição: Biblioteca contém livros

    def criarLivros(self, titulo, ano, autor):
        # Evitar duplicatas
        for livro in self.livros:
            if livro.titulo == titulo:
                print(f"O livro '{titulo}' já está armazenado na biblioteca!")
                return
        novo_livro = Livro(titulo, ano, autor)
        self.livros.append(novo_livro)
        print(f"Novo livro '{titulo}' criado e adicionado com sucesso!")

    def listarLivros(self):
        if not self.livros:
            print("Nenhum livro na biblioteca ainda.")
        else:
            print(f"\nLivros disponíveis na biblioteca {self.nome}:")
            for livro in self.livros:
                print(f"- {livro.titulo} ({livro.ano}), Autor: {livro.referenciaAutor.nome}")


class Livro: 
    def __init__(self, titulo, ano, autor):
        self.titulo = titulo
        self.ano = ano
        self.referenciaAutor = autor  # agregação: Autor existe independente


class Autor:
    def __init__(self, nome, nacionalidade):
        self.nome = nome 
        self.nacionalidade = nacionalidade 


class Usuario: 
    def __init__(self, nome, biblioteca):
        self.nome = nome 
        self.biblioteca = biblioteca  # associação: Usuário conhece uma biblioteca

    def pegarLivro(self, titulo):
        # dependência: usa o livro temporariamente
        for livro in self.biblioteca.livros:
            if livro.titulo == titulo:
                print(f"{self.nome} pegou emprestado o livro '{livro.titulo}' de {livro.referenciaAutor.nome}.")
                return livro  
        print(f"O livro '{titulo}' não foi encontrado na biblioteca.")


# -------------------------------
# TESTANDO O SISTEMA
# -------------------------------
if __name__ == "__main__":
    # Criando autores
    autor1 = Autor("Machado de Assis", "Brasileiro")
    autor2 = Autor("George Orwell", "Britânico")

    # Criando biblioteca
    minha_biblioteca = Biblioteca("Biblioteca Central")

    # Adicionando livros
    minha_biblioteca.criarLivros("Dom Casmurro", 1899, autor1)
    minha_biblioteca.criarLivros("Memórias Póstumas de Brás Cubas", 1881, autor1)
    minha_biblioteca.criarLivros("1984", 1949, autor2)

    # Listar livros
    minha_biblioteca.listarLivros()

    # Criar usuário
    usuario1 = Usuario("Alicia", minha_biblioteca)

    # Usuário pega livros
    usuario1.pegarLivro("Dom Casmurro")
    usuario1.pegarLivro("O Alienista")  # não existe
