# Este e um programa de Caixa Eletronico, que tem cedulas de R$50, R$20, R$ 10, R$1


saque = total_cedulas = int(0)
cedulas = int(50)
print('BEM VINDO AO CAIXA ELETRÔNICO')
saque = int(input('\nDigite o valor que você deseja sacar: '))
print()
while True:
    if saque >= cedulas:
        saque -= cedulas
        total_cedulas += 1
    else:
        if total_cedulas > 0:
            print(f'Você sacou {total_cedulas} cédulas de R${cedulas} ')
        if cedulas == 50:
            cedulas = 20
        elif cedulas == 20:
            cedulas = 10
        elif cedulas == 10:
            cedulas = 1
        total_cedulas = int(0) 
        if saque == 0:
            break
print('\nObrigado por utilizar o Caixa Eletronico.\n')