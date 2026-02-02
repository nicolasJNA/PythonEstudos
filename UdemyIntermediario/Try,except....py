# Try, except, else e finally
# Aula 151,152,143

try:
    a = 19  
    b = 0
    c = a / b
    print("linha 2")
except ZeroDivisionError:
    print('Dividiu por zero')
except NameError:
    print('Nome b não está definido')
except (TypeError, IndexError) as error:
    print('TypeError + IndexError')
    print('MSG:', error)
    print('Nome: ',error.__class__.__name__)
except Exception:   #exceção maxima 
    print('Erro desconhecido')

print('Continuar')