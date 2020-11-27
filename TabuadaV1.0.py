# Este codigo serve como tabuada, você insere 1 valores e ele calcular de 0 a 10.
# O programa para quando você digita um valor negativo


while True:
    b = int(input('\nInsira o valor a ser multiplicado: '))
    if b < 0:
        break
    n = int(input('Insira quantas vezes quer que o numero seja multiplicado: '))
    for c in range(0,n+1):
        print(f'{b} * {c} = {b*c}')
print('Obrigado por utilizar a Tabuada.')