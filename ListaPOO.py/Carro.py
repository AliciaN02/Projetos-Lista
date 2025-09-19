class Veiculo: 
  def __init__(self,marca):
    self. marca = marca

  def descrição(self):
    print(f"A marca do veículo é: {self.marca}")

class Carro(Veiculo): 
  def __init__(self,marca,modelo):
    super().__init__(marca)
    self.modelo = modelo
     
  def descrição(self):
        super().descrição()  # Chama o método da classe mãe
        print(f"A marca {self.marca} (possui um modelo {self.modelo})")

c1 = Carro("Fiat", "Uno")
c1.descrição()
