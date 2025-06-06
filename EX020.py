import random
Aluno1 = str(input('DIGITE O NOME DO ALUNO 1: '))
Aluno2 = str(input('DIGITE O NOME DO ALUNO 2: '))
Aluno3 = str(input('DIGITE O NOME DO ALUNO 3: '))
Aluno4 = str(input('DIGITE O NOME DO ALUNO 4: '))
ListaAlunos = [Aluno1, Aluno2, Aluno3, Aluno4]
random.shuffle(ListaAlunos)
print(f'A Ordem de alunos será {ListaAlunos}')