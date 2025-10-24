def main():
    divisiveis = 0
    print("digite um numero")
    for i in range(5):
        numero = int(input(f"Numero{i + 1}"))

        if(numero % 3 == 0):
            divisiveis += 1

    print(f"São {divisiveis} numeros divisiveis por 3")
if __name__ == "__main__":
    main()