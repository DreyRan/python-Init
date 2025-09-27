# Crie uma função chamada calcular_energia() que:
# Receba a massa (em kg) como parâmetro
# Calcule a energia usando a fórmula E=mc² (onde c é a velocidade da luz ≈ 3x10⁸ m/s)
# Retorne o valor da energia calculada
# Não deve imprimir nada dentro da função, apenas retornar o valor

def calcular_energia(massa):
    c = 300000000
    energia = massa * (c**2)
    return energia

resultado = calcular_energia(2)
print(resultado)