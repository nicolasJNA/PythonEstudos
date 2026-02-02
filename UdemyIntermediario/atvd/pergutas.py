# Jogo de perguntas
def jogo(dicio,ind):
    print('\nPergunta: ',dicio[ind]['pergunta'])
    for indice,valores in enumerate(dicio[ind]['alternativas']):
        print(f'{indice}) {valores}')
    resposta = input('Qual a alternativa correta: ')
    if resposta == dicio[ind]['resposta']:
        print('\nPARABENS VOCE ACERTOU!!!')
        return 1
    else:
        print('QUE PENA VOCE ERROU')
        return 0

perguntas =[
    {'pergunta': 'Qual a capital de pernambuco',
    'alternativas': ['Campinas','Olinda','Igarassu','Caruaru','Recife'],
    'resposta': '4'},
    {'pergunta':'Qual o outro planeta que anel',
     'alternativas':['terra','urano','venus','marte','TON 618'],
     'resposta': '1'},
    {'pergunta':'Qual o resultado correto de 53%14',
    'alternativas':['10','9','7','11','0'],
    'resposta':'3'}
]
total = 0
for indice in range(len(perguntas)):
    total += jogo(perguntas,indice)


print(f'\nO JOGO ACABOU\nAcertos: {total}\nErros:{3-total}')