def removePrimeirodigito(numero):
    return numero // 10000

def removeSegundodigito(numero):
    return (numero % 10000) // 1000

def removeTerceirodigito(numero):
    return (numero % 1000) // 100

def removeQuartodigito(numero):
    return (numero % 100) // 10

def removeQuintodigito(numero):
    return (numero % 10) // 1

numero = int(input("Entre com um  numero de 5 digitos:"))
primerio_digito = removePrimeirodigito(numero)
segundo_digito = removeSegundodigito(numero)
terceiro_digito = removeTerceirodigito(numero)
quarto_digito = removeQuartodigito(numero)
quinto_digito = removeQuintodigito(numero)
print(primerio_digito)
print(segundo_digito)
print(terceiro_digito)
print(quarto_digito)
print(quinto_digito)