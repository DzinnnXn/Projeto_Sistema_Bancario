class ContaBancaria:
    def __init__(self, cliente, saldo_inicial=0.0):
        self.cliente = cliente
        self.saldo = saldo_inicial

    def deposito(self, valor):
        senha = input("Digite sua senha para confirmar o depósito: ")
        if senha == self.cliente.senha:
            if valor > 0:
                self.saldo += valor
                print(f"Depósito de R${valor} realizado com sucesso. Saldo atual: R${self.saldo}")
            else:
                print("O valor do depósito deve ser maior que zero.")
        else:
            print("Senha incorreta. Depósito não autorizado.")

    def saque(self, valor):
        senha = input("Digite sua senha para confirmar o saque: ")
        if senha == self.cliente.senha:
            if valor > 0 and valor <= self.saldo:
                self.saldo -= valor
                print(f"Saque de R${valor} realizado com sucesso. Saldo atual: R${self.saldo}")
            else:
                print("Saldo insuficiente ou valor de saque inválido.")
        else:
            print("Senha incorreta. Saque não autorizado.")

    def transferencia(self, outra_conta, valor):
        senha = input("Digite sua senha para confirmar a transferência: ")
        if senha == self.cliente.senha:
            if valor > 0 and valor <= self.saldo:
                self.saldo -= valor
                outra_conta.saldo += valor
                print(f"Transferência de R${valor} realizada com sucesso.")
            else:
                print("Saldo insuficiente ou valor de transferência inválido.")
        else:
            print("Senha incorreta. Transferência não autorizada.")

class Cliente:
    def __init__(self, nome, rg, senha):
        self.nome = nome
        self.rg = rg
        self.senha = senha
        self.conta = None  # A conta bancária associada a este cliente

    def criar_conta(self, saldo_inicial=0.0):
        self.conta = ContaBancaria(self, saldo_inicial)

class Banco:
    def __init__(self, nome, cnpj, endereco):
        self.nome = nome
        self.cnpj = cnpj
        self.endereco = endereco
        self.clientes = []  # Lista de clientes do banco

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    def listar_clientes(self):
        for i, cliente in enumerate(self.clientes):
            i += 1
            print(f"Índice: {i} | Nome: {cliente.nome} | RG: {cliente.rg} | Saldo: R${cliente.conta.saldo}")

    def remover_cliente(self, indice):
        if 0 <= indice < len(self.clientes):
            cliente_removido = self.clientes.pop(indice)
            print(f"Cliente {cliente_removido.nome} removido com sucesso.")
        else:
            print("Índice de cliente inválido.")