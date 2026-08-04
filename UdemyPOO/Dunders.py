#Python special methods, Magic methods ou Dunder methods

# __str__ e __repr__


class Ponto:
    def __init__(self,x,y) -> None:
        self.x = x 
        self.y = y

    def __str__(self):
        return f'({self.x},{self.y})'
    
    def __repr__(self) -> str:
        class_name = type(self).__name__
        return f'{class_name} ({self.x!r},{self.y!r})'

    def __add__(self,other) -> int:
        resultado = Ponto(self.x + other.x,self.y + other.y)
        return f'{self.__class__.__name__} {resultado.x,resultado.y}'

    def __gt__(self,other) -> bool:
        resultado_self = self.x + self.y 
        resultado_other = other.x + other.y
        return resultado_self>resultado_other

coordenada1 = Ponto(1,2)
coordenada2 = Ponto(5,6)

print(f'{coordenada2 = !r}') #__repr__
print(f'{coordenada1 = }') # __str__
 
soma = coordenada1 + coordenada2
print(f'{soma=}')
print("coordenada2 > coordenada1: ",coordenada2>coordenada1)