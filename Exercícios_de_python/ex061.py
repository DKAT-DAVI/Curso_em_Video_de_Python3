print('\033[1;93m-=-=-=-=-=-=-=-=-=-=-=-=-=-\033[m')
print('\033[1;31m      GERADOR DE PA\033[m')
print('\033[1;93m-=-=-=-=-=-=-=-=-=-=-=-=-=-\033[m')
termo = int(input('Primeiro Termo: '))
razão = int(input('Razão da PA: '))
cont = 0
while cont <= 9:
    print(termo, end=' ')
    print('->', end=' ')
    termo += razão
    cont += 1
print('FIM')
