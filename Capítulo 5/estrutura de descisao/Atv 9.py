def verificaNumero(numero):

    if (numero % 5 == 0):
        print(f"O numero {numero} é divisível por cinco")
    else:
        print(f"O numero {numero} não é divisível por cinco")

    if (numero % 3 == 0):
        print(f"O numero {numero} é divisível por tres")
    else:
        print(f"O numero {numero} não é divisível por tres")

numero = int(input("Digite um numero"))

verificaNumero(numero)