class AnaliseString: 

  def _init_ (self, texto):
    self.texto = texto 

  def contar_caracters(self): 
    return len (self.texto)
    

  def transformar_minusculo(self):
    return self.texto.lower()

  def transforma_maiuscula(self): 
    return self.texto.upper()

  def contar_vogais(self): 
    contador = 0
    for letra in self.texto:
     if letra.lower() in "aeiou":
      contador += 1
    return contador

  def contem_IFB(self): 
    return "ifb" in self.texto.lower()


texto = input("Digite uma string: ")
analise = AnaliseString(texto)

print("Número de caracters: ", analise.contar_caracteres())
print("Texto em minúsculo: ", analise.transformar_minusculo())
print("Texto em maiusculo: ", analise.transforma_maiuscula())
print("Contar vogais: ", analise.contar_vogais())
print("Contém IFB? ", analise.contem_IFB())