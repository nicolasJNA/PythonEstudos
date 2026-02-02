# Generator expression, Iterables e Iterators em python
import sys

iterable = ['Ola','mundo','!']
iterador = iter(iterable)

lista = [numero for numero in range(10000)]
generator = (numero for numero in range(100))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

print(next(generator))