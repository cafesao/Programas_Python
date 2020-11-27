import random 
dado = [1,2,3,4,5,6,7,8]
jogadores = {}
jogo = []
cont = 1
for c in range(1,5):
    jogadores['jogador'] = str(input(f'Digite o nome do jogador {c}: ')).capitalize()
    jogadores['dado'] = str(random.choice(dado))
    jogo.append(jogadores.copy())
    jogadores.clear()
jogo = sorted(jogo, key=lambda k: k['dado'], reverse=True)
for c in range(0,4):
    print()
    print(f'{cont}º jogador: ')
    print(f'O jogador {jogo[c]["jogador"]}', end=' ')
    print(f'tirou {jogo[c]["dado"]} no dado')
    cont += 1
    print()
    print('-------------------------------------------')