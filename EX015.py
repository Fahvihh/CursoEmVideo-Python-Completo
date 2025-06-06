QtKmPercorrido = float(input('Digite a quantidade de KM percorrido: '))
QtDiasAlug = int(input('Digite a quantidade de dias alugado: '))
ValKmPercorrido = QtKmPercorrido * 0.15
ValDiasAlug = QtDiasAlug * 60
print(f'O valor a ser pago por {QtDiasAlug} dias e {QtKmPercorrido} KM rodados é de: {ValKmPercorrido + ValDiasAlug}')