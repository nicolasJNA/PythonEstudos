# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - Iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos

from itertools import combinations, permutations, product

def print_iter(iterador):
    print(*list(iterador),sep="\n")

pessoas = ['Joao','Jose','Josue','Josias']
camisas = [['Adidas','Polo','Ciclone'],['p','m','g']]

print_iter(combinations(pessoas,2))
print()
print_iter(permutations(pessoas,2))
print()
print_iter(product(*camisas))