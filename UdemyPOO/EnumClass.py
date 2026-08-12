import enum 

class Direcoes(enum.Enum):
    DIREITA = enum.auto()
    ESQUERDA = enum.auto()
    CIMA = enum.auto()
    BAIXO = enum.auto()

def mover(direcao: Direcoes):
    if not isinstance(direcao,Direcoes):
        raise ValueError("Direção não encontrada")

    print(f'{direcao.name.capitalize()} ({direcao.value})')

mover(Direcoes.ESQUERDA)
mover(Direcoes.DIREITA)
mover(Direcoes.CIMA)
mover(Direcoes.BAIXO)