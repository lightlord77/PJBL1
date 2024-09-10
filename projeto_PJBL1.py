https://prod.liveshare.vsengsaas.visualstudio.com/join?FE0EB4ADA27A3DCA1D7A9D04DF3F7A413BF3

#-- coding: latin-1 --
class Except(Exception):
    """Tratamento de exceção. Uso: em raise Except(<mensagem>)."""
    pass
"""
Classe Deque: implementação utilizando lista/vetor estático circular.
"""
class Deque:
    def __init__ (self,max_deque):
        """Cria novo deque como lista de tamanho fixo: vetor estático."""
        self.max_deque=max_deque # Tamanho máximo do deque.
        self._data=[None]*max_deque # Lista de tamanho máximo N.
        self._size=0 # Tamanho corrente do deque.
# Frente (início) do deque: é decrementado/incrementado a cada
# addFirst()/deleteFirst(), respectivamente.
        self._front=0 # Posição inicial da frente/início.
# Top (final) do deque: é incrementado/decrementado a cada
# addLast()/deleteLast(), respectivamente.
        self._top=0 # Posição corrente do topo/fim.
# Ponteiro utilizado para percorrer o deque.
        self._ptr=0 # Posição do ponteiro no deque (0 no início).

        
    def is_empty(self):
        """Retorna verdadeiro se o deque estiver vazio."""
        return self._size==0
    

    def is_full(self):
        """Retorna verdadeiro se o deque estiver cheio."""
        return self._size==self._max_deque
    

    def get_size(self):
        """Retorna o tamanho no deque."""
        return self._size
    
    
    def peek(self):
        """Retorna elemento no início do deque sem removê-lo.
Retorna None se o deque estiver vazio."""
        if self.is_empty( ):
            return None
        else:
            return self._data[self._front] # Primeiro item do deque.
        
        
    def top(self):
        """Retorna elemento no fim do deque sem removê-lo.
Retorna None se o deque estiver vazio."""
        if self.is_empty( ):
            return None
        else:
            return self._data[self._top] # Último item do deque.
        
        
    def __str__(self):
        """Se o deque estiver vazio,
retorna mensagem de aviso;
senão,
monta uma lista temporária usando rewind e next para percorrer
o deque inserir (lista_temp.append()) cada um de seus elementos
nesta lista. Usa contador para controlar a inserção dos elementos
do deque sem excer o tamanho dele.
Usa str(lista_temp) para retornar o string do deque."""
        if self.is_empty( ):
            return "Deque vazio."
        else:
            lista_temp=[]
            strSize=0
            self.rewind()
            while strSize<self._size:
                lista_temp.append(self.next())
                strSize+=1
            return str(lista_temp)
        
        
    def getVC(self):
        """Se o deque estiver vazio,
retorna mensagem de aviso;
senão,
retorna a string do vetor circular (str(lista)) com os elementos
do deque "circulados"."""
        if self.is_empty( ):
            return "Vetor vazio."
        else:
            return str(self._data)
        

    def rewind(self):
        """Coloca ponteiro no início do deque."""
        self._ptr=self._front

        
    def next(self):
        """Se lista vazia,
retorna None;
senão,
guarda o elemento no ponteiro e passa o ponteiro para o próximo
elemento da deque, circulando se necessário. Retorna o elemento
guardado."""
        if self.is_empty():
            return None
        else:
            e=self._data[self._ptr]
            self._ptr+=1
        if self._ptr==self._max_deque: # Passou o fim da deque?
            self._ptr=0 # Circula.
            return e
        
        
    def addFirst(self,e):
        if self.is_full():
            raise Except("Deque cheio!")
        if self.is_empty():
            self._data[self._front]=e
        else:
            self._front-=1
            if self._front==-1: # Passou o início do vetor?
                self._front=self._max_deque-1 # Circula.
            self._data[self._front]=e # Item adicionado no fim do vetor.
        self._size+=1

        
    def addLast(self,e):
        if self.is_full():
            raise Except("Deque cheio!")
        if self.is_empty():
            self._data[self._front]=e
        else:
            self._top+=1
            if self._top==self._max_deque: # Passou o fim do vetor?
                self._top=0 # Circula.
            self._data[self._top]=e # Item adicionado no topo/fim do deque.
        self._size+=1
    
    
    def deleteFirst(self):
        if self.is_empty( ):
            raise Except('Deque cheio!')
        else:
            e_front=self._data[self._front] # Primeiro do deque.
            self._data[self._front]=None # Limpa posição.
            self._size-=1
            self._front+=1
            if self._front==self._max_deque: # Passou o fim do vetor?
                self._front=0 # Circula.
            return e_front
    
    
    def deleteLast(self):
        if self.is_empty( ):
            raise Except('Deque vazio!')
        else:
            e_top=self._data[self._top] # Último do deque.
            self._data[self._top]=None # Limpa posição.
            self._size-=1
            self._top-=1
            if self._top==-1: # Passou o início do vetor?
                self._top=self._max_deque-1 # Circula.
            return e_top
        
    


