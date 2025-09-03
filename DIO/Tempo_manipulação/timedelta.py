#manipulação de data e hora usando Timedelta
#Exemplo de um lavajato que de acordo com o tamanho do carro leva um determinado tempo
#o programa exibe o tempo em que o carro entrou no lava a jato e o tempo que sairá 
import datetime 
import os

os.system("clear")

carro = {'P':30,'M':40,'G':60}
data_atual = datetime.datetime.now()

while True: 
    automovel = input("Qual o tamanho do seu carro(P,M,G)? ")
    if carro.get(automovel) == None: #caso o valor digitado não exista no dicionario 'carro'
        continue
    tempo_estimado = data_atual + datetime.timedelta(minutes=carro.get(automovel)) 
    print(f"Seu carro entrou de {data_atual} e ficará pronto as {tempo_estimado}")
    break


