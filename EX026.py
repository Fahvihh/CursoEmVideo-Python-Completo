Frase = str(input('ESCREVA UMA FRASE: ')).strip()
print(f'Existe {Frase.upper().count('A')} letras "A"')
print(f'A primeira letra A fica no caracter: {Frase.upper().find('A') +1}')
print(f'A letra A aparece pela última vez no caracter: {Frase.upper().rfind('A') +1}')