def calculodias (qntcigarro, qntanos):
    totalcigaross = qntcigarro * (qntanos * 365)
    perdaminutos = totalcigaross * 10
    perdadias = perdaminutos / 1440
    return perdadias
qntcigarro = int(input("Quantos cigarros voce fuma em média por dia?"))
qntanos = int(input("A quantos anos voce fuma?"))

total = calculodias(qntcigarro, qntanos)
print(f"Voce perdeu aproximadamente {total} dias")