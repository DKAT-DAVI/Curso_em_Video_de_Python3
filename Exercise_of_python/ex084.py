print('\033[1;93m-=-\033[m' * 15)
print(f'\033[1;31m{"COMPOSITE LIST AND DATA ANALYSIS":^45}\033[m', )
print('\033[1;93m-=-\033[m' * 15)

people = [[], []]
largest = smallest = 0
big = []
little = []

while True:
    name = str(input('NAME: '))
    people[0].append(name)
    weight = float(input('WEIGHT: '))
    people[1].append(weight)

    if len(people[1]) == 1:
        largest = smallest = weight
    else:
        if weight > largest:
            largest = weight
        if weight < smallest:
            smallest = weight

    option = str(input('Do you want continue?[Y/N] ')).upper()[0]
    if option == 'N':
        break

print('\033[1;93m-=-\033[m' * 15)

for n in range(0, len(people[1])):
    if people[1][n] == largest:
        big.append(people[0][n])
    elif people[1][n] == smallest:
        little.append(people[0][n])

print(f'In all you resgistered {len(people[0])} people')
print(f'The largest weight was {largest}Kg of {big}')
print(f'The smallest weight was {smallest}Kg of {little}')
