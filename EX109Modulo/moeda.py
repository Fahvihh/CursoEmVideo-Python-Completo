def Moeda(numero):
    return f"R${numero:.2f}"
def aumentar(numero, Formatacao):
    numero = numero + (numero * 0.1)
    if Formatacao == True:
        Moeda(numero)
    return Moeda(numero)
def reduzir(numero, Formatacao):
    numero = numero - (numero * 0.13)
    if Formatacao == True:
        Moeda(numero)
    return Moeda(numero)
def dobro(numero, Formatacao):
    numero = numero * (2)
    if Formatacao == True:
        Moeda(numero)
    return Moeda(numero)
def metade(numero, Formatacao):
    numero = numero / 2
    if Formatacao == True:
        Moeda(numero)
    return Moeda(numero)