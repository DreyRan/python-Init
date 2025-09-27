#cap 24.95, desconto 40%, transporte 3 , 60 copias
capa = 24.95
descontoLivraria = capa * 0.40
capaLivraria = capa - descontoLivraria

fretePrimeiroExemplar = 3
freteRestantedosExemplares = 0.75

custoAtacadoPrimeiroExemplar = capaLivraria + fretePrimeiroExemplar
custoAtacado = custoAtacadoPrimeiroExemplar + ((capaLivraria +freteRestantedosExemplares) * 59)
print("O custo total de Atacado  de 60 cópias é de",custoAtacado)
