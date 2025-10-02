def  transformaTemperatura(temperaturaC):
    converteC = ((9 * temperaturaC) / 5) + 32
    return converteC
temperaturaC = int(input("Qual e temperatura que voce quer transformar e fahrenheit?"))

fahrenheit = transformaTemperatura(temperaturaC)
print(f"A conversão de graus celsius em fahrenheit deu: {fahrenheit}")