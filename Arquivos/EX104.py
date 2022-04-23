def leiaint(text):
    while True:
        n=str(input(text)).strip()
        if n.isnumeric():
            n=int(n)
            return n

        else:
            print('Valor inválido. Tente novamente')


j=leiaint('Digite apenas números:')
print(j)