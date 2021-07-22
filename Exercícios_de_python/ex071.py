print('\033[1;93m-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\033[m')
print('\033[1;31m SIMULADOR DE CAIXA ELETRÔNICO\033[m')
print('\033[1;93m-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\033[m')
print('=' * 40)
msg = 'BANCO DKAT'
print(f'{msg:^40}')
print('=' * 40)
valor = int(input('Qual valor você quer sacar? R$'))
total = valor
ced = 200
tot_ced = 0
while True:
    if total >= ced:
        total -= ced
        tot_ced += 1
    else:
        if tot_ced > 0:
            print(f'Total de {tot_ced} de R${ced}.00')
        if ced == 200:
            ced = 100
        elif ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 2
        elif ced == 2:
            ced = 1
        tot_ced = 0
        if total == 0:
            break
print('=' * 40)
print('Agradeçemos a preferência! Volte sempre!')
print('=' * 40)