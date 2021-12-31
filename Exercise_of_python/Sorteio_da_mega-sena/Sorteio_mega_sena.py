from random import randint
from time import sleep

print('\033[1;94m***\033[m'*15)
print(f'\033[1;93m{"GERADOR DE NÚMEROS DA MEGA-SENA":^45}\033[m',)
print('\033[1;94m***\033[m'*15)

cont = int(input('\033[1;92mQuantos jogos serão sorteados? '))

jogo = []

print('\033[1;94m***\033[m'*15)
print(f'\033[1;93m{f"RESULTADOS DOS {cont} SORTEIOS":^45}\033[m',)
print('\033[1;94m***\033[m'*15)

for i in range(0, cont):
    while len(jogo) != 6:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
    jogo.sort()
    print(f'\033[1;92m{i+1}º JOGO: ', end=' ')
    for n in jogo:
        print(f'{n:^4} ', end=' ')
    print('')
    jogo.clear()
    sleep(1)
print('\033[1;94m***\033[m'*15)
print('\033[1;93mBOA SORTE!')
