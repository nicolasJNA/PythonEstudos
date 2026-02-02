'''
Docstring para Seção_DOIS.metodos_Dic

setdefault -  define um valor padrão
len - quantas chaves
values - iteravel com os valores
items  iteravel com chaves e valores
copy- retorna uma copia rasa (shallow copy)
get - obtem uma chave
pop - Apaga um item com uma chave especific (del)
popitem - Apaga o ultimo item adcionado
update- atualiza um dicionario com outro
'''

pessoa = {
    'nome':'nicolas',
    'idade':'20 anos'
}

# pessoa.setdefault('sobrenome','justo')
# print(pessoa['sobrenome'])
# #print(len(pessoa))
# #print(tuple(pessoa.keys()))
# #print(list(pessoa.values()))
# # print(list(pessoa.items()))

# # for chave in pessoa:
# #     print(chave)

# # for chave, valor in pessoa.items():
# #     print(chave, valor)
# import copy

# d1 ={
#     'c1':1,
#     'c2': 2,
#     'ls': [1,2,3,4,5]
# }
#copia rasa, elas apontam para a mesma lista (dado mutavel)
#d2 = d1.copy()

# copia profunda, não estão apontando para o mesmo dado na memoria,

# d2 = copy.deepcopy(d1)

# d2['ls'][0] = 1000 
# print(d1)
# print(d2)

pessoa.pop('nome')
pessoa.popitem()
print(pessoa)

pessoa.update(nome='nicolas',sobrenome='justo',idade='20',estado='Pernambuco')
print(pessoa.values())