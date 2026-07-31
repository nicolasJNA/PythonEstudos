class Escritor:
    def __init__(self, nome):
        self.nome = nome;
        self._ferramenta = None

    @property
    def _ferramenta(self):
        return self._ferramenta

    @_ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta 

class FerramentaDeEscrever:
    def __init__(self, nome):
        self.nome = nome

    def escrever(self):
        return f'{self.nome} está escrevendo'


escritor = Escritor('Jose')
caneta = FerramentaDeEscrever('Bic')
maquina_de_escrever = FerramentaDeEscrever('maquina')

escritor.ferramenta = caneta

print(caneta.escrever)
print(maquina_de_escrever.escrever)
print(escritor.ferramenta.escrever)
