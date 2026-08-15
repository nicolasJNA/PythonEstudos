import abc

class Conta(abc.ABC):
    def __init__(self, agencia: int, conta: int, saldo: float) -> None:
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
    @abc.abstractmethod
    def sacar(self, valor):
        ...

    def depositar(self, valor) -> float:
        self.saldo += valor
        return self.saldo

    def detalhe(self,msg: str = "")->None:
        print(f'Saldo atual {self.saldo} valor {msg}')

class ContaPoupança(Conta):
    def __init__(self, agencia:int, conta:int, saldo:float):
        super().__init__(agencia, conta, saldo)

    def sacar(self, valor: float) -> float:
        pos_saque = self.saldo - valor

        if pos_saque >= 0:
            self.saldo -= valor
            self.detalhe(f'sacado {valor}')
            return self.saldo
        
        print("Não foi possivel efetuar o saque")
        print("Valor ultrapassa o saldo da conta")
