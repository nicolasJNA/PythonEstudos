class Pessoa:
    def __init__(self, nome: str, idade: int)-> None:
        self.nome = nome
        self.idade = idade

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade

    @nome.setter
    def nome(self,nome: str):
        self._nome = nome

    @idade.setter
    def idade(self,idade: int):
        self._idade = idade

class Cliente(Pessoa):
    def __init__(self, nome: str, idade:int) -> None:
        super().__init__(nome, idade)
        self.conta = None



if __name__ == '__main__':
    cliente1 = Cliente('Nico',20)
    print(cliente1)
    print(cliente1.conta)