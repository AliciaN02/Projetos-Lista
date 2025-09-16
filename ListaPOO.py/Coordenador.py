class Coordenador(): 
    def __init__(self,nome,curso):
        self.nome = nome 
        self.curso = curso 

    def imprimirEmenta(self, disciplina):
        print(f"Curso: {self.curso}\nDisciplina: {disciplina.getNomeDisc()}\nEmenta: {disciplina.getEmenta()}\n Coordenador: {self.nome}")

class Disciplina(): 
    def __init__(self,nome, ementa): 
        self.nome = nome 
        self.ementa = ementa 

    def getEmenta(self):
        return self.ementa

    def getNomeDisc(self):
        return self.nome
       
cod1 = Coordenador("Cassia", "Engenharia de Software")
disciplina = Disciplina("POO", "Orientação a Objetos Python")

cod1.imprimirEmenta(disciplina)
