NumerosTupla = ("zero", "um", "dois", 'três' , 'quatro', 'cinco' ,
                'seis' ,'sete', 'oito' ,'nove' ,'dez' ,'onze' ,'doze', 'treze' ,'catorze' ,'quinze',
                'dezesseis' ,'dezessete' ,'dezoito', 'dezenove' ,'vinte')
while True:
    NumEscolha = int(input("Digite um número entre 0 e 20: "))
    if NumEscolha >0 and NumEscolha <=20:
        break
    else:
        print("Valor incorreto! Tente outra vez. ", end='')
print(f"O número digitado foi {NumerosTupla[NumEscolha]}.")