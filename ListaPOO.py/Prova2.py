class Residencia:
    class __Comodo:  #Classe interna (representa um cômodo da residência).
        def __init__(self, nome, area):
            self.nome = nome
            self.area = area

        def __str__(self):
            return f'{self.nome} - {self.area}m²'

    def __init__(self):  #Construtor da residência
        self.__comodos = []  #Lista privada de cômodos

    def adicionar_comodo(self, nome, area):  #Adiciona um novo cômodo
        novo_comodo = self.__Comodo(nome, area)
        self.__comodos.append(novo_comodo)

    def exibir_comodos(self):  #Exibe a lista de cômodos
        if not self.__comodos:
            print("Nenhum cômodo foi adicionado ainda.")
        else:
            print("Cômodos da residência:")
            for i, comodo in enumerate(self.__comodos, start=1):
                print(f'{i}. {comodo}')

    def calcular_area_total(self):  #Calcula a soma da área de todos os cômodos
        return sum(comodo.area for comodo in self.__comodos)


# === Programa Menu Interativo ===
def menu():
    residencia = None

    while True:
        print("\n === MENU INTERATIVO ===")
        print("1. Criar nova residência")
        print("2. Adicionar cômodo")
        print("3. Exibir cômodos")
        print("4. Calcular área total")
        print("5. Sair")
        opcao = input("Informe a opção desejada: ")

        if opcao == "1":
            residencia = Residencia()
            print("Residência criada com sucesso.")

        elif opcao == "2":
            if residencia is None:
                print("Por favor, crie uma residência primeiro.")
            else:
                nome = input("Informe o nome do cômodo: ")
                try:
                    area = float(input("Informe a área do cômodo (em m²): "))
                    if area <= 0:
                        print("A área deve ser um número positivo.")
                    else:
                        residencia.adicionar_comodo(nome, area)
                        print("Cômodo adicionado com sucesso.")
                except ValueError:
                    print("Área inválida. Por favor, insira um número.")

        elif opcao == "3":
            if residencia is None:
                print("Por favor, crie uma residência primeiro.")
            else:
                residencia.exibir_comodos()

        elif opcao == "4":
            if residencia is None:
                print("Por favor, crie uma residência primeiro.")
            else:
                total = residencia.calcular_area_total()
                print(f"A área total da residência é: {total:.2f} m²")

        elif opcao == "5":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")


# Executa o menu
if __name__ == "__main__":
    menu()
