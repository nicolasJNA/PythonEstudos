from functools import partial
from types import GeneratorType

def print_iter(iterador):
    print(*list(iterador),sep='\n')
    print()

def aumentar_preco(valor,porcentagem):
    return round(valor * porcentagem,2)



produtos = [
    {'nome':'Produto 1','preco':10},
    {'nome':'Produto 2','preco':12.7},
    {'nome':'Produto 3','preco':31},
    {'nome':'Produto 4','preco':9},
    {'nome':'Produto 5','preco':4.5},
]

aumentar_dez_porcento = partial(aumentar_preco, 1.1)

# novos_produtos = [
#     {**p,
#      'preco':aumentar_dez_porcento(p['preco'])
#      } 
#     for p in produtos
# ]
def muda_preco_de_produtos(produto):
    return {
        **produto,
        'preco': aumentar_dez_porcento(produto['preco']
        )
    }

novos_produtos = map(muda_preco_de_produtos,produtos)
novos_produtos = (p for p in produtos)
print_iter(produtos)
print_iter(novos_produtos)
print(novos_produtos)

print(hasattr(novos_produtos,'__iter__'))
print(type(range))

print(list(map(
    lambda x: x*3,[1,2,3,4]
)))