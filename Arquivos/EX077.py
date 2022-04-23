tupla=('APRENDER', 'PROGRAMAR',
       'LINGUAGEM', 'PYTHON', 'CURSO',
       'GRÁTIS', 'ESTUDAR', 'PRATICAR',
       'TRABALHO', 'MERCADO', 'PROGAMADOR',
       'FUTURO')
for c in tupla:
    print(f'Na palavra {c} temos',end='')
    for letre in c:
        if letre in 'AEIOU':
            print(f' {letre}', end='')
    print()