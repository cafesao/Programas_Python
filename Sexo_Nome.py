# Uma pesquisa, mostrando varios dados no final, podendo inserir mais pessoas caso necessario.


i1 = i2 = s1 = 0
while True:
    i = int(input('Digite sua idade: '))
    s = str(input('Qual seu sexo (F - Feminino / M - Masculino):  ')).split()[0].upper()
    if i > 18:
        i1 += 1
    if s in 'M':
        s1 += 1
    if s in 'F' and (i < 20):
        i2 += 1
    c = str(input('\nDeseja inserir mais pessoas (S - SIM / N - NÃO): ')).split()[0].upper()
    if c in 'N':
        break
if i1 == 1:
    print(f'\n{i1} pessoa tem mais de 18 anos')
else:
    print(f'\n{i1} pessoas tem mais de 18 anos')
if s1 == 1:
    print(f'\n{s1} homem foi cadastrado')
else:
    print(f'\n{s1} homens foram cadastrados')   
if i2 == 1:   
    print(f'\n{i2} mulher tem menos de 20 anos')
else: 
    print(f'\n{i2} mulheres tem menos de 20 anos')
print('\nObrigado por utilizar o cadastramente de sexo e nome')