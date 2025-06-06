num = int(input('Digite um número: '))
tot = 0
for c in range(1,num+1):
    if num % c == 0:
        tot += 1
print(f'O número {num} foi divisivel {tot} vezes.')
if tot == 2:
    print('É primo!')
else:
    print('Não é primo!')