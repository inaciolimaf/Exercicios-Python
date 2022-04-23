from random import randint
def sorte(lista):
    for c in range(0,5):
        lista.append(randint(1,10))
    print('Sorteando 5 valores para a lista: ', end='')
    for c in lista:
        print(f'{c} ', end='')
def soma(lista):
    soma1=0
    for c in lista:
        if c%2==0:
            soma1+=c
    print()
    print(f'A soma dos números pares é {soma1}')


numeros=[]
sorte(numeros)
soma(numeros)