def linha_espaco2(frase3,linha_space):
    print(linha_space)
    print(linha_space)
    print(frase3)

def linha_espaco1(frase1,frase2,frase3):
    linha_space = " "
    print(frase1)
    print(linha_space)
    print(frase2)
    linha_espaco2(frase2,linha_space)
frase1 = str(input("Frase 1"))
frase2 = str(input("Frase 2"))
frase3 = str(input("Frase 3"))

linha_espaco1(frase1,frase2,frase3)

