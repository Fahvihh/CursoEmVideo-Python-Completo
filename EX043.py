from math import pow
import time
print('BEM VINDO AO CÁLCULO DE IMC.COM!')
print('--'*16)
peso = float(input('DIGITE SEU PESO[KG]: '))
altura = float(input('DIGITE SUA ALTURA[M]: '))
IMC = peso / pow(altura,2)
print('CALCULANDO...')
time.sleep(2.0)
print('--'*16)
print(f'IMC CALCULADO: {IMC:.2f}')
if IMC < 18.5:
    print('ABAIXO DA MÉDIA!')
elif 18.5 <= IMC < 25:
    print('PESO IDEAL!')
elif 25 <= IMC <30:
    print('SOBREPESO!')
elif 30 <= IMC <40:
    print('OBESIDADE')
elif 40 <= IMC:
    print('OBESIDADE MÓRBIDA')
else:
    print('Parece que houve um erro no valor digitado...Tente novamente!')