import random
print('------------JOKENPÔ--------------')
print('VEREMOS QUEM SERÁ O CAMPEÃO!')
JogadorHumano = str(input('ESCOLHA PEDRA, PAPEL OU TESOURA: ')).strip().upper()
JogadorMaquina = random.choice(['PEDRA', 'TESOURA', 'PAPEL'])
print(f'JOGADOR 1 (HUMANO) JOGOU: {JogadorHumano}')
print(f'JOGADOR 2 (MÁQUINA) JOGOU: {JogadorMaquina}')
if JogadorHumano == JogadorMaquina:
    print('EMPATE! JOGUE OUTRA VEZ...')
elif JogadorHumano == 'PEDRA' and JogadorMaquina == 'PAPEL':
    print('QUE PENA! VOCÊ PERDEU!')
elif JogadorHumano == 'PEDRA' and JogadorMaquina == 'TESOURA':
    print('VOCÊ GANHOU! PARABÉNS!')
elif JogadorHumano == 'PAPEL' and JogadorMaquina == 'TESOURA':
    print('QUE PENA! VOCÊ PERDEU!')
elif JogadorHumano == 'PAPEL' and JogadorMaquina == 'PEDRA':
    print('VOCÊ GANHOU! PARABÉNS!')
elif JogadorHumano == 'TESOURA' and JogadorMaquina == 'PAPEL':
    print('VOCÊ GANHOU! PARABÉNS!')
elif JogadorHumano == 'TESOURA' and JogadorMaquina == 'PEDRA':
    print('QUE PENA! VOCÊ PERDEU!')
else:
    print('VALOR INCOERENTE')
print('-'*32)