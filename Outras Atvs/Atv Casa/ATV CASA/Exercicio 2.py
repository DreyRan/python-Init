# Escreva um programa para ler o número total de eleitores de um município, o
# numero de votos brancos, nulos e válidos. Apresente a percentagem que cada
# um representa em relação ao total de eleitores.

Totaleleitores = int(input("Quantos eleitores tem na cidade?"))
TotalvotosBrancos = int(input("Qual foi a quantidade de votos em Branco?"))
TotalvotoNulos = int(input("Qual foi a quantidade de votos nulos?"))

Votosvalidos = Totaleleitores - (TotalvotosBrancos + TotalvotoNulos)

Votosnulo = (TotalvotoNulos / Totaleleitores) * 100
Votosbrancos = (TotalvotosBrancos / Totaleleitores) * 100

print("A porcentegem de votos Valido foi de",Votosvalidos,"%")
print("A porcentagem de voto Nulos foi de",Votosnulo,"%")
print("A porcentagem de votos em Branco foi de",Votosbrancos,"%")