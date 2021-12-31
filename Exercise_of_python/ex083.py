print('\033[1;93m-=-\033[m'*15)
print(f'\033[1;31m{"VALIDING MATHEMATICAL EXPRESSIONS":^45}\033[m',)
print('\033[1;93m-=-\033[m'*15)

expression = str(input('Type a expression: '))
o_par = 0
c_par = 0

for l in expression:
    if l == '(':
        o_par += 1
    elif l == ')' and o_par > 0:
        o_par -= 1

if o_par == 0:
    print('\033[1;94mYour expression is valid!\033[m')
else:
    print('\033[1;91mYou expression not is valid!\033[m')
