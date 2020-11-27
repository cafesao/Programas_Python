# Um jogo de Pedra, Papel e Tesoura, ou como e chamado em algumas partes do mundo, Jó-Ken-Pô

import random
import time
user1 = cpu1 = c = str
lista1 = ['Pedra','Papel','Tesoura']
lista2 = ['S','N']
print('Bem vindo ao Pedra,Papel ou Tesoura!!')
while True:
    user1 = str(input('\nO que você quer jogar, Pedra, Papel ou Tesoura: ')).split()[0].capitalize()
    if user1 not in lista1:
        while user1 not in lista1:
            print('Você digitou errado, digite corretamente sua escolha.')
            user1 = str(input('\nO que você quer jogar, Pedra, Papel ou Tesoura: ')).split()[0].capitalize()
    cpu1 = random.choice(lista1)
    if cpu1 in 'Pedra':
        if user1 in 'Papel':
            print('\nHmmmmmm...o computador esta escolhendo...')
            time.sleep(2)
            print(f'\nVocê ganhou, o computador jogou {cpu1}')
        if user1 in 'Pedra':
            print('\nHmmmmmm...o computador esta escolhendo...')
            time.sleep(2)            
            print(f'\nOps, vocês empataram, o computador também jogou {cpu1}')
        if user1 in 'Tesoura':
            print('\nHmmmmmm...o computador esta escolhendo...')
            time.sleep(2)            
            print(f'\nPutz, você perdeu, o computador jogou {cpu1}') 
    if cpu1 in 'Papel':
        if user1 in 'Papel':
            print('\nHmmmmmm...o computador esta escolhendo...')
            time.sleep(2)            
            print(f'\nOps, vocês empataram, o computador também jogou {cpu1}')
        if user1 in 'Pedra':
            print('\nHmmmmmm...o computador esta escolhendo...')
            time.sleep(2)            
            print(f'\nPutz, você perdeu, o computador jogou {cpu1}')
        if user1 in 'Tesoura':
            print('\nHmmmmmm...o computador esta escolhendo...')
            time.sleep(2)            
            print(f'\nVocê ganhou, o computador jogou {cpu1}')
    if cpu1 in 'Tesoura':
        if user1 in 'Papel':
            print('\nHmmmmmm...o computador esta escolhendo...')
            time.sleep(2)            
            print(f'\nPutz, você perdeu, o computador jogou {cpu1}')
        if user1 in 'Pedra':
            print('\nHmmmmmm...o computador esta escolhendo...')
            time.sleep(2)            
            print(f'\nVocê ganhou, o computador jogou {cpu1}')
        if user1 in 'Tesoura':
            print('\nHmmmmmm...o computador esta escolhendo...')
            time.sleep(2)            
            print(f'\nOps, vocês empataram, o computador também jogou {cpu1}')         
    c = str(input('\nDeseja recomeçar? [S - Sim/N - Não]: ')).split()[0].capitalize()
    if c not in lista2:
        while c not in lista2:
            print('Você digitou errado, digite novamente.')
            c = str(input('\nDeseja recomeçar? [S - Sim/N - Não]: ')).split()[0].capitalize()
    if c in 'N':
        break
print('\nObrigado por jogar.')