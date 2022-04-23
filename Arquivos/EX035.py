print('-=-'*10)
print('Analisador de Triângulos')
print('-=-'*10)
a=float(input('Primeiro segmento:'))
b=float(input('Segundo segmento:'))
c=float(input('Terceiro segmento:'))
if a+b>c and a+c>b and b+c>a:
    print('Esses segmentos PODEM formar triângulos.')
else:
    print('Esses segmentos NÃO PODEM formar triângulos.')
