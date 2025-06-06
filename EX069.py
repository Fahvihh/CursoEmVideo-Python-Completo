ContIdade = ContSexoM = ContIdadeF = 0
while True:
    Idade = int(input('Digite sua idade: '))
    Sexo = str(input('Digite seu sexo [M/F]: ')).upper()
    Pergunta = str(input('Deseja continuar [S/N]: ')).upper()
    if Idade > 18:
        ContIdade += 1
    if Sexo == 'M':
        ContSexoM += 1
    if Sexo == 'F':
        if Idade < 20:
            ContIdadeF += 1
    if Pergunta == 'N':
        break
print(f'O número de pessoas maiores que 18 anos é de: {ContIdade}')
print(f'O número de homens cadastrados foram de: {ContSexoM}')
print(f'O número de mulheres menores que 20 anos é de: {ContIdadeF}')
