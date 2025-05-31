#C=(n,p) = n! / p! * (n * p)!
import math
def CalcularC(n,p):
    nfa = math.factorial(n)
    pfat = math.factorial(p)
    nvzp = math.factorial(n - p)
    div = pfat * nvzp
    resultado = nfa / div
    print("Voce pode fazer ",int(resultado)," Combinações")

n = int(input("Qual o N numero?"))
p = int(input("Qual o P numero?"))
CalcularC(n,p)
