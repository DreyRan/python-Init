def valor_diametro(raio):
    return raio * 2

def valor_area(raio , pi):
    return pi * (raio ** 2)

def valor_circunferencia(raio , pi):
    return (2 * raio) * pi

# Main
pi = 3.14159
raio = float(input("Qual o valor do raio?"))
diametro = valor_diametro(raio)
area = valor_area(raio, pi)
circunferencia = valor_circunferencia(raio, pi)

print("Esse é o valor do raio que voce colocou", raio)
print("Esse é o valor do diametro", diametro)
print("Essse é o valor da area", area)
print("Esse é o valor da circunferencia", circunferencia)