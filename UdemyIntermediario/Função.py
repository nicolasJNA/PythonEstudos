import os
os.system('clear')
"""
Introdução a funções no python (def)
Funções sçao trechos de cofigo usados para
replicar determinada ação ao longo do seu codigo
elas podem receber valores para parametos e retornar um valor
especifico.
Por padrão, funçoes python retornam None (Nada) 
Refatorar: editar o código
"""
# caso n tenha nenhum parametro dado, o 3º valor em ver de ser None,
# ele tem 10 como valor 
#         ( parametro)

def soma(a,b,c=10):
    #definição
    print(f'{a=}\t {b=}\t {c=}')

#argumentos posicionais
soma(b=22,a=33)   
soma(22,33,11)
