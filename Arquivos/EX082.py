lista=[]
listapar=[]
listaimpar=[]
while True:
    num=int(input('Digite um número:'))
    lista.append(num)
    if num%2==0:
        listapar.append(num)
    elif num%2==1:
        listaimpar.append(num)
    resp=str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp=='N':
        break
print(f'A lista completa é {lista}')
print(f'A lista dos números pares é {listapar}')
print(f'A lista dos números ímpares é {listaimpar}')