# reduce faz a redução iteravel em vum valor
from functools import reduce

produtos = [
    {'nome':'Produto 1','preco':10},
    {'nome':'Produto 2','preco':12.7},
    {'nome':'Produto 3','preco':31},
    {'nome':'Produto 4','preco':9},
    {'nome':'Produto 5','preco':4.5},
]

# def funcao_reduce(acumulador,produto):
#     print('acumulador',acumulador)
#     print('produto', produto)
#     return acumulador + produto['preco']


total = reduce(
    lambda ac, p: ac + p['preco'],
    produtos,
    0
)
print(f'meu total é {total}')
# for i in produtos:
#     total += i['preco']

# print(sum(p['preco'] for p in produtos))