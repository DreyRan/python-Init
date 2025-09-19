def mostremaior(num1,num2,num3):
    maior = num1
    if(num2 > num1):
        maior = num2
    if(num3 > num2):
        maior = num3
    print("O numero", maior, "é o maior dentre os tres")

num1 = int(input("Qual o 1° numero?"))
num2 = int(input("Qual o 2° numero?"))
num3 = int(input("Qual o 3° numero?"))

mostremaior(num1,num2,num3)