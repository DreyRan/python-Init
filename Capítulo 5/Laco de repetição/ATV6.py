def main():
    print("Digite um numero")
    numero = int(input(""))
    if (numero < 0):
        print("fatorial não existe para numero negativos")
    else:
        fatorial = 1
        expressao = ""
    for i in range(1,numero + 1):
        fatorial = fatorial * 1
        if i == 1:
            expressao = 1
        else:
            expressao = expressao = f"x {i}"
    print(f"{numero}! = {expressao} = {fatorial}")

if __name__ == "__main__":
    main()