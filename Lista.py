class NodoLista:
	def __init__(self, dado = 0, proximoLista = None):
		self.dado = dado
		self.proximoLista = proximoLista

class Lista:
    def __init__(self):
        self.cabeca = None
    
    def verificaListaVazia(self):
        if self.cabeca == None:
            return -1
    
    def mostrar(self):
        if self.verificaListaVazia() == -1:
            print("Lista vazia!")
        else:
            corrente = self.cabeca
            print("\nLista atual: ", end = '')
            while corrente.proximoLista != None:
                print("" + str(corrente.dado) + " -> ", end = '')
                corrente = corrente.proximoLista
            if corrente.proximoLista == None:
                print(corrente.dado)
    
    def insereInicio(self, novoDado):
        novoNodo = NodoLista(novoDado)
        novoNodo.proximoLista = self.cabeca
        self.cabeca = novoNodo
        return "\nElemento inserido com sucesso no início da lista!"
    
    def removeFinal(self):
        corrente = self.cabeca
        
        if corrente.proximoLista == None:
            self.cabeca = None
            return "\nÚltimo elemento removido com sucesso!"
        else:
            anterior = None
            while corrente.proximoLista !=  None:
                anterior = corrente
                corrente = corrente.proximoLista
        
            anterior.proximoLista = None
            return "\nÚltimo elemento removido com sucesso!"
            
    def inserirPosicao(self, elemento, posicao):
        novoNodo = NodoLista(elemento)
        corrente = self.cabeca
        pos = 1
        if posicao == 1:
            self.insereInicio(elemento)
        else:
            anterior = None
            while corrente.proximoLista != None:
                anterior = corrente
                corrente = corrente.proximoLista
                pos += 1
                if pos == posicao:
                    anterior.proximoLista = novoNodo
                    novoNodo.proximoLista = corrente
                    return "\nElemento inserido na posicao determinada!"
            
            if posicao > pos:
                corrente.proximoLista = novoNodo
                novoNodo.proximoLista = None
                return "\nElemento inserido na última posicao da lista!"
    
    def buscarPosicao(self, elemento):
        corrente = self.cabeca
        posicao = 1
        
        while corrente:
            if corrente.dado == elemento:
                return posicao
            else:
                posicao += 1
            corrente = corrente.proximoLista
        return -1
    
    def buscarElemento(self, elemento):
        corrente = self.cabeca
        while corrente and corrente.dado != elemento:
            corrente = corrente.proximoLista
        return corrente
    
    def removePosicao(self, elemento):
        corrente = self.cabeca
        if corrente.dado == elemento:
            self.cabeca = corrente.proximoLista
            return "\nElemento removido com sucesso!"
        else:
            posicaoMemoria = self.buscarElemento(elemento)
            if posicaoMemoria == None:
                return "\nElemento não pertence a lista!"
            else:
                while corrente.proximoLista != posicaoMemoria:
                    corrente = corrente.proximoLista
                corrente.proximoLista = posicaoMemoria.proximoLista
                return "\nElemento removido com sucesso!" 
    
    def apagaLista(self):
        while self.cabeca != None:
            self.removeFinal()
        return "\nLista apagada com sucesso!"
        