# class MinhaString(str):
#     def upper(self):
#         print('CHAMOU O UPPER')
#         retorno = super(MinhaString, self).upper()
#         print('Depois do upper')
#         return retorno

# string = MinhaString("ola mundo")
# print(string.upper())

class A:
    atributo_a = 'valor a'
    def method(self):
        print('A')

class B(A):
    atributo_b = 'valor b'
    def method(self):
        print('B')

class C(B):
    atributo_c = 'valor c'
    def method(self):
        print('C')
        super(B,self).method()
       

c = C()
print(c.atributo_c)
print(c.atributo_a)
print(c.atributo_b)
c.method()
print()

print(C.mro())