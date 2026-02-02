'''
O primieiro modulo executado chamamse __main__
Voce pode importar outro modulo inteiro ou parte do modulo
O python conhece a pasta onde o __main__ está e as pastas
abaixo dele
Ele não conhece pastas e módulos acima do __main__  por padrão
O python connhece todos os modulos e pacotes presentes nos caminhos do
sys.path
'''
import modularizacao_m
import sys 
try:
    sys.path.append('/home')
except:
    ...

print('Este modulo se chama', __name__)
print(*sys.path,sep='\n')