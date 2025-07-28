def valortotal(valor,descontot):
    vt = valor - descontot
    return vt

valor = float(input("Qual é o valor da mercadoria?"))
desconto = float(input("Qual é a % de desconto?"))
descontot = (desconto / 100) * valor
precof = valortotal(valor,descontot)
print("O valor da mercadoria é ", precof,"O valor do desconto foi de ", descontot)

