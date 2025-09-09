class TestaInteiro: 
  
    def testando(self):
         while True:
             try:
                valor = int(input("Digite um valor inteiro: "))
                print(f"O valor:{valor} é inteiro")
                break
             except ValueError: 
                print("Erro! Digite um valor inteiro.")    

             
t = TestaInteiro()

t.testando()
