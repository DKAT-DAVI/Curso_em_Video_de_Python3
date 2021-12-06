print('\033[1;93m-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\033[m')
print('\033[1;31m    ESTATÍSTICAS EM PRODUTO\033[m')
print('\033[1;93m-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\033[m')

from time import sleep

print('=' * 40)
msg = 'LOJAS PREÇO BAIXO'
print(f'{msg:^40}')
print('=' * 40)

cont = 0

nome = str(input('NOME DO PRODUTO: ')).upper()
mais_barato = nome

preco = float(input('PREÇO DO PRODUTO: R$'))

barato = total = preco

while True:
    if preco > 1000:
        cont += 1

    escolha = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while escolha not in 'N' and escolha not in 'S':
        escolha = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if escolha == 'N':
        break
    nome = str(input('NOME DO PRODUTO: ')).upper()

    preco = float(input('PREÇO DO PRODUTO: R$'))

    total += preco

    if preco < barato:
        barato = preco
        mais_barato = nome

print('\nFINALIZANDO COMPRA...')
sleep(3)
print(f"""O total da compra foi R${total:.2f}
Temos {cont} produtos custando mais de R$1000.00
O produto mais barato foi {mais_barato} que custa R${barato:.2f}""")
