# _new__ e __init__ em classes python

# __new__ cria e retorna um novo objeto (não recebe self)
# __init__ metodo responsavel por inicializar a instancia (retorna None)

class A:
    def __new__(cls, *args, **kwargs):
        print("antes da criação da instancia")
        instancia = super().__new__(cls)
        print("depois da criação da instancia")
        return instancia
    
    def __init__(self,x):
        self.x = x
        print('Local do init')

    def __repr__(self):
        return 'A()'

a = A(123)
print(a.x)