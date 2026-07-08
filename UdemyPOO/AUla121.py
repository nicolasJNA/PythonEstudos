# Métodos em instãncias de classes python
# Hard Code - algo que foi escrito diretamente no código
class Car:
    def __init__(self,nome):
        self.nome = nome

    def acelerar(self):
        print(f'Carro {self.nome} acelerando')

fusca = Car('Fusca')
print(fusca.nome)
fusca.acelerar()
print('-'*23)
celta = Car(nome='Celta')
print(celta.nome)
celta.acelerar()