def validaidade(idade):
    if(idade >= 18):
        print("você é maior de idade")
    else:
        print("Você é menor de idade")

idade = int(input("Qual sua idade "))

validaidade(idade)