from random import randint
print('\033[1;93m-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\033[m')
print('\033[1;31m     JOGO DE PAR OU ÍMPAR\033[m')
print('\033[1;93m-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\033[m')
venceu = 0
while True:
    escolha = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    while escolha not in 'Pp' and escolha not in 'ÍíIi':
        print('ESCOLHA INVÁLIDA! TENTE NOVAMENTE!')
        escolha = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    jogador = int(input('Digite um número: '))

    pc = randint(0, 10)
    resultado = jogador + pc

    if resultado % 2 == 0:
        if escolha in 'Pp':
            print('='*50)
            print(f'Você jogou {jogador} e o computador jogou {pc}. Total {resultado} = PAR')
            print('='*50)
            print('VOCÊ GANHOU!')
            print('=-'*15)
            venceu += 1
        elif escolha in 'ÍíIi':
            print('='*50)
            print(f'Você jogor {jogador} e o computador jogou {pc}. Total {resultado} = PAR')
            print('='*50)
            print('VOCÊ PERDEU!')
            print('=-'*15)
            break
    if resultado % 2 != 0:
        if escolha in 'Pp':
            print('='*50)
            print(f'Você jogou {jogador} e o computador jogou {pc}. Total {resultado} = ÍMPAR')
            print('='*50)
            print('VOCÊ PERDEU!')
            break
        elif escolha in 'ÍíIi':
            print('='*50)
            print(f'Você jogor {jogador} e o computador jogou {pc}. Total {resultado} = ÍMPAR')
            print('='*50)
            print('VOCÊ GANHOU!')
            venceu += 1
print(f'GAME OVER! Você venceu {venceu} vezes.')
