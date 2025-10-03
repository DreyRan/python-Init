def produtos(codigo):
    if (codigo == 1):
        print(f"Este é um Alimento não perecível")

    elif (codigo >= 2 and codigo <= 4):
        print("Este é um Alimento Perecível")

    elif (codigo >= 5 and codigo <= 6):
        print("Este é um produto do Vestuário")

    elif (codigo == 7):
        print("Este é um produto de Higiene Pessoal")

    elif (codigo >=8 and codigo <= 15):
        print("Este é um produto de Limpeza e utensílios domésticos")

    else:
        print("Este não é um código valido")

def main():
    codigo = int(input("Insira o código do produto"))
    produtos(codigo)

if __name__ == "__main__":
    main()
