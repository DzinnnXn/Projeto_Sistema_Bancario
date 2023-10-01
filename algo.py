import os
from classes import *
banco = Banco("Bradesco", 123456789, "Jundiaí - SP")
cliente = Cliente()

def pausar():
    os.system("pause")
    
def cls():
    os.system("cls")

def main():
    s = 0
    while s == 0:
        print("Bem-Vindo ao nosso Banco!!")
        print("[1] - Cadastrar Cliente")
        print("[2] - Excluir Cliente")
        print("[3] - Depositar")
        print("[4] - Saquar")
        print("[5] - Transferência")
        print("[6] - Visualizar Clientes")
        print("[7] - Sair")
        menu = int(input(">>"))
        match menu:
            case 1:
                cls()
                print("-------------------------")
                print("         CADASTRO        ")
                print("-------------------------")
                nome = input("Digite o nome do novo cliente: ")
                rg = input("Digite o rg do novo cliente: ")
                cliente.adicionar_cliente(nome, rg)
                print("Cliente cadastrado com sucesso.")
                pausar()
            
            case 2:
                cls()
                print("-------------------------")
                print("     EXCLUIR CLIENTE     ")
                print("-------------------------")
                cliente.listar_clientes()
                indice = int(input("Digite o indice no cliente que deseja remover \n>>"))
                cliente.remover_cliente(indice)
                pausar()
            
            case 3:
                cls()
                print("-------------------------")
                print("         DEPÓSITO        ")
                print("-------------------------")
                pausar()
            
            case 4:
                cls()
                print("-------------------------")
                print("         SAQUE           ")
                print("-------------------------")
                pausar()
            
            case 5:
                cls()
                print("-------------------------")
                print("     TRASNFERÊNCIA       ")
                print("-------------------------")
                pausar()
            
            case 6:
                cls()
                print("-------------------------")
                print("   VISUALIZAR CLIENTES   ")
                print("-------------------------")
                cliente.listar_clientes()
                pausar()
            
            case 7:
                cls()
                print("Saindo...")
                pausar()
                break