"""
split e join com list e str
split - divide uma string
join - une uma string
"""


frase = ' Hello world como eu serei executado '

lista_palavras = frase.split(' ') 
#divide transformadno numa lista, o espaço é feito na virgula

for i,frase in enumerate(lista_palavras):
    lista_palavras[i] = lista_palavras[i].strip()

frase_nova = '-'.join(lista_palavras)
print(frase_nova)
