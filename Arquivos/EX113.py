def leiafloat(entrada):
    while True:
        try:
            resp=int(input(entrada))
        except (ValueError, TypeError):
            print('Digite um valor válido')
            continue
        else:
            return resp
n=leiafloat('Digite um valor:')
print(f'Você digitou {n}')