# criar, deletar, mover e nomear diretorios ou arquivos
# os + shutil 
# mover/renomear: shutil.move
# mover/renomear: os.rename
# copiar: shutil.copy
# apagar: os.unlink
# apagar recursivamente: shutil.rmtree

import os
import shutil

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME,'Documentos')
DESKTOP = os.path.join(HOME,'Documentos')
print(*os.walk(DESKTOP))