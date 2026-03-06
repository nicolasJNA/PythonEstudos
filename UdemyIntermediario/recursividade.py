# Fumções que chamam ela mesma

def recursao(somatorio):
    if somatorio == 0:
        return 0
    return somatorio + recursao(somatorio-1)
 
print(recursao(10))