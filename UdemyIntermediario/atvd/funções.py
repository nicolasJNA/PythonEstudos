# Exercicio de funções
# multiplicar uma lista de valores inserida pelo usuario
'''
total = 0
lista = []
def produto(*args):
    total = 1
    for numeros in args:
        total *= numeros
    return total

while True:
    numero = input('Informe um numero ou (s)air: ')
    if numero == 's' and len(lista)== 0:
        print(0)
        break
    elif numero == 's':
        total = produto(*lista)
        print(total)
        break
    try: 
        lista.append(int(numero))
    except:
        print("informe um valor válido")
'''
# função que diz se é impar ou par

def im_par(numero):
    resultado = False
    resultado = numero%2 == 0
    return resultado

numero = 0 
resultado = 0
while True:
    numero = input('Escreva um numero inteiro e informarei se é impar ou par: ')
    try:
        numero = int(numero)
    except ValueError:
        print('NUMERO INTEIRO')
        continue
    resultado = im_par(numero)
    if resultado:
        print('É par')
        break
    else:
        print('É impar')
        break