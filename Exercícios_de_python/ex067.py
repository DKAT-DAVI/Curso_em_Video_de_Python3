print('\033[1;93m-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\033[m')
print('\033[1;31m         TABUADA v3.0\033[m')
print('\033[1;93m-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\033[m')
while True:
    num = int(input('Quer ver a tabuada de qual valor: '))
    if num < 0:
        break
    print('\033[1;94m-=-=-=-=-=-=-=-=\033[m')
    for i in range(1, 11):
        print(f'{num} x {i} = {num * i}')
    print('\033[1;94m-=-=-=-=-=-=-=-=\033[m')
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')