import copy

from dados.produtos_modulo import produtos


# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
novos_produtos = [
    {**p, 'preco': round(p['preco']*1.1,2)}
    for p in copy.deepcopy(produtos)
]

print(*novos_produtos, sep='\n')
print()
# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
produtos_ordenados_reverso = sorted(
    copy.deepcopy(produtos), 
    key=lambda p: p['nome'],
    reverse=True
)
print(*produtos_ordenados_reverso, sep='\n')
print()
# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
produtos_ordenados = sorted(
    copy.deepcopy(produtos), 
    key=lambda p: p['nome'],
)
print(*produtos_ordenados, sep='\n')
print()
print(*produtos, sep='\n')
