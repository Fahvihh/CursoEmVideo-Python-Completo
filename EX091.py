import random, time
from operator import itemgetter
jogadores = {}
jogador = 0
for c in range(1,5):
    jogador = random.randint(1,6)
    jogadores[f"Jogador{c}"] = jogador.conjugate()
ranking = {}
for k, v in jogadores.items():
    print(f"O {k} tirou {v}")
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
c = 1
for k, v in ranking:
    print(f"{c}° LUGAR: {k} com {v}")
    c += 1