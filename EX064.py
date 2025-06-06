num = 1
soma = 0
cont = 0
while num != 999:
    num = int(input('Digite um número inteiro [999 para parar]: '))
    cont += 1
    soma += num
print(f'A soma de todos os números digitados foi de: {soma - 999}')
print(f'A quantidade de númeos digitados foi de: {cont - 1}')