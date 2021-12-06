print('\033[1;93m-=-\033[m'*15)
print(f'\033[1;31m{"LARGEST AND SMALLEST ON THE LIST":^45}\033[m',)
print('\033[1;93m-=-\033[m'*15)

num = list()
for i in range(0, 5):
    num.append(int(input(f'Enter a number for position {i}: ')))

print('\033[1;93m-=-\033[m'*15)

print(f'You typed the numbers {num}')
print(f"""The largest number typed was: {max(num)} in position {num.index(max(num))}
The smallest number typed was: {min(num)} in position {num.index(min(num))} """)

print('\033[1;93m-=-\033[m'*15)