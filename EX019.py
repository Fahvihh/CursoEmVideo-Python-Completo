import _random
Aluno1 = str(input('DIGITE O NOME DO ALUNO 1: '))
Aluno2 = str(input('DIGITE O NOME DO ALUNO 2: '))
Aluno3 = str(input('DIGITE O NOME DO ALUNO 3: '))
Aluno4 = str(input('DIGITE O NOME DO ALUNO 4: '))
ListaAlunos = [Aluno1, Aluno2, Aluno3, Aluno4]
print(f'O ALUNO ESCOLHIDO FOI: {random.choice(ListaAlunos)}')