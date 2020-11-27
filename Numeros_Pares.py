# Pede um valor é mostra todos os numeros pares até aquele valor

c = int(input('Digite um valor: '))
for c in range(0, c+1):
    if (c % 2) == 0:
        print(c)