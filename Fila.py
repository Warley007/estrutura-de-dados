class NodoFila:
	def __init__(self, dado = 0, proximoFila = None):
		self.dado = dado
		self.proximoFila = proximoFila

class Fila:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
    
    def verificaFilaVazia(self):
        if self.primeiro == None:
            return -1
    
    def mostrar(self):
        if self.primeiro == None:
            print("\nFila vazia")
        else:
            corrente = self.primeiro
            print("\nFila atual: ", end = '')
            while corrente.proximoFila != None:
                print("" + str(corrente.dado) + " -> ", end = '')
                corrente = corrente.proximoFila
            if corrente.proximoFila == None:
                print(corrente.dado)
    
    def insereFila(self, novoDado):
        novoNodo = NodoFila(novoDado)
        if self.primeiro == None:
            self.primeiro = novoNodo
            self.ultimo = novoNodo
            return "\nElemento inserido com sucesso!"
        else:
            self.ultimo.proximoFila = novoNodo
            self.ultimo = novoNodo
            return "\nElemento inserido com sucesso!"
    
    def encontrarPosicao(self, valor):
        posicao = 1
        corrente = self.primeiro
        
        while corrente.proximoFila != None:
            if corrente.dado == valor:
                return posicao
            corrente = corrente.proximoFila
            posicao += 1
        
        if corrente.dado == valor:
            return posicao
        else:
            return -1
        return posicao
        
    def buscarElemento(self, valor):
        corrente = self.primeiro
        while corrente and corrente.dado != valor:
            corrente = corrente.proximoFila
        
        return corrente
    
    def removerFila(self):
        self.primeiro = self.primeiro.proximoFila
        
        if self.primeiro == None:
            self.ultimo = None
        return "\nPrimeiro elemento removido com sucesso!"
    
    def apagarFila(self):
        while self.primeiro != None and self.ultimo != None:
            self.removerFila()
        return "\nFila apagada com sucesso!"