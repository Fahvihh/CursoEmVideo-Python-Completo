import random
print('OLÁ AMIGO VIRTUAL! VAMOS JOGAR?')
print('Digite um número de 0 a 5 enquanto eu sorteio um aleatório! Você acha que é capaz de acertar?')
NumDigitado = int(input('NÚMERO: '))
NumAleatorizado = random.randint(0,5)
if NumDigitado == NumAleatorizado:
    print(f'Número Digitado: {NumDigitado} '
          f'Número aleatorizado: {NumAleatorizado}') 
    print('Nossa, você é realmente muito bom! Nós pensamos no mesmo número')
else:
    print(f'Número Digitado: {NumDigitado} '
          f'Número aleatorizado: {NumAleatorizado}')
    print('Nossa, você é péssimo nisso...')