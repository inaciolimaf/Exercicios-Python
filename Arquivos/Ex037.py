numero=int(input('Digite um número:'))
print('''Escolha uma das opções:
[1] para binário
[2] para octal
[3] para hexadecimal''')
resposta=int(input('Sua opção:'))
if resposta==1:
    print('O número {} em binário é {}'.format(numero, bin(numero)[2:]))
elif resposta==2:
    print('O número {} em octal é {}'.format(numero, oct(numero)[2:]))
elif resposta==3:
    print('O número {} convertido para hexadecimal é {}'.format(numero, hex(numero)[2:]))
else:
    print('Opção inválida tente denovo')
