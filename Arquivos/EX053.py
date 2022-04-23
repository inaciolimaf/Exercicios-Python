frase=str(input('Digite uma frase:').strip().upper())
separado=frase.split()
junto=''.join(separado)
inverso=''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print('O palímdromo de {} é {}'.format(junto, inverso))
if inverso==junto:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')