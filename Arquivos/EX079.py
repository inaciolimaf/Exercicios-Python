lista=[]
while True:
    num=int(input('Digite um valor:'))
    if lista.count(num)==0:
        lista.append(num)
        print('Valor adicionado com sucesso...')
    elif lista.count(num)>0:
        print('Valor duplicado. Não adiconado')
    resp=str(input('Quer continuar? [S/N]')).strip().upper()
    if resp=='N':
        break
lista.sort()
print(lista)