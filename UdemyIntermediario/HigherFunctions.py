'''
Higher Order Functions
    funçõe que retornam outras funções ou recebem funções como parametro
Funções de primeira classe
    função que é tratada como uma variavel ou tipo de dado especifico
'''

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao} {nome}'
    return saudar

falar_bomdia = criar_saudacao('Bom dia')
falar_boanoite = criar_saudacao('Boa noite')

for nome in ['nicolas','caleb','franci']:
    print(falar_bomdia(nome))
    print(falar_boanoite(nome))

