print('\033[1;93m-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\033[m')
print('\033[1;31m       NÚMERO POR EXTENSO\033[m')
print('\033[1;93m-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\033[m')

valor = ('zero', 'um', 'dois', 'três', 'quatro',
         'cinco', 'seis', 'sete', 'oito', 'nove',
         'dez', 'onze', 'doze', 'treze', 'quatorze',
         'quinze', 'dezesseis', 'dezessete', 'dezoito',
         'dezenove', 'vinte')
while True:
    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if 20 >= num >= 0:
            break
        print('Tente novamente.', end=' ')
    print(f'Você digitou o número {valor[num]}.')
    while True:
        op = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
        if op not in 'SN':
            print('Tente novamente.', end=' ')
        else:
            break
    if op in 'Nn':
        break
print('VALEU! ATÉ A PRÓXIMA!')


