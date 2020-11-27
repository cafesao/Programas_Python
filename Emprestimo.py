#O programa aprova ou não um emprestimo de uma casa, referente ao valor do salario do usuario.

while True:
    no1 = str(input('Qual seu nome?: ')) 
    sa1 = int(input('Quanto você ganha mensalmente?: ')) 
    ca1 = int(input('Qual o valor da casa?: ')) 
    an1 = int(input('Em quantos anos você quer pagar a casa?: '))
    no2 = no1.split()[0].capitalize()
    men1 = ca1 / (an1 * 12)
    if men1 > (sa1 * 0.3) :
        print(f'Infelizmente Sr.(a) {no2}, o seu emprestimo foi negado por exceder o limite de 30% do seu salario ')
    else: 
        print(f'Parabens Sr.(a) {no2}, seu emprestimo foi aprovado, o valor mensal que você deve pagar é de R$ {men1:.2f}')
    r = str(input('Deseja recomeçar? (Sim / Não): ')).split()[0].upper()
    if r[0] == 'N':
        break         
print('\nObrigado por utilizar Natação.')
