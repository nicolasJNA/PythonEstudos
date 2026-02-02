# Retorna valores das funçoes
# args - argumentos não nomeados
#* _ * args (empacotamento e desempacotamento)

x,y, *resto = 1,2,3,4,5

# def soma(x,y):
#     return x + y

def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total

tupla = (1,2,3,4,5,6,4,2,2)

total = soma(*tupla)
print(total)