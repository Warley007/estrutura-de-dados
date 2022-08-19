import os
import Pilha

def menuSecundarioPilha():
    objetoPilha = Pilha.Pilha()
    operacaoSecundaria = ""
    while operacaoSecundaria != 6:
        os.system("cls")
        print("\t\t\tESTRUTURA DE DADOS PILHA\n")
        print("1 - Inserir um elemento na pilha")
        print("2 - Remover um elemento na pilha")
        print("3 - Econtrar a posição de um elemento dentro da pilha")
        print("4 - Buscar um determinado elemento na pilha")
        print("5 - Apagar a pilha")
        print("6 - Retornar ao menu principal")
        operacaoSecundaria = int(input("\nDigite o número da operacação que se deseja realizar na PILHA: "))
        
        if operacaoSecundaria == 1:
            os.system('cls')
            print("\t\t\tOpção inserir um elemento na pilha\n")
            elemento = int(input("\nDigite qual elemento vai ser adicionado na pilha: "))
            print(objetoPilha.inserePilha(elemento))
            print("\nPilha após operacação: ", end= "")
            objetoPilha.mostrar()
            input("\nPresione ENTER para continuar...")
        
        elif operacaoSecundaria == 2:
            os.system("cls")
            print("\t\t\tOpção remover um elemento na pilha")
            objetoPilha.mostrar()
            print(objetoPilha.removePilha())
            print("\nPilha após operacação: ", end = '')
            objetoPilha.mostrar()
            input("\nPresione ENTER para continuar...")
        
        elif operacaoSecundaria == 3:
            os.system("cls")
            print("\n\t\tOpção econtrar a posição de um elemento dentro da pilha")
            if objetoPilha.verificaPilhaVazia() == -1:
                print("\nErro: impossível executar operação em pilha vazia!")
            else:
                objetoPilha.mostrar()
                elemento = int(input("\nDigite o número a ser buscado na pilha: "))
                if objetoPilha.buscarPosicao(elemento) == 0:
                    print("\nElemento não pertence a pilha!")
                else:
                    print("\nO elemento está na posição", objetoPilha.buscarPosicao(elemento))
            
            input("\nPresione ENTER para continuar...")        
                
        
        elif operacaoSecundaria == 4:
            os.system("cls")
            print("\t\t\tOpção buscar um determinado elemento na pilha")
            if objetoPilha.verificaPilhaVazia() == -1:
                print("\nErro: impossível executar operação em pilha vazia!")
            else:
                objetoPilha.mostrar()
                elemento = int(input("\nDigite o número a ser buscado na pilha: "))
                if objetoPilha.buscaElemento(elemento) == None:
                    print("\nElemento não pertence a pilha!")
                else:
                    print("\nO elemento está na posição de memória", objetoPilha.buscaElemento(elemento))
            input("\nPresione ENTER para continuar...")
        
        elif operacaoSecundaria == 5:
            os.system("cls")
            print("\t\t\tOpção apagar pilha")
            if objetoPilha.verificaPilhaVazia() == -1:
                print("\nERRO: A pilha já está vazia!")
            else:           
                os.system("cls")
                print("\t\t\tOpção apagar a pilha")
                print(objetoPilha.apagarPilha())
            input("\nPresione ENTER para continuar...")
        
        elif operacaoSecundaria != 6:
            input("Opção inválida! Pressione ENTER para tentar novamente!")

