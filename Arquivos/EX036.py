valor = float(input('Qual é o valor da casa? R$'))
salario = float(input('Salário do comprador:'))
anos = float(input('Quantos anos de financiamento?'))
prestação=valor/(12*anos)
print('Para pasgar uma casa de R${:.2f} em {:.0f} anos e a prestação será de R${:.2f}'.format(valor, anos, prestação))
if prestação<salario*0.3:
    print('Empréstimo APROVADO')
else:
    print('Empréstimo NEGADO')