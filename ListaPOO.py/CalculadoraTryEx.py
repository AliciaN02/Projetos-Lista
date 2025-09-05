while True: 
    try: 
        print("\n ----- Calculadora -----")
        print(" 1. Soma")
        print(" 2. Subtração ")
        print(" 3. Multiplicação ")
        print(" 4. Divisão ")
        print(" 5. Sair ")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            n1 = float(input("Digite o primeiro número: "))
            n2 = float(input("Digite o segundo número: "))
            print("Resultado:", n1 + n2)

        elif opcao == 2: 
            n1 = float(input("Digite o primeiro número: "))
            n2 = float(input("Digite o segundo número: "))
            print("Resultado:", n1 - n2)

        elif opcao == 3:
            n1 = float(input("Digite o primeiro número: "))
            n2 = float(input("Digite o segundo número: "))
            print("Resultado:", n1 * n2)

        elif opcao == 4:
            n1 = float(input("Digite o primeiro número: "))
            n2 = float(input("Digite o segundo número: "))
            if n2 != 0:
                print("Resultado:", n1 / n2)
            else:
                print("Erro: não é possível dividir por zero!")

        elif opcao == 5:
            print("Saindo...")
            break

        else: 
            print("Opção inválida!")

    except Exception as erro:
        print(f"\nOcorreu um erro: {erro}")
