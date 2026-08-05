from contextlib import contextmanager
@contextmanager
def my_open(caminho_arq, modo):
    print("Abrindo arquivo")
    try:
        arquivo = open(caminho_arq, modo)
        yield arquivo
    except Exception as e: 
        print("Ocorreu um erro:", e.__class__.__name__)
    print('Fechando')
    arquivo.close()


with my_open('contextManager.txt', 'w') as arquivo:
    print('WITH', arquivo)
    print(type(arquivo))
    arquivo.write('EScrito',5212)