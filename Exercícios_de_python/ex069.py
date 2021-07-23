print('\033[1;93m-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\033[m')
print('\033[1;31m   ANÁLISE DE DADOS DO GRUPO\033[m')
print('\033[1;93m-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\033[m')

pessoas = homens = mulheres = 0

while True:
    print('=' * 30)
    msg = 'CADASTRO DE UMA PESSOA'
    print(f'{msg:^30}')
    print('=' * 30)

    idade = int(input('IDADE: '))

    if idade > 18:
        pessoas += 1

    sexo = str(input('SEXO: [M/F] ')).upper().strip()[0]
    while sexo not in 'M' and sexo not in 'F':
        sexo = str(input('SEXO: [M/F] ')).upper().strip()[0]

    if sexo == 'M':
        homens += 1

    if sexo == 'F' and idade > 20:
        mulheres += 1

    print('='*30)

    escolha = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

    while escolha not in 'S' and escolha not in 'N':
        escolha = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

    if escolha in 'N':
        print('=' * 30)
        break

print('\n======= FIM DO CADASTRO =======')
print(f"""Total de pessoas com mais de 18 anos: {pessoas}
Ao todo temos {homens} homens cadastrados
E temos {mulheres} mulheres com menos de 20 anos""")
