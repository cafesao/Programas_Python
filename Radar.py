# Programa para radar de transito, pedindo ao user a velocidade do veiculo.


ve = int(input('Digite a velocidade do veiculo: '))
if ve > 80:
    ve1 = ve - 80
    print('Você estava acima do limite de velocidade 80Km/h \n')
    print(f'Sua velocidade atual é {ve}km, por isso você foi multado em R${ve1*7}')
else:
    print('Você não foi multado.')     