# Mostra os multiplos de Três


c1 = int(0)
for c in range(1,501,2):
    if (c % 3) == 0:
        c1 = c1 + c
print(c1)        