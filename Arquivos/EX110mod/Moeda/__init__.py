def moeda(preço):
    return f'R$ {preço:.2f}'.replace('.',',')


def resumo(num, aumento, desconto):
    print('-='*15)
    print(f'{"Resumo do valor":^30}')
    print('-='*15)
    print(f'{"Preço analisado:":<20}', end='')
    print(moeda(num))
    print(f'{"Dobro do preço:":<20}', end='')
    print(moeda(num*2))
    print(f'{"Metade do preço:":<20}', end='')
    print(moeda(num/2))
    print(f'{f"{aumento}% de aumento:":<20}', end='')
    print(moeda(num*(100+aumento)/100))
    print(f'{f"{desconto}% de desconto:":<20}', end='')
    print(moeda(num*(100-desconto)/100))