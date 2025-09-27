def calcular_imc(kg,altura):
    IMC = kg / (altura ** 2)
    print("Seu índice de massa corporal é: ",IMC)

def calcular_def_p_agua(kg,altura2,idade):
    T = 13.397 * kg
    M = 4.799 * altura2
    B = 5.677 * idade
    TMB = 88.362 + T + M + B
    TDEE = TMB * 1.55
    Defict = TDEE - (TDEE * 0.15)
    grama_proteina = 1.5 * kg
    mlporkg = 0.035 * kg
    print("Seu DEFICT calorico diario é de: ",int(Defict)," Kcal/dia")
    print("Voce deve consumir: ",int(grama_proteina)," Gramas de proteina por dia")
    print("Voce tem que beber: ",mlporkg,"Litros de água por dia")

kg = float(input("Quantos quilos vc tem?"))
altura = float(input("Qual a sua altura em metros?"))
altura2 = float(input("Qual a sua altura em cm?"))
idade = int(input("Qual a sua idade?"))

calcular_imc(kg, altura)
calcular_def_p_agua(kg,altura2,idade)

