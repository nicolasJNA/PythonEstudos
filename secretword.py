secreta = 'amor'
letra_acertada = ''
while True:
    digitado = input('Digite uma letra: ')

    if len(digitado) > 1 or len(digitado) == 0:
        continue
    
    if digitado in secreta:
        letra_acertada += digitado
    
