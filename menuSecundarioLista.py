import os
import Lista
def menuSecundarioLista():
    objetoLista = Lista.Lista()
    operacaoSecundaria  = ""
    
    while operacaoSecundaria != 8:
        os.system('cls')
        print("\t\t\tESTRUTURA DE DADOS LISTA\n")
        print("1 - Inserir um elemento no início da lista")
        print("2 - Remover um elemento na final da lista")
        print("3 - Inserir um elemento em determinada posição da lista")
        print("4 - Encontrar a posição de um elemento dentro da lista")
        print("5 - Buscar um determinado elemento na lista")
        print("6 - Remover um elemento da lista")
        print("7 - Apagar a lista (apagar todos os elementos)")
        print("8 - Retornar ao menu principal")
        
        operacaoSecundaria = int(input("\nDigite o número da operacação que se deseja realizar na LISTA: "))  

        if operacaoSecundaria == 1:
            os.system('cls')
            print("\t\t\tOpção inserir elemento no início da lista\n")
            elemento = int(input("\nDigite um número para ser inserido na lista: "))
            print(objetoLista.insereInicio(elemento))
            objetoLista.mostrar()
            input("\nPresione ENTER para continuar...")
        
        elif operacaoSecundaria == 2:
            os.system('cls')
            print("\t\t\tOpção remover um elemento na final da lista")
            if objetoLista.verificaListaVazia() == - 1:
                print("\nA lista está vazia")
            else:
                print(objetoLista.removeFinal())
                objetoLista.mostrar()
            input("\nPressione ENTER para continuar...")
        
        elif operacaoSecundaria == 3:
            os.system('cls')
            print("\t\t\tOpção inserir um elemento em determinada posição da lista")
            elemento = int(input("\nQual número vai ser adicionado na lista: "))
            if objetoLista.verificaListaVazia() == -1:
                print("A lista está vazia. Elemento vai ser adicionado na primeira posicao")
                objetoLista.insereInicio(elemento)
            else:
                posicao = int(input("\nQual a posição que o elemento vai ser inserido: "))
                print(objetoLista.inserirPosicao(elemento, posicao))
                objetoLista.mostrar()
            input("\nPressione ENTER para continuar...")
                    
        elif operacaoSecundaria == 4:
            os.system('cls')
            print("\t\t\tOpção encontrar a posição de um elemento dentro da lista")
            if objetoLista.verificaListaVazia() == -1:
                print("\nA lista está vazia")
            else:
                objetoLista.mostrar()
                elemento = int(input("\nQual o elemento a ser buscado: "))
                if objetoLista.buscarPosicao(elemento) == -1:
                    print("\nERRO: elemento não pertence a lista!")
                else:
                    print("\nO elemento " +str(elemento) + " está na posição " + str(objetoLista.buscarPosicao(elemento)))
            input("\nPressione ENTER para continuar...")
                 
        elif operacaoSecundaria == 5:
            os.system('cls')
            print("\t\t\tOpção buscar um determinado elemento na lista")
            if objetoLista.verificaListaVazia() == - 1:
                print("\nA lista está vazia")
            else:
                objetoLista.mostrar()
                elemento = int(input("\nQual elemnto a ser buscado: "))
                if objetoLista.buscarElemento(elemento) == None:
                    print("\nERRO: elemento não pertence a lista!")
                else:
                    print("\nO elemento " +str(elemento) + " está na posição de memória " + str(objetoLista.buscarElemento(elemento)))
            input("\nPressione ENTER para continuar...")
        
        elif operacaoSecundaria == 6:
            os.system("cls")
            print("\t\t\tOpção remover um elemento da lista")
            if objetoLista.verificaListaVazia() == - 1:
                print("a lista está vazia")
            else:
                objetoLista.mostrar()
                elemento = int(input("\nQual elemento será removido da lista: "))
                if objetoLista.buscarElemento(elemento) == None:
                    print("\nERRO: elemento não pertence a lista!")
                else:
                    print(objetoLista.removePosicao(elemento))
                    objetoLista.mostrar()
            input("\nPressione ENTER para continuar...")
            
        elif operacaoSecundaria == 7:
            os.system("cls")
            print("\t\t\tOpção apagar a lista (apagar todos os elementos)")
            if objetoLista.verificaListaVazia() == - 1:
                print("\nA lista já está vazia")
            else:
                print(objetoLista.apagaLista())
            input("\nPressione ENTER para continuar...")
        elif operacaoSecundaria != 8:
            input("Opção inválida! Pressione ENTER para tentar novamente...")
    