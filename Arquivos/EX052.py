num=int(input('Digite um valor:'))
n=0
print('O número {} foi divisivel por:'.format(num), end='')
for c in range(1, num+1):
    if num%c == 0:
        n+=1
        print(' {}, '.format(c), end='')
print()
if n==2:
    print('{} é primo'.format(num))
else:
    print('{} não é primo'.format(num))