# json.dump e json.load (converte num dicionario python)
import os
import json

NAME_FILE = 'aula2.json'
PATH_FILE_ABSOLUTE = os.path.abspath(
    os.path.join(os.path.dirname(__file__),NAME_FILE)
)


json_create = {'name': 'Circulo de fogo', 'orinal_name': 'Pacific rin',
'buget': 3000000, 'characters': ['Beget', 'Mako'],'is_movie': True, 'director': None} 

with open(PATH_FILE_ABSOLUTE,'w') as arquivo:
    json.dump(json_create,arquivo,indent=2)

with open(PATH_FILE_ABSOLUTE,'r') as arquivo:
    json_dict = json.load(arquivo)
    print(json_dict)