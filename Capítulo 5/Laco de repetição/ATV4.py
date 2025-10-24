def main():
    maior = 0
    menor = 0
    print("digite um numero")
    for i in range(10):
        numero = int(input(f"Numero{i + 1}"))

        if(i == 0):
            maior = numero
            menor = numero
        if(numero > maior):
            maior = numero
        elif(numero < menor):
              menor = numero

    print(f"Maior número: {maior}")
    print(f"Menor número: {menor}")

if __name__ == "__main__":
    main()