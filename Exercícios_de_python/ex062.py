print('\033[1;93m-=-=-=-=-=-=-=-=-=-=-=-=-=-\033[m')
print('\033[1;31m   SUPER GERADOR DE PA\033[m')
print('\033[1;93m-=-=-=-=-=-=-=-=-=-=-=-=-=-\033[m')
termo = int(input('Primeiro Termo: '))
razão = int(input('Razão da PA: '))
cont = 1
num = 0
mais = 10
while mais != 0:
    num += mais
    while cont <= num:
        print(termo, end=' ')
        print('->', end=' ')
        termo += razão
        cont += 1
    print('PAUSA\n')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressaõ finalizada com {num} termos mostrados')
