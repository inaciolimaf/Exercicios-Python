n=20
sexo=str(input('Informe seu sexo: [M/F]'))
if sexo in 'Mm''Ff':
    n = 0
while n==20:
    sexo=str(input('Dados invalidos. Informe seu sexo: [M/F]'))
    if sexo in 'Mm''Ff':
        n=0
print('Sexo {} registrado'.format(sexo))
