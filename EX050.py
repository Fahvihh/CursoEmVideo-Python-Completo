print('Vamos realizar a soma de números pares!')
somapar = 0
cont = 0
for c in range(1,7):
    num = int(input(f'Digite o {c}° número: '))
    if num % 2 == 0:
        somapar += num
        cont += 1
print(f'Você informou {cont} números e a soma deles foi: {somapar}')
