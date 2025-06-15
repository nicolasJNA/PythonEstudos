

try:
    num = int(input("Digite um inteiro: "))
    if num%2 != 0:
        print(f"O numero {num} é impar")
    else:   
        print(f"O numero {num} é par")
except:
    print("Não é um inteiro")


