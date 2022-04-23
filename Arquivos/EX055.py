maior=0
menor=0
for num in range(1,6):
    peso=int(input('Peso da {}° passoa:'.format(num)))
    if peso>maior:
        maior=peso
        if num == 1:
            menor = peso
    elif peso<menor:
        menor=peso

print(maior)
print(menor)

