# groupby

from itertools import groupby

alunos = [
    {'nome':'Nicolas','nota':'A'},{'nome':'Nil','nota':'D'},
    {'nome':'Nico','nota':'B'},{'nome':'Nola','nota':'C'},
    {'nome':'Nolas','nota':'B'},{'nome':'las','nota':'D'},
    {'nome':'Nicol','nota':'A'},{'nome':'Nic','nota':'F'},
]

alunos_ordenados = sorted(alunos, key= lambda a: a['nota'])
alunos_agrupados = groupby(alunos_ordenados, key= lambda a: a['nota'])

for nota, aluno in alunos_agrupados:
    print(nota)
    for estudante in aluno:
        print(estudante)