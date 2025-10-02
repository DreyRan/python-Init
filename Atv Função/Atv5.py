def calculapreco(kmPercorrido, diasAlugados):
    dias = 60
    kmpreco = 0.15
    preco = (kmPercorrido * kmpreco) + (diasAlugados * dias)
    return preco
kmPercorrido = int(input("Quantos Km voce percorreu?"))
diasAlugados = int(input("Por quantos dias voce alugou o carro?"))

precototal = calculapreco(kmPercorrido, diasAlugados)
print(f"O preço total a pagar é de: {precototal} reais")