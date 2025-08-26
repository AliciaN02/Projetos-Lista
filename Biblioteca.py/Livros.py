from random import randint
class Livros: 

  def __init__ (self, Titulo, Autor):

    self.__Titulo = Titulo 
    self.__Autor = Autor 
    self.__id = randint(1,100)

  def getTitulo(self):
    return self.__Titulo

  def setTitulo(self, novoTitulo):
        self.__Titulo = novoTitulo

  def getAutor(self):
    return self.__Autor

  def setAutor(self, novoAutor):
        self.__Autor = novoAutor

  def getID(self):
    return self.__id

  