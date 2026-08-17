# os.path permite trabalhar com caminho de arquivos e pastas 
# os.path.join: Junta str num unico caminho, ex: ('pasta1','pasta2','arq') -> pasta1/pasta2/arq 
# os.path.split: retorna uma tupla com (caminho, arquivo)
import os

caminho = os.path.join('casa','quarto','computar.txt')
print(caminho)
print(os.path.split(caminho))
local,arq = os.path.split(caminho)

print(os.path.splitext(caminho))
print(os.path.exists(caminho))
print(os.path.basename(caminho))