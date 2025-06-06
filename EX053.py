print('Digite uma frase e eu direi se é um PALÍNDROMO!')
Frase = str(input('Digite a frase: ')).lower().split()
FraseCorrig = ''.join(Frase)
FraseInversa = FraseCorrig[::-1]
print(f'A frase sem espaços é: "{FraseCorrig}".\nA frase invertida é: {FraseInversa}.\nPortanto... ')
if FraseCorrig == FraseInversa:
    print('Parabéns! Isso é um PALÍNDROMO')
else:
    print('Que pena! Com certeza NÃO É UM PALÍNDROMO')
