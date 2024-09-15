import pickle
import os
from DequeVC import Deque

class compFerroviaria(Deque):
    def __init__(self, max_deque,Comp_Fer):
        super().__init__(max_deque)
        self.Comp_Fer = Comp_Fer
        
        if os.path.exists(Comp_Fer):
            self.carregar() # Carrega os dados do arquivo.
            print(f"Arquivo '{Comp_Fer}' carregado com sucesso.")
        else:
            print(f"Aviso: O arquivo '{Comp_Fer}' não foi encontrado. A composição foi inicializada vazia.")

            
    def salvar(self):
        with open(self.Comp_Fer, 'wb') as arquivo: # Abre o arquivo no modo binário.
            pickle.dump(self._data, arquivo) # Serializa a lista atual e salva no arquivo.
            print(f"Composição salva no arquivo: {self.Comp_Fer}")

        
    def add_objeto(self, objeto):
        self._data.append(objeto)
        self.salvar()
        
    def carregar(self):
    # Método para carregar a composição ferroviária do arquivo associado.
        with open(self.Comp_Fer, 'rb') as f:
            dados = pickle.load(f)
            self._data = dados.data
            self._tam = dados.tam
            self._comp = dados.comp
            self.peso = dados.peso
        print(f"Composição carregada do arquivo: {self.Comp_Fer}")

    def calcPesoTotal(self):
        peso_total=0
        for vagao in self._data:
            peso_total+=vagao.peso
        return peso_total

    def calcCompTotal(self):
        comp_total=0
        for vagao in self._data:
            comp_total+=vagao.comp
        return comp_total

    def contar_passageiros_total(self):
        total_passageiros = 0
        for vagao in self._data: # Itera em todos os vagões (self._data herdado de Deque).
            if isinstance(vagao, Passageiro): # Se for vagão de passageiro
                total_passageiros += vagao.passageiros # contabiliza todos os passageiros por composição (tamanho total)
        return total_passageiros
    
    # Contabiliza a carga transportada pela composição.
    def contar_carga_total(self):
        total_carga = 0
        for vagao in self._data: # Itera em todos os vagões (self._data herdado de Deque).
            if isinstance(vagao, Carga): # Se for vagão de carga
                total_carga += vagao.calcPesoCarga # contabiliza a carga (75% do peso)
        return total_carga
    
    # Contabiliza a potência total pela composição.
    def contar_potencia_total(self):
        total_potencia = 0
        for vagao in self._data: # Itera em todos os vagões (self._data herdado de Deque).
            if isinstance(vagao, Locomotiva): # Se for vagão de locomotiva
                total_potencia += vagao.calculoPotencia 
        return total_potencia

class Vagao(compFerroviaria):
    def __init__(self, comp, peso):
        self.comp = comp
        self.peso = peso

    def imprime(self):
        print(f"Comprimento: {self.comp} m, Peso: {self.peso} toneladas") 

class Locomotiva(Vagao):
    def __init__(self, peso):    
        super().__init__(20, peso)
        self.peso = peso
        
    def imprime(self):
        super().imprime()
        print("Tipo: Locomotiva")
        print(f"Potência: {self.calculoPotencia()} HP")
        
    def retornarPeso(self):
        if self.peso > 100 and self.peso < 200:
            return self.peso 
        else:
            print("Peso deve ser entre 100 e 200 toneladas.")
    
    def calculoPotencia(self):
        potencia = 2000 + (8000 / 100) * (self.peso - 100)
        return potencia
    
    

        
class Carga(Vagao):
    def __init__(self, peso):    
        super().__init__(18, peso)
        self.peso = peso

    def imprime(self):
        super().imprime()
        print("Tipo: Carga")
        print(f"Carga: {self.calcPesoCarga}")

    def retornarPeso(self):
        if self.peso >= 80 and self.peso <= 100:
            return self.peso 
        else:
            print("Peso deve ser entre 80 e 100 toneladas.")
    
    def calcPesoCarga(self):
        peso_carga = 0.75 * self.peso
        return peso_carga
    
    
    
