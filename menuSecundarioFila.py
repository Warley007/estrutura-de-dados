import os
import Fila
def menuSecundarioFila():
    objetoFila = Fila.Fila()
    operacaoSecundaria = ""
    while operacaoSecundaria != 6:
        os.system("cls")
        print("\t\t\tESTRUTURA DE DADOS FILA\n")
        print("1 - Inserir um elemento na fila")
        print("2 - Econtrar a posição de um elemento dentro da fila")
        print("3 - Buscar um determinado elemento na fila")
        print("4 - Remover um elemento da fila")
        print("5 - Apagar a fila")
        print("6 - Retornar ao menu principal")
        operacaoSecundaria = int(input("\nDigite o número da operacação que se deseja realizar na FILA: "))
        
        if operacaoSecundaria == 1:
            os.system("cls")
            print("\t\t\tOpção inserir um elemento na fila")
            elemento = int(input("\nDigite o número a ser inserido na fila: "))
            print(objetoFila.insereFila(elemento))
            objetoFila.mostrar()
            input("\nPressione ENTER para continuar...")
            
        elif operacaoSecundaria == 2:
            os.system("cls")
            print("\t\t\tOpção encontrar a posição de um elemento dentro da fila")
            if objetoFila.verificaFilaVazia() == -1:
                print("\nA fila está vazia!")
            else:
                objetoFila.mostrar()
                elemento = int(input("\nQual número vai ser buscado: "))
                if objetoFila.encontrarPosicao(elemento) == -1:
                    print("\nElemento não pertence a fila!")
                else:
                    print("\nElemento está na posição", objetoFila.encontrarPosicao(elemento))
            input("\nPressione ENTER para continuar...")
            
        elif operacaoSecundaria == 3:
            os.system("cls")
            print("\t\t\tOpção buscar um determinado elemento na fila")
            if objetoFila.verificaFilaVazia() == -1:
                print("\nA fila está vazia!")
            else:
                elemento = int(input("\nQual número vai ser buscado: "))
                if objetoFila.buscarElemento(elemento) == -1:
                    print("\nElemento não pertence a fila!")
                else:
                    if objetoFila.buscarElemento(elemento) == None:
                        print("\nERRO: elemento não pertence a fila")
                    else:
                        print("\nElemento está na posição de memória", objetoFila.buscarElemento(elemento))
            input("\nPressione ENTER para continuar...")
            
        elif operacaoSecundaria == 4:
            os.system("cls")
            print("\t\t\tOpção remover um elemento da fila")
            if objetoFila.verificaFilaVazia() == -1:
                print("\nA fila está vazia!")
            else:
                objetoFila.mostrar()
                print(objetoFila.removerFila())
                objetoFila.mostrar()
            input("\nPressione ENTER para continuar...")
        
        elif operacaoSecundaria == 5:
            os.system("cls")
            print("\t\t\tApagar a fila")
            if objetoFila.verificaFilaVazia() == -1:
                print("\nA fila já está vazia!")
            else:
                print(objetoFila.apagarFila())
            input("\nPressione ENTER para continuar...")
        elif operacaoSecundaria != 6:
            input("\nOpção inválida! Pressione ENTER para tentar novamente...")