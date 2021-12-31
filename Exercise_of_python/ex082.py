print('\033[1;93m-=-\033[m'*15)
print(f'\033[1;31m{"DIVIDING VALUES IN MULTIPLE LISTS":^45}\033[m')
print('\033[1;93m-=-\033[m'*15)

numbers = []
odd = []
even = []

while True:
    numbers.append(int(input('Type a number for add in list: ')))
    stop = str(input('Do you want continue?[Y/N] ')).upper()[0]
    if stop in 'N':
        break

for n in numbers:
    if n % 2 == 0:
        even.append(n)
    elif n % 2 == 1:
        odd.append(n)

print(f'The complete list is {numbers}')
print(f'The even list is {even}')
print(f'The odd list is {odd}')
