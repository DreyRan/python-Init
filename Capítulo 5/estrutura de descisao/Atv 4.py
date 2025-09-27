def verificaIdade21(idade1, idade2, idade3, idade4, idade5):
    totalidade = 0
    if (idade1 == 21):
        totalidade += 1
    if (idade2 == 21):
        totalidade += 1
    if (idade3 == 21):
        totalidade += 1
    if (idade4 == 21):
        totalidade += 1
    if (idade5 == 21):
        totalidade += 1

    print(f"O total de idades igual a 21 é {totalidade}")
def main():
    idade1 = int(input("Qual a 1° idade"))
    idade2 = int(input("Qual a 2° idade"))
    idade3 = int(input("Qual a 3° idade"))
    idade4 = int(input("Qual a 4° idade"))
    idade5 = int(input("Qual a 5° idade"))

    verificaIdade21(idade1, idade2, idade3, idade4, idade5)
if __name__ == "__main__":
 main()
