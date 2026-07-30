# Abstração
from pathlib import Path

CAMINHO = Path(__file__).parent / 'log.txt'
class Log:
    def _log(self,msg):
        raise NotImplementedError('Implemente o método log')

    def log_error(self,msg):
        return self._log(f'ERROR: {msg}')
    
    def log_success(self,msg):
        return self._log(f'SUCCESS: {msg}')

class LogFileMixin(Log):
    def _log(self,msg):
        msg_formatada = f'{msg} ({self.__class__.__name__})'
        print('Salvando no Log')
        with open(CAMINHO,'a') as arquivo:
            arquivo.write(msg_formatada)
            arquivo.write('\n') 

class LogPrintMixin(Log):
    def _log(self,msg):
        print(f'{msg} ({self.__class__.__name__})')

if __name__ == '__main__':   
    lp = LogPrintMixin()
    lp.log_error('Qualquer coisa')
    lp.log_success('Qualquer coisa')

    lf = LogFileMixin()
    lf.log_error('Qualquer coisa')
    lf.log_success('Qualquer coisa')
