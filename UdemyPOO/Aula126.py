# @static method (metodos staticos) sõa inuteis no PYTHON
# Métodos estáticos são metodos que estão dentro da classe
# São funçõs que existem dentro da classe

class Classe:
    @staticmethod
    def estatico(*args,**kwargs):
        print('OI',args,kwargs)


c1 = Classe()
c1.estatico()