lista= []
c=0
while True:
    num=int(input('Digite um valor:'))
    c+=1
    lista.append(num)
    resp=str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if resp=='N':
        break
print(f'Você digitou {c} elementos')
lista.sort(reverse=True)
print(f'Os valores em ordem crescente são: {lista}')
count=lista.count(5)
if count==0:
    print('O valor 5 não foi encontrado.')
elif count>0:
    print('O valor 5 foi encontrado')