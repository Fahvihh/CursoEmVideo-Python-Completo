import random, time
print('      JOGA NA MEGA SENA    ')
print('-' * 30)
quant = int(input('Digite a quantidade de jogos para sorteio: ' ))
tot = 1
lista = list()
jogos = list()
while tot <= quant:
    cont = 0
    while True:
        num = random.randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear ()
    tot += 1
print ('-=' * 3, f'SORTEANDO {quant} JOGOS', "-="* 3)
for i, l in enumerate (jogos):
    print (f' Jogo {i+1}: {l}')
    time.sleep(1)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5 )