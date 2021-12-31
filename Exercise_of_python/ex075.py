print('\033[1;93m-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\033[m')
print('\033[1;31m      DADOS EM UMA TUPLA\033[m')
print('\033[1;93m-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\033[m')
num = (int(input('Digite um número: ')), int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')), int(input('Digite o último número: ')))
impar = 0
print(f'Você digitou os números: {num}')
print(f'O número 9 apareceu {num.count(9)} vezes')
try:
       print(f'O números 3 foi digitado na {num.index(3)+1}ª posição')
except:
       print('Não foi digitado número 3')
print('Os valores pares digitados foram: ', end='')
for n in num:
       if n % 2 != 0:
              impar += 1
if impar == 4:
       print('Não foi digitado nenhum número par')
else:
       for n in num:
              if n % 2 == 0:
                     print(n, end=' ')



