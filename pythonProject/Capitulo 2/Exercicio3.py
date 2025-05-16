
print("Tempo do primeiro trecho: 8min e 15seg")
minutosPrimeirotrecho = 8 * 60
segundoPrimeirotrecho = 15
totalTempoprimeirotrecho = (8*60) + 15


print("Tempo do segundo trecho: 7min e 12seg x 3")
minutosSegundotrecho = (7 * 3) * 60
segundoSegundotrecho = 12 * 3


print("Tempo do Terceiro trecho: 8min e 15seg")
minutosTerceirotrecho = 8 * 60
segundoTerceirotrecho = 15

# Soma o total de minutos e converte todos os segundos em minutos
totalTempoTodostrechosminutos = (minutosPrimeirotrecho +
                                 minutosSegundotrecho +
                                 minutosTerceirotrecho) / 60
# Soma o valor total dos segundos
totalTempoTodostrechosSegundos =(segundoPrimeirotrecho +
                                 segundoSegundotrecho +
                                 segundoTerceirotrecho)

restantesMinutos = int(totalTempoTodostrechosSegundos / 60)
restantesSegundos = totalTempoTodostrechosSegundos % 60

totalMinutos = totalTempoTodostrechosminutos + restantesMinutos
totalSegundos = restantesSegundos

print("Soma de tempo de todos os trecho:",totalMinutos,"Minutos")
print("Soma de tempo de todos os trecho:",totalSegundos,"Segundos")

horaInicialSegundos = (6 * 60) * 60
minutosInicialSegundos = 52 * 60

horarioIniciaSegundos = horaInicialSegundos + minutosInicialSegundos

tempoTrechoMinutosSegundos = totalMinutos * 60

horaChegada = int(((horarioIniciaSegundos + tempoTrechoMinutosSegundos) /60)/60)
minutosChegado = int(((minutosInicialSegundos + tempoTrechoMinutosSegundos) / 60) % 60)
print("O tempo de Chegado foi as",horaChegada,":", minutosChegado, restantesSegundos)
