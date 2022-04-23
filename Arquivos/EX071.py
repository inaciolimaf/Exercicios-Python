print('='*40)
print('BANCO DO PETECA'.center(40,' '))
print('='*40)
valor=int(input('Que valor você quer sacar?'))
v100=valor//100
v50=(valor-v100*100)//50
valor=(valor-v100*100)
v20=(valor-v50*50)//20
valor=(valor-v50*50)
v10=(valor-v20*20)//10
valor=(valor-v20*20)
v5=(valor-v10*10)//5
valor=(valor-v10*10)
v2=(valor-v5*5)//2
valor=(valor-v5*5)
v1=(valor%2)
print(f'''Cédulas:
{v100} de 100 reais
{v50} de 50 reais
{v20} de 20 reais
{v10} de 10 reais
{v5} de 5 reais
{v2} de 2 reais
{v1} de 1 reais''')