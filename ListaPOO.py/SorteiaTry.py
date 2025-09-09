#Criarm código que sorteia um número entre 1 e N, onde N é fornecido pelo usuário. Tratar erros como entrada não numérica, número negativo ou zero. 
from random import randint 

class Sorteia: 

    def sorteando(self): 
       try: 
        valor = int(input("Informe o valor de N: "))
        if valor > 0:
             raise ValueError("O número deve ser maior que zero")
        else: 
          numero = randint(1, valor)
          print("Número sorteado:", numero)
                                
       except ValueError: 
          print("Erro! Informe um valor inteiro")

d = Sorteia()
d.sorteando()
