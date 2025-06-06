Distancia = float(input('DIGITE A DISTÂNCIA EM KM DA SUA VIAGEM: '))
if Distancia <= 200:
    print(f'VALOR DA VIAGEM: R$ {Distancia*0.5}')
else:
    print(f'VALOR DA VIAGEM R$ {Distancia*0.45}')