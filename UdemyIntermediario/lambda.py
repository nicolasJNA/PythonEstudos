"""Função 'invisivel' e toda ela deve ser contida numa unica expressão"""

lista = [
{'nome':'nicolas', 'idade':20},
{'nome': 'caleb', 'idade': 8},
{'nome':'luana', 'idade':21}
]

lista.sort(key=lambda valor: valor['nome'])
for item in lista:
    print(item)