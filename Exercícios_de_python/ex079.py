print('\033[1;93m-=-\033[m'*15)
print(f'\033[1;31m{"SINGLE VALORS IN LIST":^45}\033[m',)
print('\033[1;93m-=-\033[m'*15)

valors = list()
opt = ' '

while True:
    print('\033[1;94m-=-\033[m' * 15)

    add = (int(input('Type a value: ')))
    if add not in valors:
        valors.append(add)
        print('Value added successfully...')

        print('\033[1;94m-=-\033[m' * 15)

    else:
        print('Repeated value! Cannot be added.')

        print('\033[1;91m-=-\033[m' * 15)
    while opt not in 'NS':
        opt = str(input(('Do you continue?[S/N] '))).upper()[0]
    if opt in 'N':
        print('\033[1;93m-=-\033[m' * 15)
        break
    opt = ' '

valors.sort()

print('You entered the valors: ', end=' ')

for v in valors:
    print(v, end=' ')
