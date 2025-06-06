import time
print('---TABUADA COM A FUNÇÃO FOR---')
NUM = int(input('DIGITE UM NÚMERO: '))
print('CALCULANDO...')
time.sleep(2)
print('-'*30)
for c in range(1,11):
    print(f'{NUM} x {c} = {NUM*c}')
    time.sleep(1)
print('-'*30)
