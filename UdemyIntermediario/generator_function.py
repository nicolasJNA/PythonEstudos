# generator functions: podem ser entendidas comoo funções capazes de pausar
# usasse 'yield' no lugar de return

#generation function pois tem o yield
def generator(n=0, maximum=10):
    while True:
        yield n # pausa a execução
        n += 1
        
        if n > maximum:
            return 

gen = generator(n=0)
for n in gen:
    print(n)