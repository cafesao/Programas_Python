# Mostra o maior, menos e a média de todos os numeros informados.


n = re = ri = ma = int(0)
c = 1
me = 9999999
while True:
    for c in range(0,4):
        n = int(input('Digite um valor: '))
        if n < me:
            me = n
        if n > ma:
            ma = n
        re = re + n
        ri = ri + 1  
    r = str(input('Deseja continuar? (Sim / Não): ')).split()[0].upper()
    if r[0] == 'N':
        break
ri = re / ri
print(f'O maior número é {ma}, o menor é {me} e a média é {ri:.2f}\n')  