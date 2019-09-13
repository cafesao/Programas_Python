# Converte o numero informado para Binario, Octadecimal ou Hexadecimal, dando a
# opção de converter o numero para todas as opções acima.


while True:
    nu1 = int(input('Digite um valor: '))
    print('''Escolha uma das bases:
[1] Converter para Binario
[2] Converter para Octadecimal
[3] Converter para Hexadecimal
[4] Todas as opções''')
    op = int(input('\nSua opção: '))
    if op == 1:
        print(f'Seu numero convertido para Binario é {bin(nu1)}')
    elif op == 2:
        print(f'Seu nomero convertido para Octadecimal é {oct(nu1)}')
    elif op == 3:
        print(f'Seu nomero convetido para Hexadecimal é {hex(nu1)}')
    elif op == 4:  
        print(f'Binario: {bin(nu1)} \nOctadecimal: {oct(nu1)} \nHexadecimal: {hex(nu1)}')
    else:      
        print('Você digitou a opção errada.')
    r = str(input('Deseja recomeçar? (Sim / Não): ')).split()[0].upper()
    if r[0] == 'N':
        break            
print('\nObrigado por utilizar Conversor.')