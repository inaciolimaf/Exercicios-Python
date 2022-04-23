from random import randint
print('''Sou seu computador...
Acabei de pensar em um número entre 1 e 1000
Será que você consegue adivinhar qual foi?''')
Esc=0
Comp=randint(1, 1000)
while Esc != Comp:
    Esc=int(input('Qual é o seu palpite?'))
    if Esc>Comp:
        print('Menos... Tente mais uma vez.')
    elif Esc<Comp:
        print('Mais... Tente mais uma vez.')
print('ACERTOU')
