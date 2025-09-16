class Produto: 

  def __init__(self, __nome,__preço,__quantidade): 
    self.__nome = __nome
    self.__preço = __preço
    self.__quantidade = __quantidade 

  def getNome(self):
    return self.__nome

  def getPreço(self):
    return self.__preço

  def getQuantidade(self):
    return self.__quantidade

  def setNome(self, novoNome):
    self.__nome = novoNome
  
  def setPreço(self, novoPreço):
    self.__preço = novoPreço

  def setQuantidade(self, novaQuantidade):
    self.__quantidade = novaQuantidade

class CarrinhoDeCompras: 

  def __init__ (self):
    self.__produtos = []

  def adicionarProduto(self,produto): 
    self.__produtos.append(produto)

  def removerProduto(self,nome):
    for produto in self.__produtos:
      if produto.getNome() == nome:
        self.__produtos.remove(produto)
        print("Produto removido com sucesso!")
        return
    print("Produto não encontrado no carrinho!")

  def calculandoCompra(self):
    total = 0
    for produto in self.__produtos:
        total += produto.getPreço() * produto.getQuantidade()
    print(f"Total da compra: R$ {total:.2f}")


  def listarProdutos(self):
    if not self.__produtos:
      print("Carrinho vazio!")
    else: 
      print("Produtos no carrinho:")
      for produto in self.__produtos:
        print(f"-{produto.getNome()} | Quantidade: {produto.getQuantidade()}")


carrinho = CarrinhoDeCompras()
while True:
  print("---Menu---")
  print(" 1. Adicionar produto")
  print(" 2. Remover Produto")
  print(" 3. Calcular Compras")
  print(" 4. Listar Produtos")
  print(" 5. Sair") 
  
  op = input("Escolha uma opção: ")

  if op == "1":
    nome = input("Nome do produto: ")
    preco = float(input("Preço do produto: "))
    quantidade = int(input("Quantidade do produto: "))

    produto = Produto(nome, preco, quantidade)
    carrinho.adicionarProduto(produto)
    print(f"{nome} adicionado ao carrinho!")

  elif op == "2":
    nome = input("Nome do produto a remover: ")
    carrinho.removerProduto(nome)

  elif op == "3":
    carrinho.calculandoCompra()

  elif op == "4":
    carrinho.listarProdutos()


  elif op == "5": 
    print("Saindo..")
    break 
  
  else: 
    print("Opção inválida!")

