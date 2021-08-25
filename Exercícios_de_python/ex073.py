print('\033[1;93m-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\033[m')
print('\033[1;31m       TIMES DE FUTEBOL\033[m')
print('\033[1;93m-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\033[m')
times = ("Atlético-MG", "Palmeiras", "Fortaleza", "Bragantino", "Flamengo", "Corinthians",
         "Atlético-GO", "Ceará SC", "Athletico-PR", "Internacional", "Santos",
         "São Paulo", "Juventude", "Cuiabá", "Bahia", "Fluminense", "Grêmio",
         "Sport Recife", "América-MG", "Chapecoense")
print('=-='*10)
print(f'Lista de times do Brasileirão: {times}')
print('=-='*10)
print(f'Os 5 primeiros são {times[0:5]}')
print('=-='*10)
print(f'Os 4 últimos são {times[-4::]}')
print('=-='*10)
print(f'Times na ordem alfabética: {sorted(times)}')
print('=-='*10)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª posição')
print('=-='*10)
