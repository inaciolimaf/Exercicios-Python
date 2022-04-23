from  math import factorial
fat=int(input('Digita um número para calcular o fatorial:'))
print('Calculando {}! = {}'.format(fat, fat),end='')
vari=fat
while vari>1:
    vari-=1
    print('x{}'.format(vari), end='')
print('={}'.format(factorial(fat)))