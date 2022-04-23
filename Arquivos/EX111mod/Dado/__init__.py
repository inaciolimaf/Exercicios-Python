def leiadinheiro(entrada):
    while True:
        resp=str(input(entrada)).replace(',', '.').strip()
        if resp.isalpha() or resp=='':
            print('ERRO! Digite um valor válido.')
        else:
            resp = float(resp)
            return resp

