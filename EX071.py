print("-_" *28)
print(" "*18, "BANCO MUVACTION")
print("-_" *28)
print("Lembre-se que só trabalhamos com números inteiros!\n"
      "E as notas disponíveis são de R$50, R$20, R$10, R$1")
Valor = int(input("Digite o valor a ser sacado: R$"))
print("-_" *28)
Tot = Valor
TotCedula = 0
Cedula = 50
while True:
    if Tot >= Cedula:
        Tot -= Cedula
        TotCedula += 1
    else:
        if TotCedula >0:
            print(F"Total de {TotCedula} cédulas de R${Cedula}")
        if Cedula == 50:
            Cedula = 20
        elif Cedula ==20:
            Cedula = 10
        elif Cedula == 10:
            Cedula = 1
        TotCedula = 0
        if Tot == 0:
            break
print("-_" *28)
print(" "*18, "VOLTE SEMPRE!!")
print("-_" *28)