teste = input('Digite algo:')
print('O tipo primitivo é {}'.format(type(teste)))
print('Só tem espaços:{}'.format(teste.isspace()))
print('É um número: {}'.format(teste.isnumeric()))
print('É alfabético: {}'.format(teste.isalpha()))
print('É alfanumérico: {}'.format(teste.isalnum()))
print('Está em maiúsculas: {}'.format(teste.isupper()))
print('Está em minúsculas: {}'.format(teste.islower()))