# dir = verifica quais metodos e nomes um objeto possui
# utilizado no modo iterativo

# hasattr = verifica se um metodo está dentro do objeto 
# getattr = executa o metodo que está em str

string = 'Luiz'
metodo = 'upper'

if hasattr(string,metodo):
    print('Existe')
    print(getattr(string,metodo)())
else:
    print('NÂO EXISTE', metodo)