# Este programa soma todos os numeros que o usuario digitar, infinitamente, até que, o flag
# seja alcançado, que e quando o usuario digitar 999

n = re = qn = 0
while True:
    n = int(input('Digite um valor: '))
    if n == 999:
        break
    re += n
    qn += 1    
print(f'\nVocê digitou {qn} numeros, a soma de todos so numeros foi de {re}')
  