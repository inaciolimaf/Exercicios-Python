Nome=str(input('Digite seu nome completo:')).strip()
Sepnome=Nome.split()
print('Muito prazer em te conhecer')
print('Seu primeiro nome é {}'.format(Sepnome[0]))
print('Seu úiltimo nome é {}'.format(Sepnome[len(Sepnome)-1]))
