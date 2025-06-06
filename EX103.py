def ficha(NomeJogador, QuantGols):
    """
    -> Função ficha criada para
    :param NomeJogador:
    :param QuantGols:
    :return:
    """
    if NomeJogador == "":
        print(f"O jogador <desconhecido> fez {QuantGols} gol(s) no campeonato")
    else:
        print(f"O jogador {NomeJogador} fez {QuantGols} gol(s) no campeonato")


Nome = str(input("Digite o nome do jogador: "))
Gols = str(input("Digite a quantidade de gols: ")).strip()
if Gols.isnumeric():
    Gols = int(Gols)
else:
    Gols = 0
ficha(Nome, Gols)