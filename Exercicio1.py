'''  Uma livraria quer controlar seu estoque usando um dicionário onde as chaves são os títulos dos livros e os valores são a quantidade disponível em estoque.  Implemente um programa com as seguintes funcionalidades:

1. Adicionar um livro ao estoque: o usuário informa o título e a quantidade (se o livro já existir, some a quantidade nova à existente).

2. Remover unidades de um livro: o usuário informa o título e a quantidade a remover; o programa deve atualizar o estoque e avisar se o estoque ficar zerado ou se o livro não existir.

3. Consultar quantidade de um livro: o usuário digita o título e o programa mostra a quantidade disponível ou informa que o livro não está no estoque.

4. Mostrar todos os livros com suas quantidades ordenados alfabeticamente.

5. Sair

O programa deve repetir o menu até que o usuário escolha sair. Utilizar função.
'''
def removeLivro(dicLivros):
   print("==Remove Livro==")
   titulo = input("Titulo").lower().strip()
   if titulo not in dicLivros: 
       print("Titulo não cadastrado!")
        
   else: 
        if dicLivros [titulo] == 0:
            print("Estoque zerado para este titulo!")
        else:
            quantidade = int(input("Quantidade: "))
            if quantidade > dicLivros [titulo]:
               print (f"Quantidade atual insuficiente: {dicLivros[titulo]}")

            else: 
             dicLivros[titulo] -= quantidade
    
             print(f"Quantidade atualizada: {dicLivros[titulo]}")
   
def addLivro(dicLivros):
   print("==Adiciona Livro==")

   titulo = input("Titulo: ").lower().strip()
   quantidade = int(input("Quantidade: ")) 
   if titulo in dicLivros: 
      dicLivros[titulo] += quantidade
   else: 
      dicLivros[titulo] = quantidade 
      print(dicLivros)

def menu (dicLivros):
    print("\n==Livraria==")
    print("1.Adicionar um livro\n2.Remover unidades\n3.Consultar quantidade\n4. Mostrar todos\n5.Sair ")
    op = input("Escolha: ")

    while True:
     if op == '5':
       print("Saindo...")
       break
     elif op == '4':
        pass
     elif op == '3':
        pass
     elif op == '2':
        removeLivro(dicLivros)
     elif op == '1':
        addLivro(dicLivros)
     else:
        print("Opção inválida")

     
def main ():
    dicLivros={"Sherlock":10}
    menu(dicLivros)


    pass
 
if __name__ == "__main__":

    main()
    