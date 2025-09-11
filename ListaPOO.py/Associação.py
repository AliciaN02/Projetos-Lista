class Professor: 
    def __init__(self, nome, disciplina=None): 
        self.nome = nome 
        self.disciplina = disciplina 

    def setDisciplina (self, novaDisciplina): 
        self.disciplina = novaDisciplina

    def exibir_dados(self): 
        print(f"Professor: {self.nome}")
        if self.disciplina:
         print(f"Disciplina: {self.nome}")
         print(f"Ementa: {self.disciplina.ementa}")
        else: 
            print("Professor não atribuído.")

class Disciplina: 
    def __init__(self, nome, ementa): 
        self.nome = nome 
        self.ementa = ementa 
    

dc1 = Disciplina("Python POO", "Herança, Polimorfismo")
prof = Professor ("Henrique")
prof.exibir_dados()
print()
prof.setDisciplina(dc1)
prof.exibir_dados()





           