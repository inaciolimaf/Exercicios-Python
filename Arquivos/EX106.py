def ajuda(comand):
    print(f'Acessando manual do comando {comand}')
    help(comand)
def título(msg):
    tamnho=len(msg)
    print('-='*tamnho)
    print(msg)
    print('-='*tamnho)

while True:
    título('Sistema de ajuda')
    comando=str(input('Função ou bibliotca:'))
    if comando.strip().upper()=='FIM':
        break
    else:
        ajuda(comando)

título('Até logo')