Dinheiro = float(input('DIGITE O SEU SALDO BANCÁRIO: '))
if Dinheiro < 5.82:
    print('Você NÃO pode comprar nenhum dólar! Sinto muito!')
else:
    print(f'VOCÊ PODE COMPRAR {Dinheiro//5.82} DÓLAR(ES)! PARABÉNS')