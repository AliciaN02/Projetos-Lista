'''Faça um programa em python para cadastro de agenda. 

O programa deve utilizar dicionários para cadastrar os contatos, usando como chaves, nome, endereço, e-mail e telefone. Os dicionários devem ser guardados em uma lista.

O menu deve oferecer as seguintes opções: 

1. Adicionar contato - deve verificar se o contato já existe antes de adicionar.

2. Editar contato - deve solicitar o nome de um contato, verificar sua existência e solicitar que o usuário entre com os dados do contato novamente, menos o nome.

3. Buscar contato - deve solicitar o nome de um contato e mostrar os dados.

4. Listar contatos - deve listar os contatos em ordem alfabética.

5. Remover contato - deve remover um contato existente.

6. Sair.

'''
def editar_Contatos(lista_contatos):
    print("\n== Editar Contato ==")

    if not lista_contatos:
        print("Nenhum contato cadastrado!")
    else:
        nome = input("Digite o nome do contato que voce deseja editar: ").lower().strip()
        teste = False
    for item in lista_contatos:
        if nome in item['nome']:
            print(f"Contato encontrado {nome}")                         #Recebe as inforções atualizadas
            item['end']=input("Endereço: ").lower().strip(),
            item['email']=input("Email: ").lower().strip(),
            item['fone']=input("Telefone: ").lower().strip()
            teste = True
    if not teste:
        print("Contato não encontrado")

def addContato(lista_contatos):
    print("\n==Add Contato==")
    nome = input("Nome: ").lower().strip()

    contato ={}
    for item in lista_contatos: 
        if item in contato['nome']:
         print("Contato já cadastrado.")
        return
    else: 
        contato = {
            "nome":nome,
            "end":input("Endereço: ").lower().strip(),
            "e-mail":input("Email: ").lower().strip(),
            "fone":input("Telefone: ").lower().strip()
        }

        lista_contatos.append(contato)
    
def removerContato(lista_contatos):
    print("==RemoverContato==")
    contato = input("Contato: ").strip()

    if contato not in lista_contatos:
        print("Contato não encontrado!")
    else: 
        print(lista_contatos.pop(contato))
              

def menu(lista_contatos):
    print("==Menu==")
    
    while True:
        print("1.Adicionar contato\n2. Editar contato\n3. Buscar contato\n4. Listar contatos\n5. Remover contato\n6. Sair")
        op= input("Opção: ")

        if op == '1':
         addContato(lista_contatos)
        elif op == '2':
         editar_Contatos(lista_contatos)
        elif op == '3':
            pass
        elif op == '4':
            pass
        elif op == '5':
            removerContato(lista_contatos)
        elif op == '6':
            print("Saindo")
            break
        else:
            print("Opção inválida!")

def main():
    lista_contatos = [] 
    menu(lista_contatos)

if __name__ == "__main__":
    main()