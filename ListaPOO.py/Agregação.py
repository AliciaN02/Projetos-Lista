class Funcionário: 
    def __init__(self, nome, ferramentas): 
        self.nome = nome 
        self.ferramentas = ferramentas
    
    def exibir_info(self):
        print(f"Funcionario: {self.nome}")
        print("Ferramentas: ") 
        for f in self.ferramentas: 
            print(f"{f.nome} - {f.ação()}")      

class Ferramentas():
    def __init__(self, nome, açãoFerramenta):
        self.nome = nome 
        self.açãoFerramenta = açãoFerramenta

    def ação(self):
        return f"{self.nome}, faz: {self.açãoFerramenta}"

listaFerramentas = [Ferramentas("Furadeira", "Fura"), Ferramentas("Martelo", "Bater")]
f1 = Funcionário("Fulano", listaFerramentas)
f1.exibir_info()
                    
