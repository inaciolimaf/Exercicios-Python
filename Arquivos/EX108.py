import ModEX108

num=float(input('Digite o preço: R$'))
print(f'O dobro de {ModEX108.moeda(num)} é {ModEX108.dobro(num)}')
print(f'A metade de {ModEX108.moeda(num)} é {ModEX108.metade(num)}')
print(f'Aumentando 10%, temos {ModEX108.aumento10(num)}')