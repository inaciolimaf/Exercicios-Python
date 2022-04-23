matriz=[[],[],[]]
pares=ter=maior=0
for i in range(0,3):
    for c in range(0,3):
        n=int(input(f'Digite um valor para a posição {i}, {c}:'))
        if n%2==0:
            pares+=n
        if c==2:
            ter+=n
        if i==1:
            if n>maior:
                maior=n
        matriz[i].append(n)
print('=-'*30)
for i in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[i][c]}]',end='')
    print()
print('=-'*30)
print(f'A soma dos valores pares é {pares}')
print(f'A soma dos valores da terceira coluna é {ter}')
print(f'O maior valor da segunda coluna é {maior}')