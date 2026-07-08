import json

# pessoa = {
#     'nome':'Nicolas',
#     'idade': 22,
#     'endereco': [
#         {'rua':'Frederico Evandro', 'numero':155},
#         {'rua':'Leonardo Coelho', 'numero':441},
#         ],
#         'altura':2.25,
#         'numero_da_sorte': (4,5,17,21),
#         'dev': 'no caminho',
#         'null':None,
# }

# with open('dado.json','w') as arquivo:
#     json.dump(pessoa,arquivo,
#     ensure_ascii=False,
#     indent=2)

with open('dado.json','r') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa)

print(type(pessoa))