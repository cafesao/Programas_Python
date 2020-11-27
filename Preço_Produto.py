from tabulate import tabulate
table1 = (('Arroz','R$ 3.90',),('Feijão','R$ 8.90'),('Banana','R$ 3.50'),('Mortadela','R$ 4.50'),('Bolacha','R$ 2.20'))
print('-'*18)
print('Lista de preços')
print(tabulate(table1))