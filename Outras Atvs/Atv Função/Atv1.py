def novo_salario(salario,aumento):
    valor_aumentado = salario * aumento
    return salario + valor_aumentado

salario = int(input("Qual o valor do seu sálario?"))
aumento = (15 / 100)

total = novo_salario(salario,aumento)
print("Seu aumento foi de ",aumento,"seu novo salaria foi de ", salario," para ",total)