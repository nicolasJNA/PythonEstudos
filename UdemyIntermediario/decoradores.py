# Funções decoradoras e decoradores
# Decorar = adcionar / Remover / restrinngir / alterar
# FUnções decoradorasa são funçõoes que decoram outras funções
# Syntax Sugar

def criar_func(func):
    def interna(*args, **kwargs):
        print('vou te decorar')
        for arg in args:
            e_string(arg)
        resultado = func(*args,**kwargs)
        print(f'O seu resultado foi {resultado}')
        print('Ok, agora voce foi decorada')
        return resultado
    return interna

@criar_func
def inverte_string(string):
    print(f'{inverte_string.__name__}')
    return string[::-1]

def e_string(param):
    if not isinstance(param,str):
        raise TypeError("Param deve ser uma string")

invertida = inverte_string('123')
print(invertida)