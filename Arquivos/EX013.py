salario=float(input('Qual o salário do funcionário? R$'))
aumento=float(input('Qual é o aumento, em porcentagem(Esccreva apenas números)?'))
print('Um funcionário que ganhava R${}, com {}% de aumento, passa a receber R${:.2f}.'.format(salario, aumento, salario*((100+aumento)/100)))