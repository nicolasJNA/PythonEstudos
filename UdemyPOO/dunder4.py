# metodo especial __call__
# Faz algo ser executado entre parenteses

class CallMe:
    def __init__(self,phone):
        self.phone = phone

    def __call__(self):
        print('Está chamando', self.phone)

    def __repr__(self):
        return f'{self.__class__.__name__} {self.__dict__}'  

call1 = CallMe('358336550')
call1()