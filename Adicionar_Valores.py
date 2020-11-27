#Variaveis
lista_valores = list()
cont_vezes = num_Cinco = int(0)
resposta = str()

#Adição de valores
while True:
    numero_user = int(input('Digite um valor inteiro: '))
    cont_vezes += 1
    if numero_user not in lista_valores:
        lista_valores.append(numero_user)
    resposta = str(input('Deseja continuar? (Sim / Não): ')).split()[0].upper()
    if resposta == 'N':
        break

#Mostrar as listas
lista_valores.sort()
print(f'\nA lista de forma crescente: {lista_valores}')
lista_valores.sort(reverse=True)
print(f'A lista de forma decrescente: {lista_valores}')
print(f'\nVocê digitou {cont_vezes} vezes')

#Mostra se tem ou não o numero 5
if 5 in lista_valores:
   print(f'\nNa lista tem o numero cinco')
else:
    print('\nNão tem não tem o numero cinco')