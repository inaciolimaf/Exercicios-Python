lista=[[],[]]
for i in range(0,8):
    n=int(input(f'Digite o {i+1} valor:'))
    if n%2==1:
        lista[1].append(n)
    else:
        lista[0].append(n)
lista[0].sort()
lista[1].sort()
print(f'Os valores pares digitados foram: {lista[0]}')
print(f'Os valores pares digitados foram: {lista[1]}')