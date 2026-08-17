# walh permite a navegação pelas pastas de forma recursiva

import os

caminho = os.path.join('/home','nicolasj','Documentos')
for root,dirs,files in os.walk(caminho):
    print(root)
    for arq in files:
        print(f'     {arq}')