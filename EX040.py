import math
from statistics import mean
NOTA1 = float(input('DIGITE A NOTA DA PROVA 1: '))
NOTA2 = float(input('DIGITE A NOTA DA PROVA 2: '))
Media = mean([NOTA1, NOTA2])
print(f'Sua média é {Media}')
if Media >= 5 and Media < 7:
    print('EM RECUPERAÇÃO!')
elif Media < 5:
    print('REPROVADO(A)!')
else:
    print('APROVADO(A)!')
