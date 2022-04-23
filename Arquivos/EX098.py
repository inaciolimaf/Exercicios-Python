from time import sleep
def fort(a,b,c):
    for c in range(a, b+1, c):
        print(f'{c}  ', end='')
        sleep(0.4)
    print()


print('Contagem de 1 até 10 de 1 em 1')
fort(1,10, 1)
print('Agora é a sua fez de personalizar a contagem.')
a=int(input('Início:'))
b=int(input('Final:'))
c=int(input('Passo:'))
print(f'Contagem de {a} até {b} de {c} em {c}')
fort(a,b,c)