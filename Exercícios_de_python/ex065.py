print('\033[1;93m-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\033[m')
print('\033[1;31m     MAIOR E MENOR VALORES\033[m')
print('\033[1;93m-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\033[m')

media = num = cont = maior = menor = 0
seguir = 'S'
while seguir == 'S':
    num = int(input('Digite um número: '))
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    seguir = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    cont += 1
    media += num
print('Você digitou {} números e a média foi {:.2f}'.format(cont, media // cont))
print(f'O maior valor foi {maior} e o menor valor foi {menor}')
