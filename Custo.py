''' 1 - O custo ao consumidor de um carro novo é a soma do custo de fábrica com a porcentagem do distribuidor
e dos impostos (aplicados ao custo de fábrica).
Supondo que a porcentagem do distribuidor seja de 8% do preço de fábrica e os impostos de 20% do preço de
fábrica, fazer um programa em Python para ler o
custo de fábrica de um carro e imprimir, o preço de fábrica, o valor do imposto, o valor da porcentagem do
distribuidor custo e ao consumidor. Usar funções.
'''
def calcular_custo_consumidor(custo_fabrica):
    valor_distribuidor = custo_fabrica * 0.8
    valor_impostos = custo_fabrica * 0.20
    custo_consumidor = custo_fabrica + valor_distribuidor + valor_impostos
    return custo_consumidor, valor_distribuidor, valor_impostos

        #Solicita ao usuario o custo
custo_fabrica = float(input("Informe o custo de fabrica: "))

        #Calcula as variaveis dentro da def e retorna
custo_consumidor, valor_distribuidor, valor_impostos = calcular_custo_consumidor(custo_fabrica)


        #Exibe ao usuario o custo ao consumidor somado aos impostos e imprime 
print(f"O custo ao consumidor é: {custo_consumidor:.2f} ")
print(f"O valor do imposto é:{valor_impostos:.2f} ")
print(f"O valor da porcentagem do distribuidor é: {valor_distribuidor:.2f}")
