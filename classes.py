class Banco:
    def __init__(self, nome, cnpj, endereco):
        self.nome = nome
        self.cnpj = cnpj
        self.endereco = endereco
        self.clientes = [] 

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

class Cliente:
    def __init__(self, nome=None, rg=None):
        self.nome = nome
        self.rg = rg
        self.conta = None

    def criar_conta(self, saldo_inicial=0.0):
        self.conta = ContaBancaria(saldo_inicial)

    def deposito(self, valor):
        if self.conta:
            self.conta.deposito(valor)
        else:
            print("O cliente não possui uma conta bancária.")

    def saque(self, valor):
        if self.conta:
            self.conta.saque(valor)
        else:
            print("O cliente não possui uma conta bancária.")

    def transferencia(self, outra_conta, valor):
        if self.conta:
            self.conta.transferencia(outra_conta, valor)
        else:
            print("O cliente não possui uma conta bancária.")

class ContaBancaria:
    def __init__(self, saldo=0.0):
        self.saldo = saldo

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso. Saldo atual: R${self.saldo}")
        else:
            print("O valor do depósito deve ser maior que zero.")

    def saque(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso. Saldo atual: R${self.saldo}")
        else:
            print("Saldo insuficiente ou valor de saque inválido.")

    def transferencia(self, outra_conta, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            outra_conta.saldo += valor
            print(f"Transferência de R${valor} realizada com sucesso.")
        else:
            print("Saldo insuficiente ou valor de transferência inválido.")
