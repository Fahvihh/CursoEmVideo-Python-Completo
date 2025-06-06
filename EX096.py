def area(largura, comprimento):
    totalm2 = largura * comprimento
    print(f'A área total é: {totalm2:.1f} m²')


area(float(input("Digite a largura: ")), float(input("Digite o comprimento: ")))