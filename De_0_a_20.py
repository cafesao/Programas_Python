numeros = ('Zero', 'Um' , 'Dois' , 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
n = int(input('Digite um numero de 0 a 20: '))
while True:
    if n > 20 or n < 0:
        while n > 20 or n < 0: 
            print('Você digitou errado, tente novamente')
            n = int(input('Digite um numero de 0 a 20: '))
    if n == 0:
        print(numeros[0])
        break
    if n == 1:
        print(numeros[1])
        break
    if n == 2:
        print(numeros[2])
        break
    if n == 3:
        print(numeros[3])
        break
    if n == 4:
        print(numeros[4])
        break
    if n == 5:
        print(numeros[5])
        break
    if n == 6:
        print(numeros[6])
        break
    if n == 7:
        print(numeros[7])
        break
    if n == 8:
        print(numeros[8])
        break
    if n == 9:
        print(numeros[9])
        break
    if n == 10:
        print(numeros[10])
        break
    if n == 11:
        print(numeros[11])
        break
    if n == 12:
        print(numeros[12])
        break
    if n == 13:
        print(numeros[13])
        break
    if n == 14:
        print(numeros[14])
        break
    if n == 15:
        print(numeros[15])
        break
    if n == 16:
        print(numeros[16])
        break
    if n == 17:
        print(numeros[17])
        break
    if n == 18:
        print(numeros[18])
        break
    if n == 19:
        print(numeros[19])
        break
    if n == 20:
        print(numeros[20])
        break     