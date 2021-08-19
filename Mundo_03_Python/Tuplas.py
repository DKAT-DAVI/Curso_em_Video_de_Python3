print('\033[1;93m=-=-=-=- \033[1;94mAula de tuplas \033[1;93m=-=-=-=\033[m')
#Tuplas são imutáveis

lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
print(lanche[2])
print(lanche[0:2])
print(lanche[1:])
print(lanche[-1])
print(len(lanche))

print(' ')

lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
for c in lanche:
    if c == 'suco':
        print(f'Eu vou tomar {c}')
    else:
        print(f'Eu vou comer {c}')

print(' ')

for i in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[i]}')

print(' ')

for pos, eat in enumerate(lanche):
    print(f'0{pos+1} -> {eat}')

print(sorted(lanche))

a = (0, 2, 4, 6, 8)
b = (1, 3, 5, 7, 9)
d = a + b
print(sorted(d))

print(' ')

print(d.count(8))
print(sorted(d).index(8))

print(' \n ')

pessoa = ('Davi', '15', 'M', 63.5)
for p in pessoa:
    print(f'{p}')

del(lanche)
