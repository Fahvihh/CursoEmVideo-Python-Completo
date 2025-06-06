import time
NUM = int(input('DIGITE UM NÚMERO INTEIRO: '))
base = int(input('1 - BINÁRIO \n2 - OCTAL \n3 - HEXADECIMAL\nESCOLHA UMA BASE DE CONVERSÃO: '))
if base == 1:
    print('CALCULANDO...')
    time.sleep(2.0)
    print('-------'*5)
    print(f'DECIMAL: {NUM} =====> BINÁRIO: {bin(NUM)[2:]} ')
    print('-------'*5)
elif base == 2:
    print('CALCULANDO...')
    time.sleep(2.0)
    print('-------' * 5)
    print(f'DECIMAL: {NUM} =====> OCTAL: {oct(NUM)[2:]} ')
    print('-------' * 5)
elif base == 3:
    print('CALCULANDO...')
    time.sleep(2.0)
    print('-------' * 5)
    print(f'DECIMAL: {NUM} =====> HEXADECIMAL: {hex(NUM)[2:]} ')
    print('-------' * 5)
else:
    print('Opção Inválida! Tente outra vez!')