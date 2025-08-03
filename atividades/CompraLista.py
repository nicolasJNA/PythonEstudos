"""
faça uma lista de complas com listas
O usuario deve ter a possibilidade de 
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com erros
de indices inexistentes na lista
"""
import os
lista = []

while True:
    digitado = input('Escolha (l)listar (a)apagar (i)inserir: ')

    if digitado == 'i':
        os.system('clear')
        inserir = input('insira  a compra: ')
        lista.append(inserir)
    elif digitado == 'l':
        for item in enumerate(lista):
            indice, conteudo = item
            print(indice,conteudo)
    elif digitado == 'a':
        deletar = input('Escolha o indice para apagar:')
      
        try:
            ind = int(deletar)
            del lista[ind]
        except ValueError:
            print('Digite um numero pfv')
        except IndexError:
            print('O indice não existe na lista')        
        except Exception:
            print('Erro desconhecido')
    else:
        print('Digite um valor valido')
        continue 