class Passageiro(Vagao):
    def __init__(self, peso, passageiros):    
        super().__init__(15, peso)
        self.peso = peso
        self.passageiros = self.verifica_passageiros(passageiros)
               
    def retornarPeso(self):
        if self.peso > 30 and self.peso < 50:
            return self.peso
        else:
            print("Peso deve ser entre 30 e 50 toneladas.") 
    
    def verifica_passageiros(self, passageiros):
        if passageiros > 30 or passageiros < 0:
            print("O número de passageiros não pode ultrapassar 30 nem ser menor que 0!")
            return 0  # Retorna 0 se o número de passageiros for inválido.
        else:
            return passageiros
        
    
    
    def imprime(self):
        super().imprime()
        print("Tipo: Passageiro")
        print(f"Número de passageiros: {self.passageiros}")

def menu():
    print('=============== Escolha a opção desejada ===============')
    print('< 1 > Inserir vagão')
    print('< 2 > Remover vagão')
    print('< 3 > Mostrar número de vagões na Composição Ferroviária')
    print('< 4 > Mostrar peso total da Composição Ferroviária')
    print('< 5 > Mostrar comprimento total da Composição Ferroviária')
    print('< 6 > Mostrar número total de Passageiros')
    print('< 7 > Mostrar e verificar potência do vagão')
    print('< 8 > Mostrar dados de um vagão')
    print('< 0 > Sair')
    print('========================================================')

    opcao = int(input('Digite a opção desejada: '))

    return opcao

def adicionar_vagao(composicao):
    print("Escolha o tipo de vagão:")
    print("< 1 > Locomotiva")
    print("< 2 > Passageiro")
    print("< 3 > Carga")
    
    tipo_vagao = int(input('Digite o tipo de vagão desejado: '))
    if tipo_vagao == 1:
        peso = float(input('Digite o peso da locomotiva: '))
        vagao = Locomotiva(peso)
        
    elif tipo_vagao == 2:
        peso = float(input('Digite o peso do vagão de passageiro: '))
        passageiros = int(input('Digite o número de passageiros: '))
        vagao = Passageiro(peso, passageiros)
        
    elif tipo_vagao == 3:
        peso = float(input('Digite o peso do vagão de carga: '))
        vagao = Carga(peso)
        
    else:
        print("Tipo de vagão inválido.")
        return
    composicao.add_objeto(vagao)
    
    print("Vagão adicionado com sucesso!")
    

    
    
composicao = compFerroviaria(10,'dados.pkl')
    
    
terminou = 1
while terminou == 1:
    op = menu()
    if op == 0:  # Caso o usuário selecione a opção 0!
        print('Encerrando o programa...')
        exit()
    elif op == 1:
        print("Inserir vagão")
        adicionar_vagao(composicao)
        menu()
    elif op == 2:
        print("Remover vagão")
        menu()
    elif op == 3:
        print("Número de vagões na Composição Ferroviária")
        menu()
    elif op == 4:
        print("Peso total da Composição Ferroviária")
        compFerroviaria.calcPesoTotal()
        menu()
    elif op == 5:
        print("Comprimento total da Composição Ferroviária")
        compFerroviaria.calcCompTotal()
        menu()
    elif op == 6:
        print("Número total de Passageiros")
        compFerroviaria.contar_passageiros_total()
        menu()
    elif op == 7:
        print("Potência do vagão:")
        
        menu()
    elif op==8:
        print("Dados de um vagão")
        compFerroviaria.carregar()
        menu()
    else:
        print("Digite um número entre 0 e 8")
        terminou=0
    
vagao_locomotiva01 = Locomotiva(100)
vagao_passageiro02 = Passageiro(30,20)
vagao_carga03 = Carga(80)



vagao_locomotiva01.add_objeto()
vagao_locomotiva01.imprime()
vagao_passageiro02.imprime()


    

vagao_locomotiva01 = Locomotiva(peso=100)  # Cria um objeto Locomotiva
composicao.add_objeto(vagao_locomotiva01)
