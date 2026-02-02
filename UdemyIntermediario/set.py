# conjuntos matematicos em python
# set é mutavel porem aceitam apenas tipos imutaveis
# como valor interno

# set(iteravel) ou set(1,2,3)
s1 = set() # vazio
lista = [1,2,3,1,1,2,2,2,3,4,1,2,3,4]
print(s1)
'''
Sets são eficientes para removerem valores duplicados de iteraveis
    - ão aceita valores mutáveis
    - seus valores sempre seram unicos
    - não tem indices
    - são iteraveis (for,in,not in)

Metodos uteis
add, update, clear, discard
'''

s1 = set('NICOLAS')
s1.add(8)
print(s1)
s1.update((8,5,2,'oi',))
print(s1)
s1.discard('oi')
print('O "oi" foi removido: ',s1)

'''
Operadores úteis:
União (union) - |
Intersecção - intersection &
Diferença simetrica ^ (não existe em ambos)
'''

s1 = {1,2,3}
s2 = {2,3,4}
s3 = s1|s2

print('União: ',s3)
s3 = s1 & s2
print('intersecção: ',s3)
s3 = s1 - s2
print('Diferença(s1-s2): ',s3)
s3 = s1 ^ s2
print('Diferença simetrica: ',s3)