Aluno = list()
ListaClasse = list()
while True:
    Aluno.append(str(input("Digite o nome do aluno: ")))
    Aluno.append(float(input("Digite a nota 1: ")))
    Aluno.append(float(input("Digite a nota 2: ")))
    ListaClasse.append(Aluno[:])
    Aluno.clear()
    FimLaco = str(input("Deseja continuar? [S/N]: ")).upper()
    if FimLaco == "N":
        break
print("N°  NOME          MÉDIA")
print("=-"*20)
for c in range(0,len(ListaClasse)):
    print(f"{c}   ", end='')
    print(f'{ListaClasse[c][0]:10}   ', end='')
    print(f'{(ListaClasse[c][1]+ListaClasse[c][2])/2:.2f}')
print("=-"*20)
while True:
    NotaDesejada = int(input("Digite o N° do aluno que deseja ver as suas respectivas notas [999 interrompe]: "))
    if NotaDesejada == 999:
        break
    print(f"NOTAS DO ALUNO {ListaClasse[NotaDesejada][0].upper()}")
    print(f'N1: {ListaClasse[NotaDesejada][1]}')
    print(f'N2: {ListaClasse[NotaDesejada][2]}')