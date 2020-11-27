# Programa que pede ao user o nome e o salario, e no final mostra o aumento e o salario novo,
# Junto com o salario antigo.


n1 = str(input('Digite seu nome: '))
s1 = int(input('Digite seu salario: '))
n2 = n1.split()
if s1 >= 1250:
    s2 = (s1 * 0.1) + s1
    p = 10
else:
    s2 = (s1 * 0.15) + s1
    p = 15  
print(f' \nOlá {n2[0]}, seu salario atual é R${s1}, você recebeu um aumento de {p}%,', end = '')
print(f' sendo assim, seu salario novo é R${s2}')     