# @property - um getter no modo Pythonico
# é um metodo que se comporta como um atributo
# GErealmente é usada nas seguintes situações:
# - como getter 
# - p/ evitar quebra código cliente
# - p/ habilitar setter
# - p/ executar ações para obter um atributo
# Código cliente é o codigo que usa seu codigo
class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    @property
    def cor(self):
        return self.cor_tinta
    # def get_cor(self):
    #     return self.cor

caneta = Caneta('Amarelo')
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)