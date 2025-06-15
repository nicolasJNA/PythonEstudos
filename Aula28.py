nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")     

if nome and idade:
    print('Seu nome é {}'.format(nome))
    print('Seu nome invertido é {}'.format(nome[::-1]))
    if ' ' in nome:
        print("seu nome tem espaços")
    else:
        print("seu nome não tem espaços")

    print(f'Seu nome tem {len(nome)} letras')
    print('A primeira letra do seu nome é {}'.format(nome[0]))
    print('A ultima letra do seu nome é {}'.format(nome[-1]))
else:
    print("Desculpe, você deixou campos vazios")