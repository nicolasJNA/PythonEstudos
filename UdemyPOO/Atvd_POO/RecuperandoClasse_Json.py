from SalvandoClasseEm_Json import CAMINHO_ARQUIVO
import json

with open(CAMINHO_ARQUIVO,'r') as arquivo:
    pessoa = json.load(arquivo)

    print(type(pessoa))
for person in pessoa:
    print('-'*20)
    for chave,valor in person.items():
        print(f'{chave}: {valor}')
print('-'*20)