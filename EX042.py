reta1 = int(input('DIGITE O VALOR EM METROS DE UMA RETA: '))
reta2 = int(input('DIGITE O VALOR EM METROS DE OUTRA RETA: '))
reta3 = int(input('DIGITE O VALOR EM METROS DE OUTRA RETA: '))
if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print('Parabéns! Formou um triângulo!')
    if reta1 != reta2 and reta1 != reta3 and reta2 != reta3:
        print('Seu triângulo é ESCALENO')
    elif reta1 == reta2 and reta2 == reta3 and reta3 == reta1:
        print('Seu triângulo é EQUILÁTERO')
    elif reta1 == reta2 or reta2 == reta3 or reta3 == reta1:
        print('Seu triângulo é ISÓCELES!')
else:
    print('Que pena! Não formou um triângulo!')