preco = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO1\n[ 1 ] à vista DINHEIRO/CHEQUE\n[ 2 ] à vista no cartão\n[ 3 ] 2x no cartão\n[ 4 ] 3x ou mais no cartão')
resp=int(input('Sua opção:'))
if resp==1:
    Novo= 0.9 * preco
elif resp==2:
    Novo= 0.95 * preco
elif resp==3:
    Novo=preco
elif resp==4:
    Novo= preco * 1.2
print('Sua compra de R${} vai custar R${} no final'.format(preco, Novo))