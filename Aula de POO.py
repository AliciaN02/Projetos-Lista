'''class Veiculo():
    def __init__(self,marca,rodas,cor,ano,portas):
     self.marca = marca
     self.rodas = rodas
     self.cor = cor
     self.ano = ano
     self.portas = portas
     self.ligado = False

    def ligar(self):
     self.ligado = True
     print('Ligado')
  
    def aumentaAno(self, sobeAno): 
     self.ano += sobeAno

    def dimuneAno(self, desceAno):
     self.ano -= desceAno

    def desliga(self):
     self.desliga = False
     print('Desligado')

    def abrirPortas(self): 
     self.portas = True
     print('Portas abertas')

    def fecharportas(self):
     self.portas = False
     print('Portas fechadas')

v1 = Veiculo('Bmw', 4, 'Preto', 2025, 'Portas')
print(v1.ano)   
print(v1.cor)
print(v1.rodas)
print(v1.marca)

v1.abrirPortas()
v1.fecharportas() 
'''
 
class Pessoa(): 
    def __init__(self, nome, idade, altura,cor):
        self.nome = nome 
        self.idade = idade 
        self.altura = altura 
        self.cor = cor 
        self.acordar = False
        self.dormir = False
    
    def acordarPessoa (self):
        self.acordar = True
        print('Acordado')         

    def dormirPessoa (self): 
        self.dormir =True
        print('Dormindo')
    
p1 = Pessoa ('Alicia', 22, 1.71, 'Branca')
print(p1.nome)   
print(p1.idade)
print(p1.altura)
print(p1.cor)

p1.acordarPessoa()





    
