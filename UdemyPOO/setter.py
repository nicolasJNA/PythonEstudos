class Caneta:
    def __init__(self, cor):
        self._cor = cor

    @property
    def cor(self):
        print("PROPERTY")
        return self._cor

    @cor.setter
    def cor(self, valor):
        self._cor = valor
    

def mostrar(caneta):
    return caneta.cor

caneta = Caneta("Azul")
caneta.cor = 'verde'
print(caneta.cor)