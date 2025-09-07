class Criptografia: 

  def __init__ (self, frase): 
    self.frase = frase 
    self.criptografada = ""  # atributo para guardar o resultado criptografado
    pass 

  def criptografar(self):
    substituicoes = {
        "a": "4", "A": "4",
        "e": "3", "E": "3",
        "i": "1", "I": "1",
        "o": "0", "O": "0",
        "u": "8", "U": "8"
    }

    nova_frase = ""  # acumulador para construir a frase criptografada
    for letra in self.frase:
        nova_frase += substituicoes.get(letra, letra)

    self.criptografada = nova_frase

  def mostrar(self):
    if self.criptografada == "":
     print("A frase ainda não foi criptografada. Use o método criptografar () primeiro.")

    else: 
     print("Frase criptografada", self.criptografada)
      
texto = (input("Digite uma frase: "))
obj = Criptografia(texto)
obj.criptografar()
obj.mostrar()
