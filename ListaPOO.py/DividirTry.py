class Dividir: 

    def divisor(self): 
    
        try: 
            valor = int(input("Informe o primeiro número: "))
            valor2 = int(input("Informe o segundo número: "))
            resultado = valor / valor2
            print("O valor dividido dos números é", resultado)

        except ValueError:
            print("Digite um número inteiro!" )

        except ZeroDivisionError:    
            print("Não é possível dividir por zero!")

d = Dividir()
d.divisor()