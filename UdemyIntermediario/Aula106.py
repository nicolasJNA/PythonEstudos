'''
Introdução a função no Python
Funções são trechos de codigos usados para
replicar determinada ação ao longo do seu código.
Elas pode receber valores para parâmetros (argumentos)
e retorna um valor em especifico
Por padrão funções em pyhton retornam None
funçoes devem possuir a primeira letra em minusculo por padrão
'''

# def imprimir( a, b, c):
#     print(f'Hello {a}{b}{c}')
#     print('World')

# imprimir(1,2,3)
# imprimir(5,9,7)

#            (  parametro                   )
def saudadcao(nome1='Sem Nome',nome2='Zezin'):
    print(f'ola {nome1} e {nome2}')

#        (  argumento    )
saudadcao(nome2='nicolas')
saudadcao()
