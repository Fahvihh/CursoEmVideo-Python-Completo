def Moeda(numero):
    return f"R${numero:.2f}"
def aumentar(numero, Aumento, Formatacao):
    numero = numero + (numero * Aumento/100)
    if Formatacao == True:
        Moeda(numero)
    return Moeda(numero)
def reduzir(numero, Reducao, Formatacao):
    numero = numero - (numero * Reducao/100)
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