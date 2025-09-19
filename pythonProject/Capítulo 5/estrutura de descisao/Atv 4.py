def mostraidade(id1,id2,id3,id4,id5):
    totalidade = 0
    if(id1 == 21):
        totalidade = (totalidade + 1)
    if(id2 == 21):
        totalidade = (totalidade + 1)
    if (id3 == 21):
        totalidade = (totalidade + 1)
    if (id4 == 21):
        totalidade = (totalidade + 1)
    if (id5 == 21):
        totalidade = (totalidade + 1)

    print("O total de idades igual a 21 é ",totalidade)

id1 = int(input("Qual a 1° idade"))
id2 = int(input("Qual a 2° idade"))
id3 = int(input("Qual a 3° idade"))
id4 = int(input("Qual a 4° idade"))
id5 = int(input("Qual a 5° idade"))

mostraidade(id1,id2,id3,id4,id5)