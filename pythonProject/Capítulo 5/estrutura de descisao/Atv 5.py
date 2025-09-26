def soma(numero1, numero2, numero3, numero4):
    total = 0

    if (numero1 % 2 == 0):
        total += numero1
    if (numero2 % 2 == 0):
        total += numero2
    if (numero3 % 2 == 0):
        total += numero3
    if (numero4 % 2 == 0):
        total += numero4

    return total


def contaPares(numero1, numero2, numero3, numero4):
    total = 0

    if (numero1 % 2 == 0):
     total += 1
    if (numero2 % 2 == 0):
     total += 1
    if (numero3 % 2 == 0):
     total += 1
    if (numero4 % 2 == 0):
     total += 1


    return total

def main():
    numero1 = int(input("Qual o 1° numero?"))
    numero2 = int(input("Qual o 2° numero?"))
    numero3 = int(input("Qual o 3° numero?"))
    numero4 = int(input("Qual o 4° numero?"))
    totalsoma = soma(numero1, numero2, numero3, numero4)
    totalpares = contaPares(numero1, numero2, numero3, numero4)
    media = totalsoma / totalpares
    print(f"A soma dos numeros é: {totalsoma}")
    print(f"A média dos pares é: {media:.2f}")

if __name__ == "__main__":
    main()
