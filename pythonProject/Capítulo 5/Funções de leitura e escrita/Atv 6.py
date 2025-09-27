def calcularMedia(formativa1, formativa2, provabimestral):
    mediaformativa = ((formativa1 + formativa2) / 2)
    mediaBimestral = ((mediaformativa * 0.3) + (provabimestral * 0.7))
    print(f"A sua média bimestral é: {mediaBimestral}")

formativa1 = float(input("Qual a sua primeira nota?"))
formativa2 = float(input("Qual a sua Segunda nota?"))
provabimestral = float(input("Qual a nota da prova bimestral?"))

calcularMedia(formativa1, formativa2, provabimestral)