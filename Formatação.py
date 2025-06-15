#formatação tipo interpolação
nome = 'nicolas'
preco = 1234.988839
variavel = '%s o valor é %.2f' % (nome,preco)
print(variavel)
#usando f''
print(f'{nome} tem {preco:.2f} na conta')
#us
tudo = '{} na verdade é {:.2f}'.format(nome,preco)
print(tudo)