Num1 = int(input("Escreva um numero de 5 digitos"))

digito1 = Num1 // 10000
resto = Num1 % 10000

digito2 = resto // 1000
resto = resto % 1000

digito3 = resto // 100
resto = resto % 100

digito4 = resto // 10
digito5 = resto % 10

print(digito1,"  ",digito2,"  ",digito3,"  ",digito4,"  ",digito5)
