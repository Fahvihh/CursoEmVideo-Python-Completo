Idade = int(input('DIGITE SUA IDADE: '))
if Idade <= 9:
    print('ALUNO MIRIM')
elif Idade <= 14:
    print('ALUNO INFANTIL')
elif Idade <= 19:
    print('ALUNO JUNIOR')
elif Idade == 20:
    print('ALUNO SÊNIOR')
else:
    print('ALUNO MASTER')