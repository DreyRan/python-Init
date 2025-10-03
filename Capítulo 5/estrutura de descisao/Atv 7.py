def verificanumero(numero):
    if (numero == 0):
        print(f"É ZERO")
    elif (numero > 0):
        print(f"Esse numero é positivo")
    else:
        print(f"Esse numero é negativo")
numero = int(input("Digite um numero"))

verificanumero(numero)