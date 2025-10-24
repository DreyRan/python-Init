def main(tecla):
    for i in range(1,31):
        if i % 2 == 0:
            continue
        print(i)

tecla = input("aperte enter")
if __name__ == "__main__":
    main(tecla)
