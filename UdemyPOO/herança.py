class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    def falar_nome_classe(self):
        print("Estou na classe Pessoa")
        print(f'{self.nome} {self.idade} ',self.__class__.__name__)
class Cliente(Pessoa):
    def falar_nome_classe(self):
        print("Eita. tenho o mesmo nome mas não passei na classe Pessoa")
        print(f'{self.nome} {self.idade} ',self.__class__.__name__)
class Aluno(Pessoa):
    ...

cliente = Cliente('Gael',20)
aluno = Aluno('Jonael',10)

aluno.falar_nome_classe()
cliente.falar_nome_classe()