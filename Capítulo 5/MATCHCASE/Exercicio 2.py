def classInmetro(letra):
    match letra:
        case "A":
            print(f"Seu consumo é (Muito Eficiente)")
        case "B":
            print(f"Seu consumo é (Eficiente)")
        case "C":
            print(f"Seu consumo é (Pouco Eficiente)")
        case "D":
            print(f"Seu consumo é (Ineficiente)")
        case _:
            print(f"não está na lista de consumo")

def main():
    print("Qual sua letra de Consumo")
    letra = (input(""))
    classInmetro(letra)

if __name__ == "__main__":
    main()