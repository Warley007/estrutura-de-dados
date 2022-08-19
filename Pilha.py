class NodoPilha():
    def __init__(self, dado = 0, anteriorNodo = None):
        self.dado = dado
        self.anteriorNodo = anteriorNodo

class Pilha:
    def __init__(self):
        self.topo = None
    
    def verificaPilhaVazia(self):
        if self.topo == None:
            return -1

    def mostrar(self):
        if self.verificaPilhaVazia() == -1:
            print("Pilha vazia")
        else:
            corrente = self.topo
            while corrente.anteriorNodo != None:
                print ("\n\t" + str(corrente.dado))
                print ("\t|")
                corrente = corrente.anteriorNodo
            if corrente.anteriorNodo == None:
                print ("\t" + str(corrente.dado))
        
    def inserePilha(self, novoDado):
        novoNodo = NodoPilha(novoDado)
        novoNodo.anteriorNodo = self.topo
        self.topo = novoNodo
        return "\nElemento inserido com sucesso!" 
    
    def removePilha(self):  
        if self.verificaPilhaVazia() == -1:
            return "\nErro: Impossível executar operação em pilha vazia"
        else:
            self.topo = self.topo.anteriorNodo
            return "\nÚltimo elemento removido com sucesso"
            
    def buscarPosicao(self, elemento):
        corrente = self.topo
        i = 1
        while corrente.anteriorNodo != None:
            if corrente.dado == elemento:
                return i
            i += 1
            corrente = corrente.anteriorNodo        
        if corrente.anteriorNodo == None and corrente.dado == elemento:
            return i
        else:
            return 0
    
    def buscaElemento(self, valor):
        corrente = self.topo
        while corrente and corrente.dado != valor:
            corrente = corrente.anteriorNodo
        
        return corrente
  
    def apagarPilha(self): 
        if self.verificaPilhaVazia() == -1:
            return "\nA pilha já está vazia!"
        else:   
            while self.topo != None:
                self.removePilha()
            return "\nPilha apagada com sucesso!"