lista=[]
for c in range(0,5):
    num=int(input('Digite um valor:'))
    lista.append(num)
    lista.sort()
    if lista.index(num)==c:
        print('Valor adicionado ao final da fila')
    else:
        print(f'Valor adicionado na posição {lista.index(num)}')
print(f'Os valores digitados em ordem foram {lista}')
