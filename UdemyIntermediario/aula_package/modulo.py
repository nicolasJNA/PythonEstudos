# __all__ = ['variavel','soma']

variavel = 'alguma coisa'
from aula_package.modulo_b import fala_oi
def soma(*args):
    valor = 0
    for numero in args:
        valor += numero
    return valor

nova_var = 'OLA'
#fala_oi()