# Criando um exemplo de agregação com carrinho de compras e produto

class Carrinho:
    def __init__(self):
        self._produtos = []

    def total(self):
        if self._produtos:
                return sum([p.preco for p in self._produtos]) 
        else:
            print("Carrinho vazio")

    def inserir(self,*produtos):
        for produto in produtos:
            self._produtos.append(produto)

    def listar(self):
        if self._produtos:
            print(*[f"{p.nome} R${p.preco:.2f}" for p in self._produtos], sep='\n')

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

carrinho = Carrinho()
p1,p2 = Produto('pao',2), Produto('pera',5)
carrinho.inserir(p1,p2)
carrinho.listar()
print(carrinho.total())