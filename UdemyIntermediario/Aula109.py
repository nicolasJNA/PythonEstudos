'''
Escoo de funções em Python
escopo significa o local onde aquelle código é alcançavel
Existe o escopo global e local
O escopo global é o escopo onde todo o código é alcançavel
O escopo local é o escopo onde apenas nomes do mesmo local podem
ser alcançados.
'''
x = 1
def escopo():
    x = 10
    def outra():
        global x
        x = 11
        y= 2
        print(x,y)
    outra()
    print(x)
print(x)
escopo()
print(x)