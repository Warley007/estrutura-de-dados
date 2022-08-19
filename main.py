import os
import menuSecundarioPilha
import menuSecundarioFila
import menuSecundarioLista

def menuPrincipal():
    operacaoPrincipal = ""
    while operacaoPrincipal != 0:
        os.system("cls")
        print("\t\t\tESTRUTURA DE DADOS")
        print("1 - PILHA")
        print("2 - FILA")
        print("3 - LISTA")
        print("0 - ENCERRAR O PROGRAMA")
        operacaoPrincipal = int(input("\nDigite o número da opção da estrutura de dados que se deseja trabalhar: "))
        
        if operacaoPrincipal == 1:
            menuSecundarioPilha.menuSecundarioPilha()
        elif operacaoPrincipal == 2:
            menuSecundarioFila.menuSecundarioFila()
        elif operacaoPrincipal == 3:
            menuSecundarioLista.menuSecundarioLista()
        elif operacaoPrincipal != 0:
            input("OPÇÃO INVÁLIDA! Pressione ENTER para continuar...")
menuPrincipal()
print("Programa encerrado!")