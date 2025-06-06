idades = 0
media = 0
maior = 0
nomehomem = ''
MulherMenor = 0
for c in range(1,5):
    nome = str(input(f'Digite o {c}° nome: '))
    idade = int(input(f'Digite a idade correspondente ao {c}° nome: '))
    sexo = str(input(f'Digite o sexo correspondente ao {c}° nome ["M" ou "F"]: ')).upper()
    idades = idades + idade
    media = idades/4
    if sexo == 'M':
        if c == 1:
            maior = idade
            nomehomem = nome
        else:
            if idade > maior:
                maior = idade
                nomehomem = nome
    else:
        if idade < 20:
            MulherMenor = 1
print(f'A média das idades é: {media}')
print(f'O nome do homem mais velho é {nomehomem} com a idade de {maior} anos.')
print(f'O número de mulheres menores que 20 anos é de {MulherMenor}')

