def diaFeriado(dia, mes):
    match mes:
        case 10:
            match dia:
                case 12:
                    print(f"O dia {dia} do mês {mes} é o feriado do dias das Crianças")
                case _:
                    print(f"Esse dia não exite")
        case _:
            print(f"Nesse mês não tem existe")

def main():

    dia = int(input("Qual o dia do mês"))
    mes = int(input("Qual é o mês"))
    diaFeriado(dia, mes)

if __name__ == "__main__":
    main()