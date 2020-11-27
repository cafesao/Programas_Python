# Programa que faz uma pesdquisa com as pessoas informadas, mostrando a media,
# O homem mais velho e quantas mulheres tem menos de 20 anos.


soma = media = s1 = i1maior = s2 = int(0)
n1velho = str('')
i1velho = int(20)
c1 = int(input('Quantas pessoas você quer adicionar: '))
for c in range(0,c1):
   n1 = str(input('Digite seu nome: '))  
   i1 = int(input('Digite sua idade: '))
   s1 = str(input('Digite seu sexo: (M = Masculino / F = Feminino): '))
   soma = soma + i1
   if s1 in 'Mm' and i1 > i1maior:
       i1maior = i1
       n1velho = n1
   elif i1 <= i1velho:
        s2 = s2 + 1
n1velho = n1velho.capitalize()
print(f'A media de idade do grupo é {soma/c1:.1f}')
print(f'O homem mais velho é {n1velho} com {i1maior} anos')
print(f'{s2} mulheres tem menos de 20 anos')