print('\033[1;93m-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\033[m')
print('\033[1;31m  SEQUÊNCIA DE FIBONACCI v1.0\033[m')
print('\033[1;93m-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\033[m')
n = int(input('Quntos termos você quer exibir? '))
cont = 3
t1 = 0
t2 = 1
print(f'{t1} -> {t2} ->', end=' ')
while cont <= n:
    t3 = t1 + t2
    print(f'{t3} ->', end=' ')
    cont += 1
    t1 = t2
    t2 = t3
print('FIM!')
