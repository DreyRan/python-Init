def calculamedia(num1,num2,num3,num4):
    qtdpar = 0
    totalpares = 0
    if(num1 % 2 == 0):
        qtdpar += 1
        totalpares += num1
    if(num2 % 2 == 0):
        qtdpar += 1
        totalpares += num2
    if(num3 % 2 == 0):
        qtdpar += 1
        totalpares += num3
    if(num4 % 2 == 0):
        qtdpar += 1
        totalpares += num4
    return totalpares / qtdpar
    print("A media de tudo é ", media1)
num1 = int(input("Digite o 1° numero"))
num2 = int(input("Digite o 2° numero"))
num3 = int(input("Digite o 3° numero"))
num4 = int(input("Digite o 4° numero"))
totalmedia = calculamedia(num1,num2,num3,num4)
print("A media dos numeros pares é:", totalmedia)