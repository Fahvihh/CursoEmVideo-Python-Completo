import time
DadosJogador= {"Nome Jogador": str(input("Digite o nome do jogador: ")),
               "Quantidade de partidas": int(input("Digite a quantidade de partidas: "))}
TotGols = 0
for c in range(1,DadosJogador["Quantidade de partidas"]+1):
    DadosJogador[f"Quantidade de Gols partida {c}"] = int(input(f"Digite a quantidade de gols da {c}° partida: "))
    TotGols += DadosJogador[f"Quantidade de Gols partida {c}"]
DadosJogador["Total de Gols"] = TotGols
print("+="*20)
print("       Aproveitamento do jogador")
print("+="*20)
for k, v in DadosJogador.items():
    time.sleep(1)
    print(f"{k} : {v}")