salario = float(input('DIGITE SEU SALÁRIO: R$'))
if salario > 1250:
    print('Parabéns! Você recebeu um aumento de 10%!')
    print(f'NOVO SALÁRIO: R${salario*1.1:.2f}')
else:
    print('Parabéns! Você recebeu um aumento de 15%!')
    print(f'NOVO SALÁRIO: R${salario*1.15:.2f}')