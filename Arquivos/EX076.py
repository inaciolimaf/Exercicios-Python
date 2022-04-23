tupla=('lapís', 12,
       'caneta', 13,
       'borracha', 1)
for c in range(0,len(tupla)):
    if c%2==0:
        print(f'{tupla[c]:.<20}', end='')
    else:print(f'R$ {tupla[c]: >7.2f}')