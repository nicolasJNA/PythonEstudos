#variaveis livres + nonlocal(locals,globals)

# def fora(x):
#     a = x

#     def dentro():
#         # print(locals())
#         print(dentro.__code__.co_freevars)
#         return a
#     return dentro

# dentro1 = fora(10)
# dentro2 = fora(5)
# print(dentro1())
# print(dentro2())

def concatenar(String_inicial):
    valorfinal = String_inicial

    def interno(valorConcatenador):
        nonlocal valorfinal
        valorfinal += valorConcatenador
        return valorfinal
    return interno

c = concatenar(5)
print(c(3))
print(c(5))
print(c(9))