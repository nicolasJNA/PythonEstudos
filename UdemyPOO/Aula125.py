# método de classe
# self será 'cls'

class Pessoa:
    ano = 2026

    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_da_classe(cls,nome):
        print('Hey')

    @classmethod
    def criar_com_50anos(cls,nome):
        return cls(nome,50 )

p1 = Pessoa('Jose',5)
p2 = Pessoa.criar_com_50anos('Angelico')
print(Pessoa.ano)

print(f'{vars(p1)}\n{vars(p2)}')

