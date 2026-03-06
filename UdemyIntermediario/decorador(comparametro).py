# Decoradores com parâmetros
# A ordem dos decoradores sõa feitas de baixo para cima
def fabrica_de_decoradores(a=None,b=None,c=None):
    def fabrica_de_funcoes(func):
        print('Decoradora 1')

        def aninhada(*args, **kwargs):
            print('Parametros do decorador', a,b,c)
            print('aninhada')
            res = func(*args,**kwargs)
            return res
        return aninhada
    return fabrica_de_funcoes


@fabrica_de_decoradores(1,2,3)
def soma(x,y):
    return x+y


multiplica = fabrica_de_decoradores()(lambda x,y: x*y)
dez_cinco = soma(10,5)
print(multiplica(5,6))
print(dez_cinco)