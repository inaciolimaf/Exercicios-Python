def notas(*num, sit=False):
    """
    Função para analisar notas
    :param num: notas dos alunos
    :param sit: opicional indicando, insicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a turma
    """
    result={}
    média = menor = maior = cont = 0
    for c in num:
        if c > maior:
            maior = c
        if cont == 0:
            menor = c
        elif c < menor:
            menor = c
        média += c
        cont += 1
    média /= len(num)
    if sit == True:
        if 6 <= média < 7:
            situação = 'Média'
        elif média > 7:
            situação = 'Boa'
        elif média < 6:
            situação = 'Ruim'
    result['Total'] = cont
    result['Média']=média
    result['Maior']=maior
    result['Menor']=menor
    result['Situação']=situação
    return result


resultado=notas(7.5, 7.9, 3, 6.5, sit=True)
print(resultado)
