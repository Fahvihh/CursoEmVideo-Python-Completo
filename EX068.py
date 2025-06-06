import random, time
cont = 0
print('_-'*20)
print(" "*5,"VAMOS JOGAR ÍMPAR OU PAR!", " "*5)
print('_-'*20)
while True:
    NumJogador = int(input("Digite um número: "))
    Escolha = str(input("Coloque sua escolha de ímpar ou par [I/P]: ")).upper()
    NumMaquina = random.randint(1,10)
    soma = NumJogador + NumMaquina
    print("--"*20)
    print(f"Você jogou {NumJogador} e o computador {NumMaquina}. Total de {soma}. ", end="")
    if soma % 2 == 0:
        print("Deu Par!")
        print("--" * 20)
        if Escolha == "P":
            print("Você Ganhou!")
            cont += 1
        else:
            print("Você Perdeu! Fim de Jogo!")
            break
    else:
        print("Deu Ímpar!")
        print("--" * 20)
        if Escolha == "I":
            print("Você Ganhou!")
            cont+=1
        else:
            print("Você Perdeu! Fim de Jogo!")
            break
print("--"*20)
print(f"Você ganhou {cont} vezes!")