# Cadastramento de varios produtos, no final mostrando algumas informaçoes para o user.


n1 = cpro = int(0)
mpre = tpre = pre = float(0)
f = 1
pro = pause = nmp = str
while True:
    pro = str(input('Digite o nome do produto: ')).capitalize()
    pre = float(input('Digite o preço do produto: '))
    tpre = pre + tpre
    cpro = cpro + 1
    if pre > 1000:
        n1 = n1 + 1
    while f >= 1:
        mpre = pre
        f = 0
        nmp = pro
    if pre < mpre:
        mpre = pre
        nmp = pro
    pause = str(input('Deseja cadastrar novos produtos? (S - Sim / N - Não): ')).capitalize()
    if pause in 'N':
        break
print(f'O total de produtos cadastrados foi de {cpro}.')
print(f'O total das suas compras foi de R${tpre:.2f}.')
print(f'{n1} produtos custam mais de 1000 reais.')
print(f'O produto {nmp} que custa R${mpre:.2f}, é o produto mais barato cadastrado.')