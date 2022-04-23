import random
PrimeiroA = input('Primeiro aluno:')
SegundoA = input('Segundo aluno:')
TerceiroA = input('Terceiro aluno:')
QuartoA = input('Quarto aluno')
QuintoA = input('Quinto aluno:')
lista=[PrimeiroA, SegundoA, TerceiroA, QuartoA, QuintoA]
print('O aluno escolhido é {}'.format(random.choice(lista)))