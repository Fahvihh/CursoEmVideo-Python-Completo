import time
print('              BEM VINDO AO PRODUTINHOS.COM!')
print('-*-'*21)
print('Escolha um dos nossos produtinhos diversos e seja feliz!!\n'
      'Temos diversos descontos nas opções de pagamento! #Ficaadica!')
print('-*-'*21)
print('PRODUTOS DISPONÍVEIS:\n'
      '[1] - 👙 (Biquini Rosa)\n'
      'PREÇO: R$69.99\n'
      '[2] - 💄 (Batom Pink)\n'
      'PREÇO: R$23.99\n'
      '[3] - 🪞 (Espelho Pequeno)\n'
      'PREÇO: R$29.99\n'
      '[4] - 📿 (Rosário Simples)\n'
      'PREÇO: R$46.99')
produto = int(input('DIGITE O NÚMERO DO PRODUTO ESCOLHIDO: '))
valprodut = 0
ValFinal = 0
if produto == 1:
    print('Ótima escolha! o biquini é realmente uma maravilha!')
    valprodut = 69.99
elif produto == 2:
    print('Um incrível batom! Vende muito!')
    valprodut = 23.99
elif produto == 3:
    print('É um espelho bem delicado! Lindo!')
    valprodut = 29.99
elif produto == 4:
    print('Rosários são perfeitos né? Eu amo!')
    valprodut = 46.99
print('-*-'*21)
print('FORMAS DE PAGAMENTO:\n'
      '[1] - À VISTA (10% DE DESCONTO)\n'
      '[2] - À VISTA NO CARTÃO (5% DE DESCONTO)\n'
      '[3] - PARCELADO EM 2X (SEM DESCONTO)\n'
      '[4] - PARCELADO EM 3X OU MAIS (20% DE JUROS)')
FormaPagar = int(input('DIGITE A OPÇÃO ESCOLHIDA: '))
if FormaPagar == 1:
    ValFinal = valprodut - (valprodut * 0.1)
elif FormaPagar == 2:
    ValFinal = valprodut - (valprodut * 0.05)
elif FormaPagar == 3:
    ValFinal = valprodut
elif FormaPagar == 4:
    ValFinal = valprodut + (valprodut * 0.2)
print('-*-'*21)
print('CALCULANDO...')
time.sleep(2.0)
print(f'VALOR FINAL PARA PAGAMENTO É DE: R${ValFinal:.2f}')
print('MUITO OBRIGADO! VOLTE SEMPRE!')
print('-*-'*21)
