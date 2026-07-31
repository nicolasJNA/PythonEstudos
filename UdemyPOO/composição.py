class Cliente:
    def __init__(self, nome):
        self.nome =nome
        self.enderecos =  []

    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))

    def listar_enderecos(self):
        print(*[f'{p.rua} {p.numero}' for p in self.enderecos], sep='\n')

    def __del__(self):
        print("apagando ", self.nome)

class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua 
        self.numero = numero

    def __del__(self):
        print("apagando",self.numero,self.rua)

cliente1 = Cliente('Maria')
cliente1.inserir_endereco('Alvares',23)
cliente1.inserir_endereco('Tavon',2)
cliente1.listar_enderecos()

del cliente1

print("######CODIGO ACABOU######")
#garbage colector é usado quando encerra o codigo
