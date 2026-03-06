

produtos = [
    {'nome':'Produto 1','preco':10},
    {'nome':'Produto 2','preco':12.7},
    {'nome':'Produto 3','preco':31},
    {'nome':'Produto 4','preco':9},
    {'nome':'Produto 5','preco':4.5},
]

# filtrado = [
#     p
#     for p in produtos
#     if p['preco'] > 10
# ]

#                       retorna no True
filtrado = filter(lambda p: p['preco']>10,produtos)
print(*filtrado,sep='\n')