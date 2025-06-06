from math import sqrt, pow
CatO = float(input('DIGITE O VALOR DO CATETO OPOSTO: '))
CatA = float(input('DIGITE O VALOR DO CATETO ADJACENTE: '))
print(f'HIPOTENUSA = {sqrt(pow(CatO,2)+pow(CatA,2))}')