"""
inteirando Strings com while
"""

#       012345678
nome = 'Nicolas J'
#       987654321
nome_novo = ''
cont = 0;
while cont < len(nome):
    letra = nome[cont]
    nome_novo += letra;
    cont += 1

print(nome_novo)
