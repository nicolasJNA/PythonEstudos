#Python special methods, Magic methods ou Dunder methods

# __str__ e __repr__


class Ponto:
    def __init__(self,x,y):
        self.x = x 
        self.y = y

    def __str__(self):
        return f'({self.x},{self.y})'
    
    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name} {self.x,self.y}'

coordenada1 = Ponto(1,2)
coordenada2 = Ponto(5,6)

print(f'{coordenada2!r}')
print(f'{coordenada1}')