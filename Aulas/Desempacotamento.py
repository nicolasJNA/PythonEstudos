"""
introdução a tuplas e desempacotamento
"""
#o uso da _ serve para se comunicar com outro programador avisando que n usará a variavel

nome1, *_ = ['alberto', 'helena', 'luiz']
print(nome1,_)