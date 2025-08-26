class Usuarios: 

    def __init__(self, nome, matricula):
        self.nome = nome 
        self.__matricula = matricula 
        self.__emprestimos = list()

    def getMatricula(self):
        return self.__matricula
    
    def setMatricula(self, novoValor):
        self.__matricula = novoValor

    def emprestaLivros(self, livro):
        if not livro in self.__emprestimos: 
            self.__emprestimos.append(livro)
            return True
        else: 
            return False

    def devolveLivros(self, livro):
        if livro in self.__emprestimos: 
            self.__emprestimos.remove(livro)
            return True 
        else: 
            return False
        
    def listaEmprestimos(self):
        if self.__emprestimos:
         for livro in self.__emprestimos: 
            print(f"Titulo: {livro.getTitulo()}, Autor: {livro. getAutor()}, ID: {livro.getID()}")

        else: 
            print("Usuário sem empréstimos")

