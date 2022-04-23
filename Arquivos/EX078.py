listateste=[]
for c in  range(0,5):
    listateste.append(int(input(f'Digite o termo na posição {c}:')))
print(f'Você digitou os valores{listateste}')
listacerto=listateste[:]
listacerto.sort()
print(f'O maior valor digitado foi {listacerto[-1]} e ele aparece nas posições: ', end='')
for c in  range(0,len(listacerto)):
    if listateste[c]==listacerto[-1]:
        print(c, end='')
print(f'\nO menor valor digitado foi {listacerto[0]} e ele aparece nas posições: ', end='')
for c in range(0, len(listacerto)):
    if listateste[c]==listacerto[0]:
        print(c, end='')