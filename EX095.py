import time
from itertools import count

cont= 0
ListaJogadores = []
TotGols = 0
while True:
    DadosJogador= {"Nome Jogador": str(input("Digite o nome do jogador: ")),
               "Quantidade de partidas": int(input("Digite a quantidade de partidas: "))}
    for c in range(1,DadosJogador["Quantidade de partidas"]+1):
        DadosJogador[f"Quantidade de Gols partida {c}"] = int(input(f"Digite a quantidade de gols da {c}° partida: "))
        TotGols += DadosJogador[f"Quantidade de Gols partida {c}"]
    DadosJogador["Total de Gols"] = TotGols
    cont += 1
    for i in range(0, cont):
        ListaJogadores.append(DadosJogador)
    Pergunta = str(input("Deseja continuar [S/N]: ")).upper()
    if Pergunta == "N":
        break
print("+="*20)
print("       Aproveitamento do jogador")
print("+="*20)
print("COD  NOME    GOLS    TOTAL DE GOLS")
for x in range(0, cont):
    print(f"\n {x+1}   {ListaJogadores[x]["Nome Jogador"]}", end="    ")
    for y in range(1, cont+1):
        print(f'{ListaJogadores[x][f"Quantidade de Gols partida {y}"]}', end=" ")
    print(f"       {ListaJogadores[x]["Total de Gols"]}")