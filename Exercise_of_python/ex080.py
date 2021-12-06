print('\033[1;93m-=-\033[m'*15)
print(f'\033[1;31m{"ORDERED LIST WITHOUT REPETITIONS":^45}\033[m',)
print('\033[1;93m-=-\033[m'*15)

numbers = list()
for i in range(0, 5):
    n = int(input('Type a number: '))
    if i == 0 or n > numbers[-1]:
        numbers.insert(4, n)
        print('Value added to the end of the list.')
    else:
        pos = 0
        while pos < len(numbers):
            if n <= numbers[pos]:
                numbers.insert(pos, n)
                print(f'Value added in the position {pos}')
                break
            pos += 1

print('The added values were ', end='')
for n in numbers:
    print(f'{n} ', end='')
