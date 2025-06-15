"""
Fatiamento de strings
 0123456789
 Ola mundo
-9876543210
Fatiamentos [i:f:p] [::]
obs: a função len retorna o tamnaho da string
"""
nome = "Ola mundo"
"""iniciando do 0 até o tamanho da string de 1 em 1 character"""
print(nome[0:len(nome):1])
"""inciando do  0 até o 9 do lado oposto"""
print(nome[::-1])