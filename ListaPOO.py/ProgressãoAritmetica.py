class ProgressaoAritmetica: 

  def _init_(self, n, a1, r):
    self.n = n 
    self.a1 = a1
    self.r = r

  def calcula_ultimo_termo(self):
    an = self.a1 + self.r * (self.n -1)
    return an

  def lista_termos(self):
    termos = []
    for i in range(self.n):
        termo = self.a1 + self.r * i  # cálculo do termo
        termos.append(termo)
    return termos
  
  def soma_termos(self):
    an = self.calcula_ultimo_termo()  # pega o último termo
    soma = self.n * (self.a1 + an) / 2
    return soma

  n = int(input("Digite o número de termos: "))
  a1 = int(input("Digite o primeiro termo: "))
  r = int(input("Digite a razão: "))