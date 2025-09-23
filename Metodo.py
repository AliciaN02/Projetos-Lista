class Pessoa:
  __NACIONALIDADE = 'BR'
  __estadoUF = 'DF'
  __contador = 0
  
# Atributos de classe privados
  def __init__(self, idade, nome):
      self.__nome = nome
      self.__idade = idade
      Pessoa.__contador +=1

# Métodos de instância públicos
  def diminueIdade(self, valor=1):
      self.__idade -= valor

  def aumentaIdade(self, valor=1):
     self.__idade += valor

  def getIdade(self):
   return self.__idade

  def getNome(self):
   return self.__nome

  def setNome(self, novoNome):
   self.__nome = novoNome

# Métodos de classe públicos
  @classmethod
  def getUF (cls):
    return cls.__estadoUF 
 
  @classmethod
  def setUF(cls, novoValor):
    cls.__estadoUF = novoValor

  @classmethod
  def getContador (cls):
      return cls.__contador 

  @classmethod
  def getNacionalidade(cls):
       return cls.__NACIONALIDADE


p1 = Pessoa(22, 'Alicia')
#Testando os métodos "get" que retornam os valores atribuidos 
print(f"Nome: {p1.getNome()}, Idade: {p1.getIdade()}, Nacionalidade: {p1.getNacionalidade()}, UF:{p1.getUF()}")
print(f"Quantidade de pessoas criadas: {Pessoa.getContador()}")

#Testando os métodos "set" que modificam os atributos
p1.aumentaIdade(10)
p1.diminueIdade()
p1.setNome('Alicia Neves')
p1.setUF('GO')

#Verificando valores após alteração 
print("\nVerificando valores depois das alterações: ")
print(f"Nome: {p1.getNome()}, Idade: {p1.getIdade()}, Nacionalidade:{p1.getNacionalidade()}, UF: {p1.getUF()}")
print(f"Quantidade de pessoas criadas: {Pessoa.getContador()}")