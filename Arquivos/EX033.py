a=int(input('Primeiro volor:'))
b=int(input('Segundo valor:'))
c=int(input('Terceiro valor:'))
if a<b and a<c:
    menor = a
elif b<a and b<c:
    menor = b
elif c<a and c<b:
    menor= c

if a>c and a>b:
    maior=a
elif b>a and b>c:
    maior=b
elif c>a and c>b:
    maior=c
print('O menor é {}'.format(menor))
print('O maior é {}'.format(maior))