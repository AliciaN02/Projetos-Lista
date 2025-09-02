from abc import ABC , abstractmethod

class ClubeParticipante (ABC): 
    def __init__ ( self, nome, pais, confederação, rankingFifa, golsMarcados, vitorias): 
        self.nome = nome 
        self.pais = pais 
        self.confederação = confederação 
        self. rankingFifa = rankingFifa
        self.golsMarcados = golsMarcados
        self. vitorias = vitorias 

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"País: {self.pais}")
        print(f"Confederação: {self.confederação}")
        print(f"Ranking FIFA: {self.rankingFifa}")
        print(f"Gols Marcados: {self.golsMarcados}")
        print(f"Vitórias: {self.vitorias}")

    @abstractmethod
    def calcularDesempenho(self):
       pass
    
    def gerarRelatorioTecnico(self):
        pass

class UEFA (ClubeParticipante):
     def calcularDesempenho(self):
        return (self.vitorias * 3 + self.golsMarcados)* 0.5
     
     def gerarRelatorioTecnico(self):
         print(f"Relatorio Técnico do Clube UEFA {self.nome}:")
         self.exibir_dados()
         print(f"Desempenho: {self.calcularDesempenho()}")
        

class CONMEBOL (ClubeParticipante):
     def calcularDesempenho(self):
        return (self.vitorias * 3 + self.golsMarcados)* 0.7
     
     def gerarRelatorioTecnico(self):
         print(f"Relatorio Técnico do Clube CONMEBOL {self.nome}:")
         self.exibir_dados()
         print(f"Desempenho: {self.calcularDesempenho()}")
             
timeUEFA = UEFA ("Time UEFA", "França", "UEFA", 1, 30,10)
timeUEFA.gerarRelatorioTecnico()

timeCONMEBOL = CONMEBOL ("Time CONMEBOL", "Brasil", "CONMEBOL", 2,25,8)
timeCONMEBOL.gerarRelatorioTecnico()