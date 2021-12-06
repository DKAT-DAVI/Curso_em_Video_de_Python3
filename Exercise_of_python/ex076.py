print('\033[1;93m|\033[m', end='')
print('\033[1;93m=\033[m'*40, end='')
print('\033[1;93m|\033[m')
print('\033[1;93m|\033[m', end='')
print(f'\033[1;31m{"LISTAGEM DE PREÇOS":^40}\033[m', end='')
print('\033[1;93m|\033[m')
print('\033[1;93m|\033[m', end='')
print('\033[1;93m=\033[m'*40, end='')
print('\033[1;93m|\033[m')
lista = ("Lápis", 1.75, "Borracha", 2.00, "Caderno", 15.90, "Estojo", 25.00,
         "Transferidor", 4.20, "Compasso", 9.99, "Mochila", 120.32, "Canetas", 22.30,
         "Livro", 35.90,)
for p in range(0, len(lista)):
    if p % 2 == 0:
        print('\033[1;93m|\033[m', end='')
        print(f'\033[1;94m{lista[p]:.<30}', end='')
    elif p % 2 != 0:
        print(f'R${lista[p]:>8.2f}', end='')
        print('\033[1;93m|\033[m')
print('\033[1;93m|\033[m', end='')
print('\033[1;93m=\033[m'*40, end='')
print('\033[1;93m|\033[m')

