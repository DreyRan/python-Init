def multiplicanumero(numero):
     for i in range( 0, 11):
         tabuada = numero * i
         print(f"{numero} x {i} = {tabuada}")

numero = int(input("digite um numero"))

multiplicanumero(numero)