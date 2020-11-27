full_data = []
contador_linha = contador_coluna = 0

s = open("arquivos/salarios.csv", "r")
data = s.read()
linhas = data.split('\n')
for linha in linhas:
    split_row = linha.split(',')
    full_data.append(split_row)
    first_row = full_data[0]
for linha in full_data:
    contador_linha += 1
for coluna in first_row:
    contador_coluna += 1
print(f"\nTem {contador_linha} linhas")
print(f"Tem {contador_coluna} colunas")