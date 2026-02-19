import os


secreta = 'amor'
letra_acertada = ''
tentativa = 0

while True:

    digitado = input('Digite uma letra: ')
    tentativa += 1
   
    if len(digitado) > 1:
        print("Digite apenas uma letra")
        continue

    if digitado in secreta:
        letra_acertada += digitado

    palavra_formada = ''
    for soletra in secreta:
        if soletra in letra_acertada:  # Aqui está a correção - mudamos == para in
            palavra_formada += soletra
        else:
            palavra_formada += '*'

    print(palavra_formada)
   
    if palavra_formada == secreta:
        os.system('clear')
        print("Parabéns, você venceu!")
        print(f"A palavra era {palavra_formada}")
        print(f"Você tentou {tentativa} vezes")
        break