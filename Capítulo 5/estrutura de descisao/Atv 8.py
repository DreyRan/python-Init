def verificaNumero(numero):
    if (numero % 2 == 0 and numero % 3 == 0):
        print(f"O numero {numero} é divisível por dois e tres")
    else:
        print(f"O numero {numero} não é divisível por dois e tres")

numero = int(input("Digite um numero"))

verificaNumero(numero)