


jogador = {}
gols = []
tg = int(0)
jg = int(0)
while True:
    jn = str(input('Digite seu nome: ')).capitalize()
    jp = int(input('Digite quantas partidas você jogou: '))
    for c in range(1,jp+1):
        n = int(input(f'Digite quantos gols você conseguiu na partida {c}: ')) 
        tg = tg + n
        gols.append(n)
    jg = gols
    jogador['nome'].append(jn)
    jogador['partida'].append(jp)
    jogador['gols'].append(jg)
    r = str(input('Deseja adicionar mais jogadores? (S - Sim/N - Não): ')).split()[0].capitalize()
    if r == 'N':
        break
print(jogador)
    #for c in jogador.values():
    #    print(c)
    #print(f'O jogador {c["nome"]} conseguiu {c["gols"]} gols em {c["partidas"]} partidas, totalizando {tg} gols na temporada,', end='')
    #print(f' uma media de {tg/c:.2f} gols por partida')
    #ERRO PROGRAMA SUBSTITUINDO