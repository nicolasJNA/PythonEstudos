"""
Gerador de CPF 
Validador de CPF
"""
import os
import random

contador = 10
soma = 0
while True:

    cpf = ''
    for i in range(9):
        cpf += str(random.randint(0,9))

    nove_digitos = cpf[:9]

    # # try:
    # #     repetido = cpf == cpf[0] * len(cpf) 
    # # except IndexError:
    # #     print("CPF INVALIDO")
    # #     break

    # if repetido:
    #     print("VOCÊ DIGITOU SEQUENCIAL")
    #     break

    for indice in nove_digitos:
        valor = int(indice)
        soma += (valor*contador)
        contador -= 1
    
    resto = (soma*10) % 11
    resto = resto if resto <= 9 else 0 
    
    digito1 = resto
    os.system('clear')
    cpf += str(resto)

    print("O primeiro digito é", resto)
    
    soma = 0
    contador = 11
    dez_digitos = cpf[:10]
    for indice in dez_digitos:
        valor = int(indice)
        soma += (valor*(contador))
        contador -= 1
    
    resto = (soma*10) % 11
    resto = resto if resto <= 9 else 0 

    print("O segundo digito é", resto)
    digito2 = resto
    cpf_gerado = f'{nove_digitos}{digito1}{digito2}'
    print(cpf_gerado)
    break
    # if cpf_gerado == cpf:
    #     print("CPF VÁLIDO")
    #     break
    # else:
    #     print("CPF INVALIDO")
    #     break