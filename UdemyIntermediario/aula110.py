# modulos são singleton
import importlib

import modularizacao_m

for i in range(10):
    #pode recarrgar o modulo
    importlib.reload(modularizacao_m)
    print(i)
