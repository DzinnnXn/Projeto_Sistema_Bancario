class Banco:
    def __init__(self, nome, cnpj, endereco):
        self.nome = nome
        self.cnpj = cnpj
        self.endereco = endereco      
        
class Cliente:
    def __init__(self):
        self.clientes = []

    def adicionar_cliente(self, nome, rg):
        self.clientes.append({"nome": nome, "rg": rg})

    def listar_clientes(self):
        for i, cliente in enumerate(self.clientes):
            i += 1
            print(f"Índice: {i}  |  Nome: {cliente['nome']}  |  Rg: {cliente['rg']}")
            
    def remover_cliente(self, indice):
        indice -= 1
        if indice < len(self.clientes):
            del self.clientes[indice]
            print("Cliente removido com sucesso")
        else:
            print("Não existe esse cliente")