print('='*40)
print('{:^40}'.format('10 TERMOS DE UMA P.A'))
print('='*40)
pri=int(input('Primeiro termo:'))
r=int(input('Razão:'))
for i in range(0,6):
    print(pri+r*i, end=' ➡')
print('FIM')