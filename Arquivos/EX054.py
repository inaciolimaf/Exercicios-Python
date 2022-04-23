from datetime import date
maior=0
menor=0
ano= date.today().year
for i in range(1,8):
    j=int(input('Em que ano a {}º pessoa nasceu?'.format(i)))
    if ano-j>18:
        maior+=1
    else:
        menor+=1
print('''Existem:
{} MAIORES de idade 
{} MENORES de idade
'''.format(maior, menor))
