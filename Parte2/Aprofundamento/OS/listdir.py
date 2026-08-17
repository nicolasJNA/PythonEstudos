# os os.listdir permite navegar entre os caminhos
import os

for caminhos in os.listdir('/home/nicolasj/Programação/Python/PythonEstudos'):
    if os.path.splitext(caminhos)[1] == '.txt':
        print(caminhos)