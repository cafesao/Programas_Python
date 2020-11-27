# Mostra o custo da viagem, pedindo ao user a distancia.


n1 = int(input('Digite a distancia em Km: '))
if n1 <= 200:
    pr1 = n1 * 0.50
    print(f'Sua viagem vai custar R${pr1}')
else:
    pr2 = n1 * 0.45
    print(f'Sua viagem vai custar R${pr2}')    