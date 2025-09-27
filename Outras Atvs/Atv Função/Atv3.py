def tempot(distancia,velomedia):
    tempo =  int(distancia / velomedia)
    return tempo
distancia = int(input("Qual a distancia que deseja percorrer?"))
velomedia = int(input("Qual a velocidade media desejada?"))
velototal = tempot(distancia,velomedia)
print("Esse é o tempo que vc deve demora para percorer essa diatancia.",velototal,"Horas")
