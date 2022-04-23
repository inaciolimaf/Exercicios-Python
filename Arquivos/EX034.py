sal=float(input('Qual é o salário do funcionário? R$'))
if sal<=1250:
    print('Quem ganhava R${} passa a ganhar R${:.2f}'.format(sal, sal*1.15))
else:
    print('Quem ganhava R${} passa a ganhar R${:.2f}'.format(sal, sal*1.1))
