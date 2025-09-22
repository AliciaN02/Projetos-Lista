class Documento:
    def __init__(self, titulo, conteudo):
        self.titulo = titulo
        self.conteudo = conteudo


class Impressora:
    def imprimir(self, documento):
        print("\n=== IMPRESSÃO ===")
        print(f"Título: {documento.titulo}")
        print(f"Conteúdo: {documento.conteudo}")
        print("=================\n")


documentos = []
impressora = Impressora()

while True:
    print("== MENU INTERATIVO ==")
    print("1. Criar documento")
    print("2. Visualizar conteúdo (imprimir)")
    print("3. Sair")

    op = input("Informe a opção desejada: ")

    if op == "1":
        titulo = input("Digite o título do documento: ")
        if any(doc.titulo == titulo for doc in documentos):
            print(f"O documento '{titulo}' já está armazenado!")
        else:
            conteudo = input("Digite o conteúdo do documento: ")
            documentos.append(Documento(titulo, conteudo))
            print(f"Documento '{titulo}' criado com sucesso!")

    elif op == "2":
        if not documentos:
            print("Nenhum documento criado ainda.")
        else:
            print("\nDocumentos disponíveis:")
            for i, doc in enumerate(documentos, start=1):
                print(f"{i}. {doc.titulo}")
            
            escolha = input("Escolha o número do documento para imprimir: ")
            if escolha.isdigit() and 1 <= int(escolha) <= len(documentos):
                impressora.imprimir(documentos[int(escolha) - 1])
            else:
                print("Opção inválida!")

    elif op == "3":
        print("Saindo...")
        break

    else:
        print("Opção inválida! Tente novamente.")
