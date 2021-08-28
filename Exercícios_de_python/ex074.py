print('\033[1;93m-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\033[m')
print('\033[1;31m     MENOR E MAIOR VALORES\033[m')

from random import randint

num = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10),
       randint(0, 10))

print(f'Os valores sorteados foram {num}')
print(f'O maior valor foi {max(num)}')
print(f'O menor valor foi {min(num)}')



