try: 
    print('ABRIR ARQUIVO')
    #8/0
except ZeroDivisionError as error:
    print(error.__class__.__name__)
    print('DIVIDIU POR ZERO')
except ValueError:
    print("ERRO DE VALOR")
else:
    print('Não aconteceu erro')
finally:
    print('FECHAR ARQUIVO')