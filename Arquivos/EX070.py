print('-'*40)
print('LOJA SUPER BARATÃO'.center(40))
print('-'*40)
total=MaisTotal=menor=menorP=c=0
while True:
    nome=str(input('Nome do produto:'))
    preço=int(input('Preço: R$'))
    count=str(input('Queer continuar? [S/N]')).upper().strip()[0]
    while count not in 'SN':
        count=str(input('Valor inválido: Quer continuar? [S/N]'))
    total+=preço
    if preço>1000:
        MaisTotal+=1
    if c==0:
        menorP=preço
    if preço<menorP:
        menorP=preço
        menor = nome
    if count == 'N':
        break
    c+=1
print('FIM DO PROGRAMA'.center(40, '-'))
print(f'O total da compra foi {total}')
if MaisTotal==0:
    print('Não temos nenhum produto custando mais de R$ 1000.')
elif MaisTotal==1:
    print('Temos um produto custando mais de R$ 1000.')
elif MaisTotal>1:
    print(f'Temos {MaisTotal} produtos custando mais de R$ 1000.')
print(f'O produto mais barato foi a {menor} e custa R$ {menorP}')