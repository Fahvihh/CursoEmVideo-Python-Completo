print(" "*12,"PADARIA DO SEU ZÉZÃO")
print("=^"*25)
Listagem = ('Pão', 1.00, 'Biscoito', 3.50, 'Café', 2.00, 'Misto', 7.49, 'Pão de Queijo', 3.00,
            'Salgadinho', 6.79, 'Leite', 5.50, 'Muçarela', 7.89, 'Macarrão', 9.99, 'Sucrilhos', 8.78)
Produtos = Listagem[0::2]
Preco = Listagem[1::2]
for c in range(0,10):
    print(f"{Produtos[c]:13}", "..."*9, f"R${Preco[c]:.2f}")
print("=^"*25)
