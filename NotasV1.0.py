# Este programa um pouco mais copmplexo que a versão anterior, pede para que o usuario informa as notas e quantas notas serão lançadas.
# Para que o programa calcule a media entre as notas lançadas.

print('Bem-Vindo ao programa Media_Notas V1.0\n')
c = int(1)
while (c > 0):
    print('Verifique as opções de quantas notas você ira lançar e depois selecione a opção digitando o numero correspontende: ')
    print('''[1] Se você deseja lançar 2 nota
    [2] Se você deseja lançar 3 notas
    [3] Se você deseja lançar 4 notas
    [4] Se você deseja lançar 5 notas
    [5] Se você deseja lançar 6 notas
    [6] Se você deseja lançar 7 notas\n''')
    com1 = int(input('Digite a sua opção: '))
    if com1 == 1:
        no1 = float(input('\nDigite a primeira nota: '))
        no2 = float(input('Digite a segunda nota: '))
        media = (no1 + no2) / 2
        print(f'Sua media é {media:.2f}')
    elif com1 == 2:
        no1 = float(input('\nDigite a primeira nota: '))
        no2 = float(input('Digite a segunda nota: '))
        no3 = float(input('Digite a terceira nota: '))
        media = (no1 + no2 + no3) / 3
        print(f'Sua media é {media:.2f}')
    elif com1 == 3:
        no1 = float(input('\nDigite a primeira nota: '))
        no2 = float(input('Digite a segunda nota: '))
        no3 = float(input('Digite a terceira nota: '))
        no4 = float(input('Digite a quarta nota: '))
        media = (no1 + no2 + no3 + no4) / 4
        print(f'Sua media é {media:.2f}')
    elif com1 == 4:
        no1 = float(input('\nDigite a primeira nota: '))
        no2 = float(input('Digite a segunda nota: '))
        no3 = float(input('Digite a terceira nota: '))
        no4 = float(input('Digite a quarta nota: '))
        no5 = float(input('Digite a quinta nota: '))
        media = (no1 + no2 + no3 + no4 + no5) / 5
        print(f'Sua media é {media:.2f}')
    elif com1 == 5:
        no1 = float(input('\nDigite a primeira nota: '))
        no2 = float(input('Digite a segunda nota: '))
        no3 = float(input('Digite a terceira nota: '))
        no4 = float(input('Digite a quarta nota: '))
        no5 = float(input('Digite a quinta nota: '))
        no6 = float(input('Digite a sexta nota: '))
        media = (no1 + no2 + no3 + no4 + no5 + no6) / 6
        print(f'Sua media é {media:.2f}')
    elif com1 == 6:
        no1 = float(input('\nDigite a primeira nota: '))
        no2 = float(input('Digite a segunda nota: '))
        no3 = float(input('Digite a terceira nota: '))
        no4 = float(input('Digite a quarta nota: '))
        no5 = float(input('Digite a quinta nota: '))
        no6 = float(input('Digite a sexta nota: '))
        no7 = float(input('Digite a setima nota: '))
        media = (no1 + no2 + no3 + no4 + no5 + no6 + no7) / 7
        print(f'Sua media é {media:.2f}')
    print('\n[1] Repetir')
    print('[0] Finalizar \n')
    c = int(input('Digite a opção: '))              
print('\nObrigado por utilizar Notas.')