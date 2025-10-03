def classificaIdade(idade):
    if (idade >= 5 and idade <= 7):
        print(f"Voce é InfantilA")
    if (idade >= 8 and idade <= 10):
        print(f"Voce é InfantilB")
    if (idade >= 11 and idade <= 13):
        print(f"Voce é JuvenilA")
    if (idade >= 14 and idade <= 17):
        print(f"Voce é JuvenilB")
    elif(idade >= 18):
        print(f"Voce é Senior")

idade = int(input("Qual a sua idade?"))

classificaIdade(idade)