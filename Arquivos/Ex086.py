matriz=[[],[],[]]
for i in range(0,3):
    for c in range(0,3):
        n=int(input(f'Digite um valor para a posição {i}, {c}:'))
        matriz[i].append(n)
for i in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[i][c]}]',end='')
    print()