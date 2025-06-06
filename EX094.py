Pessoas = list()
cont = 1
media = 0
while True:
    Nome = str(input("Digite o nome: "))
    Sexo = str(input("Digite o sexo: ")).upper()
    Idade = int(input("Digite a idade: "))
    Pessoa = {"Nome":Nome, "Sexo": Sexo, "Idade": Idade}
    Pessoas.append(Pessoa)
    media += Idade
    Pergunta = str(input("Quer continuar? [S/N]: ")).upper()
    if Pergunta == "N":
        break
    cont += 1
print(f"TOTAL DE CADASTROS: {cont}")
print(f"A MÉDIA DE IDADE É: {media/cont:.1f}")
print(f"TODAS AS MULHERES: ", end="")
for c in range(0,cont):
    if Pessoas[c]["Sexo"] == "F":
        print(Pessoas[c]["Nome"], end=" ")
print(f"\nLISTA DE PESSOAS ACIMA DA MÉDIA")
print("NOME: ", end=" ")
for c in range(0,cont):
    if Pessoas[c]["Idade"] > media/cont:
        print(f"{Pessoas[c]["Nome"]}", end="  ")
print("\nIDADE: ", end=" ")
for c in range(0, cont):
    if Pessoas[c]["Idade"] > media / cont:
        print(f"{Pessoas[c]["Idade"]}", end="       ")
print("\nSEXO: ", end="  ")
for c in range(0, cont):
    if Pessoas[c]["Idade"] > media / cont:
        print(f"{Pessoas[c]["Sexo"]}", end="        ")