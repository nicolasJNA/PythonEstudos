def soma(x,y):
    return x + y

def multiplica(x,y):
    return x * y

def criar_funcao(funcao,x):
    def aux(y):
        return funcao(x,y)
    return aux

soma_cinco = criar_funcao(soma,5)
multiplica_dez = criar_funcao(multiplica,10)

print(multiplica_dez(10))