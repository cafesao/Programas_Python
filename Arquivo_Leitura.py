arq1 = open("arquivos/arquivo1.txt", "r") 
print(arq1.read()) 
print(arq1.tell())
print(arq1.seek(0,0)) 
print(arq1.read(10)) 