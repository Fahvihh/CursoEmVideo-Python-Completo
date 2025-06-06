## Exemplo 1
NUM1 = float(input('DIGITE O VALOR 1: '))
NUM2 = float(input('DIGITE O VALOR 2: '))
NUM3 = float(input('DIGITE O VALOR 3: '))
if NUM1 > NUM2 and NUM1 > NUM3:
    print(f'MAIOR VALOR DIGITADO: {NUM1}')
elif NUM2 > NUM1 and NUM2 > NUM3:
    print(f'MAIOR VALOR DIGITADO: {NUM2}')
else:
    print(f'MAIOR VALOR DIGITADO: {NUM3}')
if NUM1 < NUM2 and NUM1 < NUM3:
    print(f'MENOR VALOR: {NUM1}')
elif NUM2 < NUM1 and NUM2 < NUM3:
    print(f'MENOR VALOR: {NUM2}')
else:
    print(f'MENOR VALOR: {NUM3}')

## Exemplo 2
## Também da pra fazer por lista e fica bem menor! Exemplo:
numero1 = float(input('DIGITE O VALOR 1: '))
numero2 = float(input('DIGITE O VALOR 2: '))
numero3 = float(input('DIGITE O VALOR 3: '))
list = [numero1, numero2, numero3]
print(f'MAIOR VALOR: {max(list)}')
print(f'MENOR VALOR: {min(list)}')