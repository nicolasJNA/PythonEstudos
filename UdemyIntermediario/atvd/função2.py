#Crie funções que duplicam, triplicam e quadruplicam
# o numero recebido como parametro

def multiplicador(numero):
    def mult(dado):
        return numero*dado
    return mult
while True: 
    try:
        numero = int(input('informe um numero inteiro: '))
        duplicado = multiplicador(numero)
        triplicado= multiplicador(numero)
        quadruplicado = multiplicador(numero)
    except ValueError:
        continue
    print('Duplicado {}'.format(duplicado(2)))
    print('Triplicado {}'.format(triplicado(3)))
    print('Quadruplicado {}'.format(quadruplicado(4)))
    break