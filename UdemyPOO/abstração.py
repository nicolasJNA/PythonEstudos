from abc import ABC, abstractmethod

class Notificacao(ABC):
    def __init__(self, msg) -> None:
        self.msg = msg

    @abstractmethod
    def enviar(self) -> bool:
        ...

class NotificacaoEmail(Notificacao):
    def enviar(self):
        print('Email: enviando\n', self.msg)
        return True

class NotificacaoCorreio(Notificacao):
    def enviar(self):
        print('Enviando via SMS:', self.msg)
        return False

def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print("Notificação enviada")
    else:
        print("Notificação NAO enviada")

email = NotificacaoEmail("ola mundo")
sms = NotificacaoCorreio("Ola mundo")

email.enviar()
sms.enviar()

notificar(sms)