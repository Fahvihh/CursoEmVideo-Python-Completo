maior = 0
menor = 0
for c in range(1,6):
    peso = float(input('Digite seu peso: '))
    if c == 1:
        maior = peso
        menor = c
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior valor digitado foi: {maior} e o menor foi: {menor}')
