def verificanumero(numero):
    if (numero % 2 != 0):
        print(f"O numero {numero} é impar")
    else:
        print(f"O numero {numero} é par")
numero = int(input("Digite um numero"))

verificanumero(numero)