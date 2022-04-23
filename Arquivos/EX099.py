def maior(*num):
    print('=-'*40)
    if len(num)>0:
        print(f'{num} Foram informados {len(num)} valores ao todo.')
    else:
        print('Não foram informados nenhum valor')
    maior=0
    for c in num:
        if c>maior:
            maior=c
    print(f'O maior é {maior}')
maior(2,3,4,5,6,7)
maior(6)
maior()