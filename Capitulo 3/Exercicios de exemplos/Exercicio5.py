def medianota(nota1,nota2,nota3,nota4):
    return (nota1 + nota2 + nota3 + nota4) / 4

# Main
nome = input("Qual o nome do aluno?")
nota1 = float(input("Qual a 1° nota?"))
nota2 = float(input("Qual a 2° nota?"))
nota3 = float(input("Qual a 3° nota?"))
nota4 = float(input("Qual a 4° nota?"))

mediaTotal = medianota(nota1, nota2, nota3, nota4)
print(nome, "Essa é a sua media total", mediaTotal)