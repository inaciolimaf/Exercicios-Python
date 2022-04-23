from random import randint
val = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('Os valores sorteados foram: ', end='')
for c in range(0, len(val)):
    print(f'{val[c]} ', end='')
print()
print(f'O maior valor sorteado foi {sorted(val)[-1]}')
print(f'O menor valor sorteado foi {sorted(val)[0]}')