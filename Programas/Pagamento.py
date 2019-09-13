# Programa para pagamento, aceitando Á vista, cartão em 2x, 3x ou mais vezes.
# Mostrando no final o desconto ou o juros e o total


nom1 = str(input('Qual seu nome?: '))
val1 = float(input('Qual o valor do produto: '))
nom2 = nom1.split()
nom2 = nom2[0]
nom2 = nom2.capitalize()
print('Digite a opção desejada para a forma de pagamento correspondente:')
print('''
[1] Opção para Dinheiro/Cheque
[2] Opção para Cartão (À Vista)
[3] Opção para Cartão (Em 2x Vezes)
[4] Opção para Cartão (Em 3x Vezes ou mais)
''')
op1 = int(input('Digite o numero da opção desejada: '))
if op1 == 1:
    val2 = val1- (val1 * 0.1) 
    print(f'Sr.(a) {nom2} escolheu a opção de Dinheiro/Cheque\n ')
    print(f'Você ira receber um desconto de 10%, ficando o valor de R${val2:.2f}')
elif op1 == 2:
    val2 = val1 - (val1 * 0.05)
    print(f'Sr.(a) {nom2} escolheu a opção de Cartão (À vista)\n ')
    print(f'Você ira receber um desconto de 5%, ficando o valor de R${val2:.2f}')
elif op1 == 3:
    print(f'Sr.(a) {nom2} escolheu a opção de Cartão (2x Vezes)\n ')
    print(f'Você ira pagar o valor normal, que no caso é R${val1}')
elif op1 == 4: 
    val2 = val1 + (val1 * 0.2)  
    print(f'Sr.(a) {nom2} escolheu a opção de Cartão (3x Vezes ou mais)\n ')
    print(f'Você ira receber um juros de 20%, ficando o valor de R${val2:.2f}')     