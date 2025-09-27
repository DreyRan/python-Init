def calculaLucro(precocombustivel,litrosgasto, valorrecebido):
    valorliquido = (valorrecebido - (precocombustivel * litrosgasto))
    print(f"O seu valor liquido foi de: {valorliquido}")

def mediaConsumo(marcaodometro, marcakm, litrosgasto):
    rodaKm = marcakm - marcaodometro
    mediaKm = rodaKm / litrosgasto
    print(f"Sua media de Km por litro é de: {mediaKm}Km/L")

precocombustivel = float(input("Qual o preço do combustivel?"))
marcaodometro = float(input("Qual a marcação do Odometro no inicio do dia?"))
marcakm = float(input("Qual a marcação de km no fim do dia?"))
litrosgasto = float(input("Quantos litros voce gastou?"))
valorrecebido = float(input("Quanto voce recebeu no dia?"))

mediaConsumo(marcaodometro, marcakm, litrosgasto)
calculaLucro(precocombustivel,litrosgasto, valorrecebido)
