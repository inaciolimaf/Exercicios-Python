exp=str(input('Digite a sua expressão:'))
contAber=exp.count('(')
contFech=exp.count(')')
if contFech==contAber:
    print('Sua expressão é válida.')
else:
    print('Sua expressão é inválida.')