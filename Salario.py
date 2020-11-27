# Este programa tem como objetivo mostrar qual o seu salario por ano.

print('Ola, irei fazer algumas perguntas :) \n')
nome = str(input('Qual seu nome?: ')) 
nome1 = nome.split()
idade = int(input(f'Ola Sr.(a) {nome1[0]} \nQual a sua idade?: '))
salario = float(input('Qual seu salario mensal?: '))
print(f'O Sr.(a) {nome1[0]} \nCom uma idade de {idade}, com o salario mensal de R${salario}, recebe por ano o valor de R${salario*12}')