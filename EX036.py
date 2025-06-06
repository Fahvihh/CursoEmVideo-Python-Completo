ValCasa = float(input('Digite o valor da casa:  '))
Salario = float(input('Digite seu salário:  '))
QuantAnos = float(input('Digite a quantidade de anos para pagar:  '))
PrestMensal = ValCasa / (QuantAnos * 12)
print(f'Para comprar uma casa de R${ValCasa} em {QuantAnos} anos é necessário uma '
      f'prestação mensal de: {PrestMensal}')
print(f'Acontece que o banco só aceita o empréstimo caso a prestação não exceda 30% do seu '
      f'salário, ou seja, R${Salario*0.3}')
print('Portanto...')
if PrestMensal <= Salario * 0.3:
      print(f'Empréstimo aceito!')
elif PrestMensal > Salario * 0.3:
       print('Empréstimo Negado!')