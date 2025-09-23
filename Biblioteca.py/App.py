from Usuarios import Usuarios 
from Livros import Livros 

#Criando os Livros 

livro1 = Livros('Almanaque da Mônica', 'Mauricio de Souza')
livro2 = Livros('As Esganadas', 'Jo Soares')
livro3 = Livros('Dicionario', 'Aurelio')

#Criando Usuários 
usuario1 = Usuarios('Miguel', 2112)
usuario2 = Usuarios('Samuel', 2003)

#Realizar empréstimos 

usuario1.emprestaLivros(livro1)
usuario1.emprestaLivros(livro2)

usuario2.emprestaLivros(livro3) 

#Listar os empréstimos 

print(f"Lista {usuario1.nome} - Matricula {usuario1.getMatricula()}")
usuario1.listaEmprestimos()
print(f"Lista {usuario2.nome} - Matricula {usuario2.getMatricula()}")
usuario2.listaEmprestimos()

#Devolver Livros 
usuario1.devolveLivros(livro1)
usuario2.devolveLivros(livro3)
usuario1.devolveLivros(livro2)


print(f"Lista {usuario1.nome} - Matricula {usuario1.getMatricula()}")
usuario1.listaEmprestimos()
print(f"Lista {usuario2.nome} - Matricula {usuario2.getMatricula()}")
usuario2.listaEmprestimos()


