# Manipulando dados do dicionario

pessoa = {}

chave = 'nome'

pessoa[chave] = 'Nicolas'
pessoa['sobrenome'] = 'justo'

print(pessoa)
print(pessoa[chave])

pessoa[chave] = 'Caleb'

del pessoa['sobrenome']

print(pessoa)

if pessoa.get('sobrenome'):
    print('EXISTE')
