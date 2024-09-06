import pickle
from DequeVC import Deque

class compFerroviaria(Deque):
    def __init__(self, max_deque):
        super(max_deque)
    
        
    


class Vagao:
    def __init__(self, tam, comp):
            self.tam = tam
            self.comp = comp


class Locomotiva(Vagao):
    def __init__(self, tam, comp, peso):    
        self.peso = peso
        super(tam, comp)
        
    def retornarPeso(self):
        if self.peso > 100 and self.peso < 200:
            return self.peso 
        else:
            print("Peso deve ser entre 100 e 200 toneladas.")
    
    def calculoPotencia(self):
        potencia = 50*self.peso
        return potencia
        
class Carga(Vagao):
    def __init__(self, tam, comp, peso):    
        self.peso = peso
        super(tam, comp)
        tam = 18
        

        
    
class Passageiro:
    def __init__(self, tam, comp, peso):    
        self.peso = peso
        super(tam, comp)
        tam = 15
        
    def retornarPeso(self, peso,p):
        if peso > 30 and peso < 50:
            
            return peso
        else:
            print("Peso deve ser entre 30 e 50 toneladas.") 
        
        
            
