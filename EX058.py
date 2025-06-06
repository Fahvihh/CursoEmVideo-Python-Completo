import random
cont = 1
print('OLÁ AMIGO VIRTUAL! VAMOS JOGAR?')
print('Digite um número de 0 a 10 enquanto eu sorteio um aleatório! Você acha que é capaz de acertar?')
NumDigitado = int(input('NÚMERO: '))
NumAleatorizado = random.randint(0,10)
while not NumDigitado == NumAleatorizado:
    print('Errou! Tente outra vez...')
    NumDigitado = int(input('NÚMERO: '))
    NumAleatorizado = random.randint(0, 10)
    cont += 1
print(f'Parabéns! Você acertou! Foram necessárias {cont} tentativas.')