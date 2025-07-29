"""Calculadora com uso do while"""
while True:
    numero_1 = input('digite o numero: ')
    numero_2 = input('Digite outr numero: ')
    operador = input('Digite o operador(+-/*): ')
    numeros_validos = None;
    num_1_float = float(numero_1)
    num_2_float = float(numero_2)
   
    try:
      numeros_validos = True
    except:
        numeros_validos = False

    if numeros_validos is None:
        print('Digite numeros válidos')
        continue

    operador_permitido = '+-/*'

    if operador not in operador_permitido:
        print('Operador inválido')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador')
        continue

    print('')

    if operador == '+':
        print('A soma dos numeros foi {}',format(num_1_float+ num_2_float))
    elif operador == '-':
        print(num_1_float-num_2_float)
    elif operador == '/':
        if(num_2_float == 0):
            print('Não pode ser feita a operação')
            continue
        print(num_1_float/num_2_float)
    elif operador == '*':
        print(num_1_float*num_2_float)
       
    sair = input('Quer sair? [s]sim: ').lower().startswith('s')
    if (sair):
        break
    
