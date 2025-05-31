#P(A ou B)=P(A)+P(B)
# Problema exemplo Em um baralho de 52 cartas,
# qual a probabilidade de tirar um Ás ou uma carta de copas?
# Ás = 4 carta = P(A) = 4/52
# Copas = 13 cartas = P(B) = 13/52
# Ás de copas (A B)= 1 carta -> P(AeB) = 1/52
# P(AeB)= 4/52 + 13/52 - 1/52 = 30.77%

def calculaP(total,A,B):
    Ptotal = (A + B - C) / total
    Porcentagem = Ptotal * 100
    print(Porcentagem,"%")

total = float(input("Qual o total?"))
A = float(input("Qual o A?"))
B = float(input("Qual o B?"))
C = float(input("Quantidade que vc quer?"))
calculaP(total, A, B)