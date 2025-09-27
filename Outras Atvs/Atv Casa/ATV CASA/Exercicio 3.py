# Escreva um programa que a partir da idade de uma pessoa expressa em anos,
# meses e dias, apresente a idade apenas em dias (considerar o ano com 365 e cada
# mês com 30 dias).

Idadeanos = int(input("Quantos anos voce tem?"))
Idademeses = int(input("Qual sua idade em meses?"))
Idadedias = int(input("Qual sua idade em dias?"))

Totalidadedias = (Idadeanos * 365) + (Idademeses * 30) + Idadedias

print("Voce tem",Totalidadedias,"Dias de vida")