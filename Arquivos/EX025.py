nome=str(input('Qual é o seu nome completo?')).strip().upper()
SepNome=nome.split()
Cont=SepNome.count('SILVA')
print('Seu nome tem SILVA?', end='')
print(Cont==1)