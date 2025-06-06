VelCarro = float(input('DIGITE A VELOCIDADE DO CARRO [KM/H]: '))
if VelCarro > 80:
    print('Que pena! Você foi multado! A multa é de 7 reais para cada km a mais!')
    print(f'Valor da multa: R${(VelCarro-80)*7:.2f}')
else:
    print('Ufa! Você não foi multado! Fique em paz')