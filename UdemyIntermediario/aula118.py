# problema dos parametros mutáveis em funções

# def adiciona_clientes(nome,lista=[]):
#     lista.append(nome)
#     return lista

def adiciona_clientes(nome,lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

cliente1 = adiciona_clientes('nicolas')
adiciona_clientes('Joana',cliente1)
print(cliente1)

cliente2 = adiciona_clientes('Jurubea')
adiciona_clientes('Josefina',cliente2)
print(cliente2)
