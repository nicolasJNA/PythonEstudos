def meurepr(self):
    return f'{self.__class__.name} ({self.__dict__})'


class Meta(type):
    def __new__(mcs,name, bases,dict):
        print("META NEW")
        classe = super().__new__(mcs,name, bases,dict)
        classe.attr = 133
        classe.__repr__ = meurepr

        if 'falar' not in classe.__dict__ or not callable(classe.__dict__['falar']):
            raise NotImplementedError

        return classe 

    def __call__(self, *args, **kwds):
        instancia =  super().__call__(*args, **kwds)
        print(instancia.__dict__)

        if 'nome' not in instancia.__dict__:
            raise NotImplementedError

        return instancia
        
class Pessoa(metaclass=Meta):
    def __new__(cls, *args,**kwargs):
        print('Meu NEW')
        instacia = super().__new__(cls)
        return instacia

    def  __init__(self,nome):
        print('Meu INIT')
        self.nome = nome

    def falar(self):
        print(f'{self.nome} esta falando')

p1 = Pessoa("Luana")
print(p1.attr)