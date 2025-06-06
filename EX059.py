escolha = 0
while not escolha == 5:
    val1 = float(input('Digite o 1° valor: '))
    val2 = float(input('Digite o 2° valor: '))
    print('ESCOLHA ENTRE...\n'
          '[1] SOMAR\n'
          '[2] MULTIPLICAR\n'
          '[3] MAIOR\n'
          '[4] NOVOS NÚMEROS\n'
          '[5] SAIR DO PROGRAMA\n')
    escolha = int(input('DIGITE: '))
    if escolha == 1:
        print(f'SOMA DE {val1} + {val2} = {val1+val2}')
    elif escolha ==2:
        print(f'A MULTIPLICAÇÃO DE {val1} x {val2} = {val1*val2}')
    elif escolha ==3:
        if val1 > val2:
            print(f'O MAIOR VALOR ENTRE {val1} E {val2} É: {val1}')
        elif val1 == val2:
            print(f'OS VALORES {val1} E {val2} SÃO IGUAIS')
        else:
            print(f'O MAIOR VALOR ENTRE {val1} E {val2} É: {val2}')
print('Fim do programa!')
