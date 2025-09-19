class Animal: 
  def __init__(self,nome):
    self.nome = nome 

  def falar(self):
    print(f"{self.nome} faz um barulho generico!")

class Cachorro(Animal): 
  def __init__(self,nome,raça):
    super().__init__(nome)
    self.raça = raça
     
  def falar(self):
        print("\n")
        super().falar()  # Chama o método da classe mãe
        print(f"{self.nome} (um {self.raça}) está latindo:Au,au,au")

dog = Cachorro("Senhorita Rodrigues", "Golden")
dog.falar()
