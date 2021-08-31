print('\033[1;93m-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\033[m')
print('\033[1;31m       CONTANDO VOGAIS\033[m')
print('\033[1;93m-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\033[m')
words = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS',
         'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMAR', 'FUTURO')
for pos in words:
    print(f'\nNa palavra {pos} temos as vogais: ', end='')
    for letra in pos:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=' ')
