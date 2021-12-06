print('\033[1;93m-=-\033[m'*15)
print(f'\033[1;31m{"EXTRACTING DATA FROM A LIST":^45}\033[m',)
print('\033[1;93m-=-\033[m'*15)

numbers = []
cont = 0

while True:
    numbers.append(int(input('Type a value: ')))
    cont += 1
    opt = str(input('Do you want continue? [S/N]: ')).upper()[0]
    if opt == 'N':
        break

print(f'\nYou typed {cont} valors')

numbers.sort(reverse=True)
print(f'The values in descending order are: {numbers}')

if 5 in numbers:
    print('Number 5 is on that list!')
else:
    print('Number 5 is not on that list!')

