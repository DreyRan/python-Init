# Exercício 1: Cumprimento Personalizado
# Crie uma função chamada cumprimentar() que:
# Pergunte o nome da pessoa usando input()
# Imprima uma mensagem de boas-vindas personalizada com o nome
# Não precisa retornar nada, apenas imprimir a mensagem

#Jeito que eu fiz: Quando a função perguntar o input deve estar dentro dela
#def cumprimentar(nome):
   # print("Olá",nome)

# nome = input("Escreva seu nome")

# cumprimentar(nome)

#Jeito certo
def cumprimentar():
    nome = input("Escreva seu nome")
    print("Olá",nome)


cumprimentar()

