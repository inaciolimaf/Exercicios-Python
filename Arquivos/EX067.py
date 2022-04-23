while True:
    tab=int(input('Quer ver a tabuada de qual valor?'))
    if tab <= 0:
        print('Programa de tabuada ENCERRADO. Volte sempre.')
        break
    print('-'*20)

    for c in range(1, 11):
        print(f'{tab} x {c} = {tab*c}')
    print('-'*20)

