import pprint

produto = {
    'nome':'Bombagoingo',
    'preco':1000,
    'categoria':'Brinquedo',
}

dc= {
    chave: valor.upper()
    if isinstance(valor,str) else valor
    for chave, valor in produto.items()
    }

pprint.pprint(dc,width=40,sort_dicts=False)

s1 = { num for num in range(10)}
print(type(s1))