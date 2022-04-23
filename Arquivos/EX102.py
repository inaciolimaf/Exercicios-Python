def fatorial(num, show=False):
    """
    Cálculo de fatorial
    :param num: Número para calcular o fatorial
    :param show: Mostrar o cálculo
    :return: Sem retorno
    """
    print('=-'*40)
    resul=1
    num1=num
    for c in range(0,num-1):
        resul*=num
        num-=1
    if show==False:
        print(resul)
    elif show==True:
        print(num1, end='')
        num1-=1
        for c in range(0, num1):
            print(f' x {num1}',end='')
            num1-=1
        print(f' = {resul}')

fatorial(4, show=False)
