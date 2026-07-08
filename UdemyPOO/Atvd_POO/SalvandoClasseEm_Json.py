import json
import os

class Pessoa:
    def __init__(self,nome,idade,cpf,telefones):
        self.nome = nome;
        self.idade = idade;
        self.cpf = cpf;
        self.telefones = telefones;

pessoa1 = Pessoa('Nicolas',22,'144,753.994-08',('81 955684122','81 968741332'))
pessoa2 = Pessoa('Angela',58,'365.887.415-85',('81 5879655','42 985874125'))
CAMINHO_ARQUIVO = 'UdemyPOO/Atvd_POO/SalvandoClasse_Json.Json'
pessoas = [vars(pessoa1),vars(pessoa2)]

if __name__ == '__main__':
    print('è o main')
    with open(CAMINHO_ARQUIVO,'w',encoding='utf8') as arquivo:
        json.dump(pessoas,arquivo,ensure_ascii=False,indent=2)

# os.remove('UdemyPOO/SalvandoClasse_Json.Json')