print('Vamos realizar uma sequência de Fibonacci!')
Elementos = int(input('Digite a quantidade de elementos da sequência: '))
Term1 = 0
Term2 = 1
print(f'{Term1} -> {Term2}', end='')
cont = 3
while cont <= Elementos:
    Term3 = Term1 + Term2
    print(f' -> {Term3}', end='')
    Term1 = Term2
    Term2 = Term3
    cont += 1
print(' -> FIM')
