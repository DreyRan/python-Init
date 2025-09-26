def mostremaior(num1, num2, num3):

    if (num1 > num2):
        if (num1 > num3):
            print(f"O numero {num1} é o maior numero")

    elif (num2 > num3):
        print("O numero",num2, "é o maior dentre os tres")

    else:
        print("O numero", num3, "é o maior dentre os tres")



num1 = int(input("Qual o 1° numero?"))
num2 = int(input("Qual o 2° numero?"))
num3 = int(input("Qual o 3° numero?"))

mostremaior(num1, num2, num3)
