class MyOpen:
    def __init__(self, caminho, modo):
        print("INIT")
        self.caminho= caminho
        self.modo = modo
        self._arquivo = None

    def __enter__(self):
        print('ENTER: ARQUVO ABERTO')
        self._arquivo = open(self.caminho, self.modo)
        return self._arquivo

    def __exit__(self, class_exception, exception, traceback):
        self._arquivo.close()
        print("EXIT: ARQUIVO FECHADO")


with MyOpen('contextManager.txt', 'w') as arquivo:
    print('WITH', arquivo)
    arquivo.write('Linha 1\nLinha 2')