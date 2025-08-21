class Estudante:
 Escola = 'IFB'  #Atributos de Classe 
 NACIONALIDADE = 'BR' # Atributos de Classe Constante
 contadorEstudantes = 0

 #método construtor
 def __init__(self, nome, idade):
   self.nome = nome
   self.idade = idade
   Estudante.contadorEstudantes += 1


 #método de instância - modifica atributos da instância
 def atualizaIdade(self, novaIdade):
   self.idade = self.idade + novaIdade


 #métodos de classe - modifica apenas atributos da classe
 @classmethod
 def modificaEscola(cls, novaEscola):
   cls.escola = novaEscola


e1 = Estudante('Alicia', 22)
print(e1.nome, e1.idade)

e1.atualizaIdade(10)
Estudante.modificaEscola('GDF')

print(f"Quantidade de estudantes: {Estudante.contadorEstudantes}")
print(f"Nome:{e1.nome}, Idade:{e1.idade}, Escola: {Estudante.Escola}, NACIONALIDADE: {e1.NACIONALIDADE}")
      