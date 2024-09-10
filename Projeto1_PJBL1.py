import pickle
import os
from DequeVC import Deque

class compFerroviaria(Deque):
    def __init__(self, max_deque,nome_arquivo):
        super(max_deque)
        self.nome_arquivo = nome_arquivo

        if os.path.exists(nome_arquivo):
            self.carregar() # Carrega os dados do arquivo.
            print(f"Arquivo '{nome_arquivo}' carregado com sucesso.")
        else:
            print(f"Aviso: O arquivo '{nome_arquivo}' não foi encontrado. "
            "A composição foi inicializada vazia.")

            
    def salvar(self):
        # Método para salvar a composição ferroviária no arquivo associado.
        with open(self.nome_arquivo, 'wb') as f:
            pickle.dump(self, f)
            print(f"Composição salva no arquivo: {self.nome_arquivo}")

    def carregar(self):
    # Método para carregar a composição ferroviária do arquivo associado.
        with open(self.nome_arquivo, 'rb') as f:
            dados = pickle.load(f)
            self._data = dados._data
            self._size = dados._size
            self._front = dados._front
            self._top = dados._top
            print(f"Composição carregada do arquivo: {self.nome_arquivo}")




    def calcPesoTotal(self):
        pass

    def calcCompTotal(self):
        pass

    def calcPassageirosTotal(self):
        pass
    
    def calcCargaTotal(self):
        pass

class Vagao(compFerroviaria):
    def __init__(self, tam, comp):
        self.tam = tam
        self.comp = comp

    def imprime(self):
        print(f"Comprimento: {self.comprimento} m, Peso: {self.peso} toneladas") 

class Locomotiva(Vagao):
    def __init__(self, tam, comp, peso):    
        self.peso = peso
        super(tam, comp)
        
    def imprime(self):
        super.imprime()
        print("Tipo: Lococomotiva")
        print(f"Potência: {self.calculoPotencia} HP") 
        
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

    def imprime(self):
        super.imprime()

    def retornarPeso(self):
        if self.peso >= 80 and self.peso <= 100:
            return self.peso 
        else:
            print("Peso deve ser entre 80 e 100 toneladas.")
    
    def calcPesoCarga(self):
        peso_carga = 0.75 * self.peso
        return peso_carga
    
    # Contabiliza a carga transportada pela composição.
    def contar_carga_total(self):
        total_carga = 0
        for vagao in self._data: # Itera em todos os vagões (self._data herdado de Deque).
            if isinstance(vagao, Carga): # Se for vagão de carga
                total_carga += vagao.calcPesoCarga # contabiliza a carga (75% do peso)
        return total_carga 
    
class Passageiro:
    def __init__(self, tam, comp, peso):    
        self.peso = peso
        super(tam, comp)
        tam = 15
        
    def retornarPeso(self):
        if self.peso > 30 and self.peso < 50:
            return self.peso
        else:
            print("Peso deve ser entre 30 e 50 toneladas.") 
    
    def passageiros(self, passageiros):
        if passageiros > 30 and passageiros < 0:
            print("O número de passageiros não pode ultrapassar 30!")
        else:
            return passageiros
    
    def imprime(self):
        super.imprime()
