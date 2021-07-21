print('\033[1;93m-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\033[m')
print('\033[1;31m TRATANDO VÁRIOS VALORES v1.0\033[m')
print('\033[1;93m-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\033[m')

parar = int(input('Digite um número [999 para parar]: '))
cont = 0
soma = parar
while parar != 999:
    parar = int(input('Digite um número [999 para parar]: '))
    cont += 1
    soma += parar
print(f'Você digitou {cont} números e a soma entre eles foi {soma - 999}')
