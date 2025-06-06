pergunta = ' '
maior = menor = cont = soma = 0
while pergunta != 'N':
    num = int(input('Digite um número: '))
    cont += 1
    soma += num
    pergunta = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print(f'A média dos valores digitados é: {soma/cont:.2f}')
print(f'O maior valor foi: {maior}')
print(f'O menor valor foi: {menor}')