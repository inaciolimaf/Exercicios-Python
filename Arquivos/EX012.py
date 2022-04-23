preço = float(input('Qual é o preço do produto? R$'))
desconto = float(input('Qual é o desconto, em porcentagem?'))
print('O produto que custava R${}, na promoção com desconto de {}% vai custar R${:.2f}.'.format(preço, desconto, preço*((100-desconto)/100)))
