import random
PrimeiroA = input('Primeiro aluno:')
SegundoA = input('Segundo aluno:')
TerceiroA = input('Terceiro aluno:')
QuartoA = input('Quarto aluno')
QuintoA = input('Quinto aluno:')
lista=[PrimeiroA, SegundoA, TerceiroA, QuartoA, QuintoA]
NLista=random.choices(lista,k=5)
print('A ordem da lista será:')
print(NLista)