num=cont=total=0
while True:
    num=int(input('Digite um valor (999 para parar):'))
    if num==999:
        break
    total+=num
    cont+=1
print(f'Você digitou {cont} valores e a soma entre eles é {total}.')