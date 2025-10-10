def apresentaJogador(opcao):
    match opcao:
        case 1:
            print(f"Jogador 1: Bento")
        case 2:
            print(f"Jogador 2: Vitin")
        case 3:
            print(f"Jogador 3: Gabriel")
        case 4:
            print(f"Jogador 4: Militão")
        case 5:
            print(f"Jogador 5: Casemiro")
        case 6:
            print(f"Jogador 6: Douglas Santos")
        case 7:
            print(f"Jogador 7: Vínicius Junior")
        case 8:
            print(f"Jogador 8 Bruno Guimarães")
        case 9:
            print(f"Jogador 9: Richarlisson")
        case 10:
            print(f"Jogador 10: Rodrygo")
        case 11:
            print(f"Jogador 11: Paqueta")

        case _:
            print(f"Jogador {opcao} não encotrado")
def main():
    print("Digite um número de camisa de 1 até 11")
    opcao = (int(input()))

    apresentaJogador(opcao)

if __name__ == "__main__":
    main()