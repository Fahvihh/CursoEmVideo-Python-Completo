NUM1 = int(input('DIGITE UM NÚMERO: '))
NUM2 = int(input('DIGITE MAIS UM NÚMERO: '))
if NUM1 > NUM2:
    print(f'O número {NUM1} é maior que {NUM2}')
elif NUM2 > NUM1:
    print(f'O número {NUM2} é maior que {NUM1}')
else:
    print(f'O número {NUM1} é igual ao {NUM2}')