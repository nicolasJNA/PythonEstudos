# __dict__ e vars para atributos de instancias
import os
class Pessoa:
    ano_atual = 2026

    def __init__(self,nome,idade):
        self.nome = nome;
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    
p1 = Pessoa('nicolas',22)
print(p1.__dict__)
print(vars(p1))