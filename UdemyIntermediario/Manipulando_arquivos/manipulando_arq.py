import os

# criando arquivos com Python
# Usamos a função open para abrir
# um arquivo em pyhton (ele pode ou não existir)
# modos: r(leitura) w(escrita) x(criação)
# a (escreve ao final) b(binário) t(modo texto)
# + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos uteis
# write , read (escreve e ler)
# writelines (escreve varias linhas) seek (move o cursor)
# readline(ler linha) readlines (ler linhas) 

caminho_aquivo = "//home/nicolasj/Programação/Python_git/PythonEstudos/UdemyIntermediario/Manipulando_arquivos/"
caminho_aquivo += 'manipulando_arq.txt'

# arquivo = open(caminho_aquivo,'w')

# arquivo.close()

# with open(caminho_aquivo,'w+') as arquivo:
#     arquivo.write('Linha 1\n')
#     arquivo.write('Linha 1\n')
#     arquivo.writelines(
#         ('linha 3\n','linha 4\n')
#     )
#     arquivo.seek(0,0)
#     print(arquivo.read())
#     print('lendo')
#     arquivo.seek(0,0)
#     print(arquivo.readline().strip())
#     print(arquivo.readline().strip())
#     print(arquivo.readline().strip())
#     print('READLINES')
#     arquivo.seek(0,0)
#     for linhas in arquivo.readlines():
#         print(linhas)


# print('='*12)
# with open(caminho_aquivo,'r') as arquivo:
#     print(arquivo.read().strip())

# print(type(arquivo))

with open(caminho_aquivo,'w') as arquivo:
    arquivo.write('ATENÇÃO\n')
    arquivo.write('Linha 1\n')
    arquivo.writelines(
        ('linha 3\n','linha 4\n')
    )

# os.unlink(caminho_aquivo)
os.remove('aula116-2.txt')

# os.rename(caminho_aquivo,'aula116-2.txt')