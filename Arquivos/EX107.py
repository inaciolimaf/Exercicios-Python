import ModEX107


num=float(input('Digite o preço: R$'))
print(f'O dobro de {num:.0f} é {ModEX107.dobro(num):.0f}')
print(f'A metade de {num:.0f} é {ModEX107.metade(num):.0f}')
print(f'Aumentando 10%, temos {ModEX107.aumento10(num):.2f}')