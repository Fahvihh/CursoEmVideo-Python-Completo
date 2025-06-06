NUM = int(input('Digite um número inteiro: '))
NUMANTE = NUM - 1
fatorial = 0
while not NUMANTE == 0:
    fatorial = NUM * NUMANTE
    NUMANTE = NUMANTE - 1
    NUM = fatorial
print(fatorial)