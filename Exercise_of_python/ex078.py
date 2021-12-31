print('\033[1;93m-=-\033[m' * 15)
print(f'\033[1;31m{"LARGEST AND SMALLEST ON THE LIST":^45}\033[m', )
print('\033[1;93m-=-\033[m' * 15)

numbers = list()
largest = 0
big_position = list()
small_position = list()

numbers.append(int(input(f'Type a number for the position {0}: ')))
smallest = numbers[0]

for i in range(1, 5):
    numbers.append(int(input(f'Type a number for the position {i}: ')))
    if numbers[i] > largest:
        largest = numbers[i]
    if numbers[i] < smallest:
        smallest = numbers[i]

print('-=-' * 15)
print('You entered the valors: ', end='')

for n in numbers:
    print(n, end=' ')

for i in range(0, 5):
    if numbers[i] == largest:
        big_position.append(i)
    if numbers[i] == smallest:
        small_position.append(i)

print(f'\nThe largest number entered was: {largest} in the positions ', end='')
for n in big_position:
    print(f'{n}... ', end='')

print(f'\nThe smallest number entered was: {smallest} in the positions ', end='')
for n in small_position:
    print(f'{n}... ', end='')
