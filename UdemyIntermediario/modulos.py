'''
modulos padrões em python (import , form, as e *)
https://doc.python.org/3/py-modindex.html
inteiro - import nome_modulo
Vantangens: Voce tem o namespace do módulo
desvantagens: Nomes grandes
'''
# import sys

# #sys.exit()

# print(sys.platform)

"""
partes- from nome_modulo import objeto1,objeto2
vantagens: nomes pequenos
desvantagens: Sem namespace de módulo
"""
# from sys import exit, platform

# print(platform)

# alias 1- import nome_modulo as apelido
import sys as s

sys = 'subreescrito'
print(sys)
print(s.platform)

# alias 2 - from nome_modulo import objeto as apelido

# from sys import platform as pf, exit as ex

#vantagem: pode reservar nomes para o seu codigo
#Desvantagens: pode ficar fora do padrão da linguagem


'''
Má pratica - from nome_modulo import * 
vantagens: Importa tudo do módulo
desvantagem: IMporta tudo do módulo
'''

from sys import *

print(platform)
