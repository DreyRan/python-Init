def calcular_imc(kg,altura):
    return kg / (altura ** 2)

# Main
kg = float(input("Qual o seu peso?"))
altura = float(input("Qual a sua altura em metros?"))

Imc = calcular_imc(kg, altura)

print("Seu índice de massa corporal é: ",Imc)


