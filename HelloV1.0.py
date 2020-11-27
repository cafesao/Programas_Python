


while True:
    n1 = str(input('Digite uma frase ou palavra: '))
    n1 = n1.capitalize()
    print(f'Frase: {n1}')
    r = str(input('Deseja recomeçar? (Sim / Não): ')).split()[0].upper()
    if r[0] == 'N':
        break            
print('\nObrigado por utilizar Hello.')