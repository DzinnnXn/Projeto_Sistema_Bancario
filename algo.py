import os
from classes import *

def pausar():
    os.system("pause")

def cls():
    os.system("cls")

def main():
    banco = Banco("Bradesco", 123456789, "Jundiaí - SP")
    
    s = 0
    while s == 0:
        print("Bem-Vindo ao nosso Banco!!")
        print("[1] - Cadastrar Cliente")
        print("[2] - Excluir Cliente")
        print("[3] - Depositar")
        print("[4] - Sacar")
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
                senha = input("Digite a senha do novo cliente: ")
                cliente_novo = Cliente(nome, rg, senha)
                cliente_novo.criar_conta()
                banco.adicionar_cliente(cliente_novo)
                print("Cliente cadastrado com sucesso.")
                pausar()

            case 2:
                cls()
                print("-------------------------")
                print("     EXCLUIR CLIENTE     ")
                print("-------------------------")
                banco.listar_clientes()
                indice = int(input("Digite o índice do cliente que deseja remover \n>>"))
                banco.remover_cliente(indice - 1)  # Ajuste para o índice começar em 1
                pausar()

            case 3:
                cls()
                print("-------------------------")
                print("         DEPÓSITO        ")
                print("-------------------------")
                banco.listar_clientes()
                indice = int(input("Digite o índice do cliente para fazer o depósito \n>>"))
                if 0 <= indice - 1 < len(banco.clientes):
                    valor = float(input("Digite o valor do depósito: "))
                    banco.clientes[indice - 1].conta.deposito(valor)
                else:
                    print("Índice de cliente inválido.")
                pausar()
                
            case 4:
                cls()
                print("-------------------------")
                print("         SAQUE           ")
                print("-------------------------")
                banco.listar_clientes()
                indice = int(input("Digite o índice do cliente para fazer o saque \n>>"))
                if 0 <= indice - 1 < len(banco.clientes):
                    valor = float(input("Digite o valor do saque: "))
                    banco.clientes[indice - 1].conta.saque(valor)
                else:
                    print("Índice de cliente inválido.")
                pausar()

            case 5:
                cls()
                print("-------------------------")
                print("     TRANSFERÊNCIA       ")
                print("-------------------------")
                banco.listar_clientes()
                indice_origem = int(input("Digite o índice do cliente de origem: "))
                indice_destino = int(input("Digite o índice do cliente de destino: "))
                if 0 <= indice_origem - 1 < len(banco.clientes) and 0 <= indice_destino - 1 < len(banco.clientes):
                    valor = float(input("Digite o valor da transferência: "))
                    banco.clientes[indice_origem - 1].conta.transferencia(banco.clientes[indice_destino - 1].conta, valor)
                else:
                    print("Índice de cliente inválido.")
                pausar()

            case 6:
                cls()
                print("-------------------------")
                print("   VISUALIZAR CLIENTES   ")
                print("-------------------------")
                banco.listar_clientes()
                pausar()

            case 7:
                cls()
                print("Saindo...")
                pausar()
                s = 1
                break