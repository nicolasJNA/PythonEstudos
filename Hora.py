entrada = input("Que horas são: ")
try: 
    hora = int(entrada)
    if 11 >= hora >= 0:
        print("Bom dia")
    elif 17 >= hora >= 12:
        print('Boa tarde')
    elif 17 < hora < 0:
        print('Boa noite')
    else: 
        print('hora não reconhecida')
except:
    ...